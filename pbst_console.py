
import os
import sys
import hashlib
import re
import uuid

# Lista variabili
vars_list = [
    "PYCHARM_PROJECT_ID",
    "PYCHARM_UUID",
    "PBST_CONSOLE_ID",
    "PBST_UUID",
    "USERNAME",
    "USERDOMAIN"
]

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
    os.environ["PBST_CONSOLE_ID"] = PBST_CONSOLE_ID_HEX

    # Ottieni i valori delle variabili (o usa valori di default se non esistono)
    pbst_console_id = os.environ.get("PBST_CONSOLE_ID", "")
    pycharm_project_id = os.environ.get("PYCHARM_PROJECT_ID", "")
    pycharm_uuid = os.environ.get("PYCHARM_UUID", "")

    # Combina i valori in una stringa unica
    combined = f"{pbst_console_id}:{pycharm_project_id}:{pycharm_uuid}"

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
            print(f"{variabile} non è impostata.")

    # versione e piattaforma
    print('Python %s on %s' % (sys.version, sys.platform),end='\n\n')

def start():
    pbst_console_id()
    view_vars()

def check_variabili_ambiente(ds):
    """
    confronta tutte le variabili presenti in formato var=value
    con le stesse variabili di ambiente
    :param ds: docstring
    :return: true/false in funzione della riuscita di tutti i confronti
    """
    # Trova tutte le coppie var=value nella docstring
    pattern = r"(\w+)=(\S+)" # regex101
    matches = re.findall(pattern, ds)

    # Confronta ogni coppia con le variabili di ambiente
    value: str
    env_value: str
    for var, value in matches:
        env_value = os.environ.get(var)
        if var not in vars_list:
            pass
        elif env_value != value:
            return False

    return True

class PbstConsoleError(BaseException):
    """ check console non superato """
    def __init__(self, message):
        self.message = message
        super().__init__(f"{self.message}")

def check(ds):
    if os.environ.get("PBST_CONSOLE_ID") is None:
        pbst_console_id()
    result = check_variabili_ambiente(ds)
    if not result:
        view_vars()
        raise PbstConsoleError("PBST CONSOLE !!! corrupted !!!!")
    else:
        print("PBST CONSOLE ended succesfully.")