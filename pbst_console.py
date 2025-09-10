
import os
import sys
import hashlib
import re
import uuid

# Lista variabili
vars_list = [
#    "PYCHARM_PROJECT_ID",
#    "PYCHARM_UUID",
    "PBST_CONSOLE_ID_v2",
#    "PBST_UUID",
    "USERNAME",
    "USERDOMAIN"
]
def is_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False

def pbst_console_id():
    # Ottieni le variabili di ambiente
    username = os.environ.get("USERNAME", "")
    userdomain = os.environ.get("USERDOMAIN", "")

    # Combina i valori in sequenza
    combined = f"{username}:{userdomain}"

    # Calcola l'hash SHA-256 e prendi i primi 8 byte (16 caratteri esadecimali)
    hash_bytes = hashlib.sha256(combined.encode()).digest()
    PBST_CONSOLE_ID = hash_bytes[:8]  # Prendi i primi 8 byte dell'hash

    # Converti in stringa esadecimale (opzionale, per leggibilità)
    PBST_CONSOLE_ID_HEX = PBST_CONSOLE_ID.hex()

    # Imposta PBST_CONSOLE_ID come variabile di ambiente
    os.environ["PBST_CONSOLE_ID_v2"] = PBST_CONSOLE_ID_HEX

    # Ottieni i valori delle variabili (o usa valori di default se non esistono)
    pbst_console_id = os.environ.get("PBST_CONSOLE_ID_v2", "")
    pycharm_project_id = os.environ.get("PYCHARM_PROJECT_ID", "")
    pycharm_uuid = os.environ.get("PYCHARM_UUID", "")

    combined = f"{pbst_console_id}"
    if  os.environ.get("PYCHARM_PROJECT_ID", "") != "":
        combined = f"{combined}:{pycharm_project_id}"
    if os.environ.get("PYCHARM_UUID", "") != "":
        combined = f"{combined}:{pycharm_uuid}"

    # Usa un namespace fisso (NAMESPACE_URL)
    namespace = uuid.NAMESPACE_URL

    # Genera l'UUIDv5
    custom_uuid = uuid.uuid5(namespace, combined)

    # Imposta PBST_UUID come variabile di ambiente
    os.environ["PBST_UUID"] = f"{custom_uuid}"


def view_vars():

    # Stampa solo le variabili specificate, una per riga
    for variabile in vars_list:
        value = os.environ.get(variabile)
        if value is not None:
            print(f"{variabile}={value}")
        else:
            print(f"{variabile} is not setting.")

    # versione e piattaforma
    print('%sPython %s on %s%s' % ("\n",sys.version, sys.platform,"\n"))


def start():
    '''
    Lancia la console IPython e costruisce le variabili di ambiente
    :return:
    '''
    msg_err = "PBST CONSOLE must IPython not standard console: "\
              "install IPython and setting it as console if available"
    if not is_ipython():
        raise PbstConsoleError(msg_err)
    pbst_console_id()
    view_vars()


def check_variabili_ambiente(ds, dbg=False):
    """
    confronta tutte le variabili presenti in formato var=value
    con le stesse variabili di ambiente
    :param ds: docstring
    :return: true/false in funzione della riuscita di tutti i confronti
    """
    msg_err = "PBST vars not all present: check your docstring"
    # Trova tutte le coppie var=value nella docstring
    pattern = r"(\w+)=(\S+)" # regex101
    matches = re.findall(pattern, ds)

    # se le variabili PBST non sono tutte presenti in docstring segnalo errore
    vars_in_docstring = {k for k, v in matches}
    vars_pbst_presenti: bool = all(k in vars_list for k in vars_in_docstring)
    if not vars_pbst_presenti:
        raise PbstConsoleError(msg_err)

    # Confronta ogni coppia var=val trovata
    # con le variabili di ambiente
    value: str
    env_value: str
    for var, value in matches:
        env_value = os.environ.get(var)
        if var not in vars_list:
            pass
        elif env_value != value:
            if dbg:
                print(f"{var},{value},{env_value}")
            return False
    return True


class PbstConsoleError(BaseException):
    """ check console non superato """
    def __init__(self, message):
        self.message = message
        super().__init__(f"{self.message}")


def check(ds,dbg=False):
    msg_err = "PBST CONSOLE session changed ( must be once ) or corrupted!"
    msg_ok  = "PBST CONSOLE checked."
    if os.environ.get("PBST_CONSOLE_ID") is None:
        pbst_console_id()
    result = check_variabili_ambiente(ds,dbg=dbg)
    if not result:
        view_vars()
        print(flush=True)
        raise PbstConsoleError(msg_err)
    else:
        print(msg_ok)