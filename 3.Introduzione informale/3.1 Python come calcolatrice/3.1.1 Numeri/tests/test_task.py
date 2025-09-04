# NON ELIMINARE import __init__
import __init__

import os
import sys
import logging
import colorlog

def print_color(text: str, color: str = "white", bold: bool = False, end: str = ""):
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }
    bold_code = "\033[1m" if bold else ""
    reset_code = "\033[0m"
    print(f"{bold_code}{colors[color]}{text}{reset_code}",end=end)

# set logger
pbst_log_level_default = logging.getLevelName(logging.ERROR)
pbst_log_level=os.getenv("PBST_LOG_LEVEL",pbst_log_level_default).upper()
pbst_log_name = f"PBST_LOG:{os.path.dirname(os.path.dirname(__file__)).split('\\')[-1]}"
logger = logging.getLogger(pbst_log_name)
try:
    logger.setLevel(pbst_log_level)
except Exception as e:
    print_color("Failed to set PBST log level to {}.\n".format(pbst_log_level, pbst_log_level_default),"red")
    pbst_log_level = pbst_log_level_default
    logger.setLevel(pbst_log_level)

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(name)s:%(asctime)s:%(levelname)s:%(reset)s %(message)s",
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'black,bg_red',
    },
    secondary_log_colors={},
    style='%'
)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

if pbst_log_level in ["DEBUG", "INFO", "WARNING"] :
    logger.info(f"log level set to {pbst_log_level}")
else:
    testo_colorato = {
        "PBST log level set to " : "blue",
        pbst_log_level: "red",
        " as default.\n( set environment variable PBST_LOG_LEVEL=" : "blue",
        "INFO" : "green",
        " or " : "blue",
        "DEBUG" : "yellow",
        " in Run Configuration).\n" : "blue"
    }
    for k, v in testo_colorato.items():
        print_color(k, v, end="")


logger.info(f"start task {pbst_log_name}")

# il riferimento a outputConsole verrà risolto dinamicamente dalla import __init__
# e verrà eseguito il task relativo
from task import output_console as oc

logger.info(f"end task {pbst_log_name}\n")

# partenza test_task
logger.info(f"start test_task {pbst_log_name}")
try:
    from rePatterns import EXP_CON_PARENTESI as EXP_CON_PARENTESI
except ImportError as ie:
    msg_debug = f"\nfile:{__file__}\ndir:{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}"
    logger.debug(msg_debug)
    msg_info = f"append to sys.path '{os.path.abspath(os.path.dirname(__file__))}'"
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    logger.info(msg_info)
from rePatterns import EXP_CON_PARENTESI as EXP_CON_PARENTESI
from rePatterns import EXP_SENZA_DIV as EXP_SENZA_DIV
from rePatterns import EXP_SOLO_NATURALI as EXP_SOLO_NATURALI
from rePatterns import EXP_CON_DIV as EXP_CON_DIV
from rePatterns import EXP_CON_DIV_TRONCATA as EXP_CON_DIV_TRONCATA
from rePatterns import EXP_UND_CON_DIV_IN_MOD as EXP_UND_CON_DIV_IN_MOD
from rePatterns import EXP_RIS_INT as EXP_RIS_INT
from rePatterns import EXP_RIS_FLOAT as EXP_RIS_FLOAT
from rePatterns import EXP_ASS_INT as EXP_ASS_INT
from rePatterns import EXP_ASS_EXP_INT as EXP_ASS_EXP_INT
from rePatterns import EXP_CON_VARIABILI as EXP_CON_VARIABILI
from rePatterns import EXP_TRACEBACK_NAME_ERROR as EXP_TRACEBACK_NAME_ERROR
from rePatterns import EXP_LIST_IVA_MSG_ERR as EXP_LIST_IVA_MSG_ERR
from rePatterns import EXP_LIST_IVA_PATTERN as EXP_LIST_IVA_PATTERN

import re
import unittest

# suddivide in righe la stringa multilinea
#outputConsole.replace('/', '\\') # rimpiazza ogni slash '/' con backslash '\'
def get_doc_rows():
    return str(oc.__doc__).split('\n')

# preleva tutte le righe precedenti eye_output fino ad un precedente eye_output
# oppure a eye_start_console ( PyDev console: using IPython 9., Python 3.13 )
def catch_rows_from_eye(rows, eye, all_rows=False):
    """
 elimina intestazione dalle righe fino a quella che inizia con eye,
 riga precedente e quella con eye non sono eliminate

    :param rows: stringa multilinea
    :param eye: start linea
                se 'Python 3.13' skip questa e restituisce tutte le altre
                se 'Out[' inserisce la precedente ( istruzione ) e questa che è l'output
    :param all_rows: True comprende anche le successive, default False
    :return:
    """
    # EYES
    PYDEV_CONSOLE_EYE = 'PyDev console: using IPython 9.'
    PYSTD_CONSOLE_EYE = 'Python 3.13'
    SYNTAX_ERROR = 'SyntaxError:'
    IPY_OUT_LINE_EYE = 'Out['
    new_list = []
    for i, riga in enumerate(rows):
        # Se la riga inizia con eye, aggiungiamo la riga precedente alla nuova lista
        # e se All_rows is True aggiungo le righe successive a eye
        if new_list.__len__() >= 0 and all_rows is True:
            if rows[i] != eye:
                new_list.append(rows[i])
        elif (new_list.__len__() == 0
            and eye == PYSTD_CONSOLE_EYE
            and all_rows is True):
            new_list.append(rows[i])
        elif (riga.startswith(eye)
            and new_list.__len__() == 0
            and eye == PYSTD_CONSOLE_EYE):
            all_rows = True  # al primo elemento da inserire se 'Python 3.' imposto di scrivere tutte le successive
        elif riga.startswith(eye) and new_list.__len__() == 0 and eye == IPY_OUT_LINE_EYE:
            # cerco indice i del precedente eye
            k = 0 # indice precedente eye
            for j in range(i-1,0,-1):
                if (rows[j].startswith(IPY_OUT_LINE_EYE)
                or rows[j].startswith(PYSTD_CONSOLE_EYE)
                or rows[j].startswith(SYNTAX_ERROR)
                ):
                    k = j # segno primo eye incontrato
                    break
            for z in range(k + 1, i):
                new_list.append(
                    rows[z])  # al primo elemento da inserire se 'Out[' appendo le righe precedenti
            new_list.append(rows[i])  # e poi il risultato (output generato)
        else:
            pass

    return new_list

def is_out_line(linea: str) -> bool:
    # verifico se Outline di IPython
    return bool(re.fullmatch(r'Out\[\d+]: .*', linea))


def catch_rex_row(self,row,
                  regex,
                  match_group_alone=True,
                  match_group_num=1,
                  pos=1,
                  match_comment_off=None,
                  match_out_line_skip=None,
                  globs=None
                  ):
    group_matched = None
    group_num_matched = None

    if (match_out_line_skip
            and is_out_line(row)):
        log_pbst(self,"row (Out skip): {row}",DEBUG_LVL)
        return group_matched, row, group_num_matched

    if (match_comment_off is not None
            and match_comment_off
            and '#' in row):
        # row non deve avere commenti
        row = row.split('#')[0]
        log_pbst(self,f"row (split comment): {row}",DEBUG_LVL)
    else:
        log_pbst(self,f"row: {row}",DEBUG_LVL)
    matches = re.finditer(regex, row)
    for matchNum, match in enumerate(matches, start=pos):
        # msg_match in cyan se DEBUG e yellow se INFO
        color_set = f"\033[40;36;1m" if pbst_log_level == DEBUG_LVL else "\033[40;33;1m"
        color_reset = f"\033[0m"
        msg_match = "Match {matchNum} was found at {start}-{end}:{start_color} {match} {end_color}"\
            .format(matchNum=matchNum,
                    start=match.start(),
                    end=match.end(),
                    start_color=color_set,
                    end_color=color_reset,
                    match=match.group()
                    )
        log_pbst(self,msg_match,DEBUG_LVL) if pbst_log_level == DEBUG_LVL else log_pbst(self,msg_match,INFO_LVL)
        group_matched = match.group()

        if match_group_alone:
            break

        for group_num in range(0, len(match.groups())):
            group_num = group_num + 1
            msg_group = "Group {groupNum} found at {start}-{end}: {group}"\
                        .format(groupNum=group_num,
                                start=match.start(group_num),
                                end=match.end(group_num),
                                group=match.group(group_num))
            log_pbst(self,msg_group,DEBUG_LVL)
            if match_group_num == group_num:
                group_num_matched = match.group(group_num)

            break
    # se globs eseguo la riga cosi in caso di assegnamento viene aggiornato globals
    # poi rieseguo solo se non ha dato eccezione sperando sia un'espressione
    # todo 'pericolo di iniezione codice' inserire check di espressione o assegnamento
    if globs is not None:
        global crr_row_execution_successfully_completed
        try:
            # se shell IPython Out[...]: non ha effetto, cioè vengono considerati i caratteri successivi
            exec(compile(row, os.devnull, mode='exec'), globs)
            crr_row_execution_successfully_completed = True
            log_pbst(self,f"before _: {_}",DEBUG_LVL)
            log_pbst(self,f"EXEC: {row}",DEBUG_LVL)
            exec(compile(f"_ = {row}", os.devnull, mode='exec'), globs)
            log_pbst(self,f"after _: {_}",DEBUG_LVL)
        except Exception as exc:
            crr_row_execution_successfully_completed = False

    return group_matched, row, group_num_matched


def catch_rex(self,lista,
              regex,
              match_group_alone=True,
              on_match_return_next_row=False,
              on_match_return_group=False,
              match_group_num=1,
              pos=1,
              match_comment_off=None,
              match_out_line_skip=None,
              globs=None
              ):
    matching_done = False
    return_row = None
    group_matched = None
    return_group = None
    for row in lista:
        if on_match_return_next_row and matching_done:
            return_row = row
            break
        elif on_match_return_group and matching_done:
            break
        elif matching_done:
            break
        group_matched, return_row, return_group = catch_rex_row(self, row,
                                                                regex,
                                                                match_group_alone,
                                                                match_group_num,
                                                                pos,
                                                                match_comment_off,
                                                                match_out_line_skip,
                                                                globs)

        if group_matched is not None:
            matching_done = True
    return group_matched, return_row if on_match_return_next_row else None, return_group if on_match_return_group else None

def is_arithmetic_expression(s):
    operatori = {'+', '-', '*', '/', '//', '%', '**'}
    try:
        eval(s, {'__builtins__': None}, {})
    except Exception:
        return False
    for carattere in s:
        if carattere in operatori:
            return True
    return False

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def compact_in_single_line(multiple_instructions: str) -> str:
    # Sostituisce ogni '# ...\n' con ';'
    multiple_instructions = re.sub(r'#.*\n', ';', multiple_instructions)
    # Rimuove tutti i caratteri di newline e spazi
    multiple_instructions = multiple_instructions.replace('\n', ' ')
    # Sostituisce uno o più ';' consecutivi (con eventuali spazi) con un solo ';'
    multiple_instructions = re.sub(r'[;]+', ';', multiple_instructions)
    # Rimuove eventuali spazi residui intorno a ';'
    multiple_instructions = re.sub(r'\s*;\s*', ';', multiple_instructions)
    # Rimuove spazi multipli con uno solo
    multiple_instructions = re.sub(r'\s+', ' ', multiple_instructions)
    # Rimuove eventuali spazi iniziali o finali
    return multiple_instructions.strip()

# globals
_ = None
istruzioni_da_eseguire_insieme: str = ""

DEBUG_LVL = "DEBUG"
INFO_LVL = "INFO"
WARNING_LVL = "WARNING"
ERROR_LVL = "ERROR"
CRITICAL_LVL = "CRITICAL"

def log_pbst(self,msg,level="INFO"):
    log_msg = f"{self._testMethodName}: \n{msg}"
    match level.upper():
        case "DEBUG" : logger.debug(log_msg),
        case "INFO": logger.info(log_msg),
        case "WARNING": logger.warning(log_msg),
        case "ERROR": logger.error(log_msg),
        case "CRITICAL": logger.critical(log_msg)
        case _: logger.info(log_msg)


class TestCase(unittest.TestCase):
    def test_05_parentesi_non_consentite(self):
        log_pbst(self,"started")
        doc_rows = get_doc_rows()
        log_pbst(self,f"doc_rows\n{doc_rows}",DEBUG_LVL)
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}",DEBUG_LVL)

            pattern = EXP_CON_PARENTESI  # verifico che non ci siano parentesi
            msg_err = "parentesi non ammesse nelle espressioni aritmetiche"
            try:
                espressione, no_value, no_value = catch_rex(self,lista, pattern)
                self.assertTrue(espressione is None, msg_err)
            except AssertionError as ae:
                if espressione.startswith("Out[") or \
                    espressione.startswith("Traceback"):
                    continue
                else:
                    log_pbst(self,ae,DEBUG_LVL)
                    break
            except Exception as e:
                msg_err = f"{e}"
            finally:
                if doc_rows == doc_rows_rimanenti:
                    superati_gli_assert = True
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)
        log_pbst(self,"ended successfully.\n")


    def test_10_espressione_con_naturali(self):
        global _
        log_pbst(self,"started")
        doc_rows = get_doc_rows()
        log_pbst(self,f"doc_rows\n{doc_rows}",DEBUG_LVL)

        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}",DEBUG_LVL)
            try:
                pattern = EXP_SOLO_NATURALI  # verifico che ci sia un'espressione con naturali senza divisioni
                msg_err = "espressione aritmetica con numeri naturali senza divisioni non trovata"
                espressione_naturale, row, no_value = catch_rex(self,lista, pattern, on_match_return_next_row=True)
                self.assertTrue(espressione_naturale is not None, msg_err)
                risultato = eval(espressione_naturale)
                msg_err = "risultato espressione aritmetica con naturali con risultato non intero"
                self.assertTrue(type(risultato) == type(1234567890), msg_err)
                pattern = EXP_RIS_INT
                (matched_da_console,
                 no_row,
                 risultato_da_console) = catch_rex_row(self,row,
                                                       pattern,
                                                       match_group_alone=False
                                                       )
                msg_err = f"risultato valutato '{risultato}' dell'espressione aritmetica con naturali '{espressione_naturale}'" \
                          f" non coincide col risultato '{risultato_da_console}' indicato in console"
                self.assertTrue(int(risultato_da_console) == risultato, msg_err)
                msg_err = f"risultato negativo {risultato} nell'espressione aritmetica con naturali {espressione_naturale}"
                self.assertTrue(risultato >= 0, msg_err)
                _ = risultato
                superati_gli_assert = True
            except AssertionError as ae:
                log_pbst(self, ae, DEBUG_LVL)
            except Exception as exc:
                log_pbst(self, exc, DEBUG_LVL)
            finally:
                if doc_rows == doc_rows_rimanenti:
                    break;
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)
        log_pbst(self,"ended successfully.\n")


    def test_20_espressione_con_interi(self):
        global _
        log_pbst(self,"started")
        doc_rows = get_doc_rows()
        log_pbst(self,f"doc_rows\n{doc_rows}",DEBUG_LVL)

        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}",DEBUG_LVL)
            try:
                pattern = EXP_SOLO_NATURALI  # verifico che ci sia un'espressione con naturali
                msg_err = "espressione aritmetica con solo numeri naturali, invece che anche con interi, presente"
                espressione_con_naturali, row, no_value = catch_rex(self,lista, pattern, on_match_return_next_row=True)
                self.assertTrue(espressione_con_naturali is None, msg_err)

                pattern = EXP_SENZA_DIV  # verifico che ci sia un'espressione anche con divisioni
                msg_err = "espressione aritmetica con numeri interi e senza divisioni non presente"
                espressione_con_interi, row, no_value = catch_rex(self,lista, pattern, on_match_return_next_row=True)
                self.assertTrue(espressione_con_interi is not None, msg_err)
                risultato = eval(espressione_con_interi)
                msg_err = "risultato calcolato non intero dell'espressione aritmetica"
                self.assertTrue(type(risultato) == type(1234567890), msg_err)
                pattern = EXP_RIS_INT
                matched_out, no_row, risultato_da_console = catch_rex_row(self,row, pattern, match_group_alone=False)
                msg_err = f"risultato valutato '{risultato}' dell'espressione aritmetica con interi '{espressione_con_interi}'" + \
                          f" non coincide col risultato '{risultato_da_console}' indicato in console"
                self.assertTrue(int(risultato_da_console) == risultato, msg_err)
                _ = risultato
                superati_gli_assert = True
            except AssertionError as ae:
                log_pbst(self, ae, DEBUG_LVL)
            except Exception as exc:
                log_pbst(self,exc,DEBUG_LVL)
            finally:
                if doc_rows == doc_rows_rimanenti:
                    break
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)
        log_pbst(self,"ended successfully.\n")


    def test_30_espressione_con_risultato_float(self):
        global _
        log_pbst(self,"started")
        doc_rows = get_doc_rows()
        log_pbst(self,f"doc_rows\n{doc_rows}",DEBUG_LVL)

        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}",DEBUG_LVL)
            try:
                pattern = EXP_CON_DIV  # verifico che ci sia un'espressione anche con divisioni
                msg_err = "espressione aritmetica con divisioni tra numeri interi, e quindi risultato float, non presente "
                espressione_float, row, no_value = catch_rex(self,lista,
                                                             pattern,
                                                             on_match_return_next_row=True)
                self.assertTrue(espressione_float is not None, msg_err)
                risultato = eval(espressione_float)
                msg_err = "risultato non float dell'espressione aritmetica"
                self.assertTrue(type(risultato) == type(0.123456789), msg_err)
                pattern = EXP_RIS_FLOAT
                matched_group, matched_group_num, risultato_da_console = catch_rex_row(self,row,
                                                                                       pattern,
                                                                                       match_group_alone=False)
                msg_err = f"risultato valutato '{risultato}' dell'espressione aritmetica con interi '{espressione_float}' \
                                non coincide col risultato '{risultato_da_console}' indicato in console"
                self.assertTrue(float(risultato_da_console) == risultato, msg_err)
                _ = risultato
                superati_gli_assert = True
            except AssertionError as ae:
                log_pbst(self, ae, DEBUG_LVL)
            except Exception as exc:
                log_pbst(self,exc,DEBUG_LVL)
            finally:
                if doc_rows == doc_rows_rimanenti:
                    break
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)
        log_pbst(self,"ended successfully.\n")


    def test_40_divisione_troncata(self):
        global _
        log_pbst(self,"started")
        doc_rows = get_doc_rows()
        log_pbst(self,f"doc_rows\n{doc_rows}",DEBUG_LVL)

        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}",DEBUG_LVL)
            try:
                pattern = EXP_CON_DIV_TRONCATA  # verifico che ci sia un'espressione anche con divisione troncata
                msg_err = "espressione aritmetica con divisione troncata non presente"
                espressione_intero, row, no_value = catch_rex(self,lista,
                                                              pattern,
                                                              on_match_return_next_row=True)
                self.assertTrue(espressione_intero is not None, msg_err)
                risultato_intero = eval(espressione_intero)
                msg_err = "calcolato risultato non intero dell'espressione aritmetica tra interi con divisione troncata"
                self.assertTrue(type(risultato_intero) == type(123456789), msg_err)
                pattern = EXP_RIS_INT
                matched_group, no_value, risultato_da_console = catch_rex_row(self,row,
                                                                              pattern,
                                                                              match_group_alone=False)
                msg_err = f"risultato valutato '{risultato_intero}', dell'espressione aritmetica con interi e divisione troncata '{espressione_intero}'" + \
                          f", non coincide col risultato '{risultato_da_console}' indicato in console"
                self.assertTrue(int(risultato_da_console) == risultato_intero, msg_err)
                _ = risultato_intero
                # le espressioni senza // bucano quelle rappresentate quindi prima bisogna cercare le doppie //
                # nella stringa
                msg_err = "L'espressione non contiene la divisione troncata"
                self.assertTrue(espressione_intero.count("//") > 0, msg_err)
                superati_gli_assert = True
            except AssertionError as ae:
                log_pbst(self, ae, DEBUG_LVL)
            except Exception as exc:
                log_pbst(self, exc, DEBUG_LVL)
            finally:
                if doc_rows == doc_rows_rimanenti:
                    break
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)
        log_pbst(self,"ended successfully.\n")


    def test_50_underscore_con_divisione_in_modulo(self):
        global _  # impostata da test_40
        global istruzioni_da_eseguire_insieme
        istruzioni_da_eseguire_insieme = ""
        log_pbst(self,"started")
        doc_rows = get_doc_rows()
        log_pbst(self,f"doc_rows\n{doc_rows}",DEBUG_LVL)

        log_pbst(self,f"\nistruzioni da eseguire: {istruzioni_da_eseguire_insieme}\nunderscore: {_}",DEBUG_LVL)
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}",DEBUG_LVL)
            try:
                pattern = EXP_UND_CON_DIV_IN_MOD  # verifico che ci sia un'espressione anche con divisioni
                msg_err = "espressione aritmetica con underscore e divisione in modulo non presente"

                espressione_underscore, row, matched_group_num = catch_rex(self,lista,
                                                                           pattern,
                                                                           on_match_return_next_row=True)
                self.assertTrue(espressione_underscore is not None, msg_err)

                globs = globals()
                log_pbst(self,"_={_}", DEBUG_LVL)
                istruzioni_da_eseguire_insieme += "_ = "
                istruzioni_da_eseguire_insieme += espressione_underscore
                exec(compile(istruzioni_da_eseguire_insieme, 'nul', mode='exec'), globs)
                msg_err = f"risultato '{_}' non decimale dell'espressione aritmetica con divisione in modulo, underscore '{_}'"
                self.assertTrue(type(_) == type(123456789), msg_err)
                pattern = EXP_RIS_INT
                matched_group, no_value, risultato_da_console = catch_rex_row(self,row, pattern, match_group_alone=False)
                msg_err = f"risultato valutato '{_}' dell'espressione aritmetica '{espressione_underscore}'" + \
                          f"non coincide col risultato '{risultato_da_console}' indicato in console"
                self.assertTrue(int(risultato_da_console) == _, msg_err)
                superati_gli_assert = True
            except AssertionError as ae:
                log_pbst(self, ae,DEBUG_LVL)
            except Exception as exc:
                log_pbst(self, exc, DEBUG_LVL)
            finally:
                if doc_rows == doc_rows_rimanenti:
                    break
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)
        _ = None
        istruzioni_da_eseguire_insieme = ""
        log_pbst(self,"ended successfully.\n")


    def test_60_assegnamento_intero(self):
        global istruzioni_da_eseguire_insieme
        log_pbst(self,"started")
        doc_rows = get_doc_rows()
        log_pbst(self,f"doc_rows\n{doc_rows}",DEBUG_LVL)

        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        file_name_to_compile = os.devnull
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}",DEBUG_LVL)
            try:
                pattern = EXP_ASS_INT  # verifico che ci sia un'espressione con assegnamento intero
                msg_err = "assegnamento intero non presente"
                assegnamento_intero, no_row, espressione_numerica = catch_rex(self,lista, pattern)
                self.assertTrue(assegnamento_intero is not None, msg_err)
                exec(compile(assegnamento_intero, file_name_to_compile, mode='exec'))
                istruzioni_da_eseguire_insieme += f"{assegnamento_intero};"
                superati_gli_assert = True
            except AssertionError as ae:
                log_pbst(self, ae, DEBUG_LVL)
            except Exception as exc:
                log_pbst(self, exc, DEBUG_LVL)
            finally:
                if superati_gli_assert or doc_rows == doc_rows_rimanenti:  # trovato o finita lista
                    break
                elif not superati_gli_assert and doc_rows != doc_rows_rimanenti:  # continuare
                    doc_rows = doc_rows_rimanenti
                elif not superati_gli_assert and doc_rows == doc_rows_rimanenti:  # non superato e finita lista
                    continue
                else:
                    self.assertTrue(False, "errore imprevisto in " + self._testMethodName)
        self.assertTrue(superati_gli_assert, msg_err)
        log_pbst(self,"ended successfully.\n")


    # seleziona l'espressione s e check is_arithmetic_expression(s)
    def test_70_assegnamento_espressione_intera(self):
        global istruzioni_da_eseguire_insieme
        log_pbst(self,"started")
        doc_rows = get_doc_rows()
        log_pbst(self,f"doc_rows\n{doc_rows}",DEBUG_LVL)

        log_pbst(self,f"istruzioni_da_eseguire_insieme: \n{istruzioni_da_eseguire_insieme}")
        superati_gli_assert = False
        msg_err = None
        IPY_OUT = 'Out['
        file_name_to_compile = os.devnull
        all_rows = False
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, IPY_OUT, all_rows=all_rows)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}",DEBUG_LVL)
            try:
                pattern = EXP_ASS_EXP_INT  # verifico che ci sia un'espressione con assegnamento intero
                (assegnamento_esp_intera,
                 no_row,
                 espressione_numerica) = catch_rex(self,lista, pattern,
                                                    on_match_return_group=True,
                                                    match_group_alone=False,
                                                    match_group_num=1
                                                   )
                msg_err = "assegnamento espressione intera non presente"
                self.assertTrue(assegnamento_esp_intera is not None, msg_err)
                msg_err = "assegnamento espressione intera non presenta espressione con almeno un operatore"
                self.assertTrue(is_arithmetic_expression(espressione_numerica), msg_err)
                msg_err = "assegnamento espressione intera non presenta un'espressione ma un numero"
                if is_number(espressione_numerica.strip()):
                    doc_rows_rimanenti = lista
                    eye_to_find = assegnamento_esp_intera
                    all_rows = True
                    continue  # proviamo se esiste un'altra riga esclusa quella matched
                globs = globals()
                exec(compile(assegnamento_esp_intera, file_name_to_compile, mode='single'), globs)
                superati_gli_assert = True
                istruzioni_da_eseguire_insieme += f"{assegnamento_esp_intera};"
            except AssertionError as ae:
                log_pbst(self, ae, DEBUG_LVL)
            except Exception as exc:
                log_pbst(self, exc, DEBUG_LVL)
            finally:
                if superati_gli_assert or doc_rows == doc_rows_rimanenti:  # trovato o finita lista
                    break
                elif not superati_gli_assert and doc_rows != doc_rows_rimanenti:  # continuare
                    doc_rows = doc_rows_rimanenti
                elif not superati_gli_assert and doc_rows == doc_rows_rimanenti:  # non superato e finita lista
                    continue
                else:
                    self.assertTrue(False, "errore imprevisto in " + self._testMethodName)
        self.assertTrue(superati_gli_assert, msg_err)
        log_pbst(self,"ended successfully.\n")

    # todo inserire log_pbst

    def test_80_espressione_con_variabili(self):
        globs = globals()
        global istruzioni_da_eseguire_insieme
        global _
        istruzioni_da_eseguire_insieme = ""
        _ = None

        log_pbst(self,"started")
        doc_rows = get_doc_rows()
        log_pbst(self,f"doc_rows\n{doc_rows}",DEBUG_LVL)

        log_pbst(self,f"istruzioni_da_eseguire_insieme: {istruzioni_da_eseguire_insieme}",DEBUG_LVL)
        log_pbst(self,f"_: {_}",DEBUG_LVL)

        superati_gli_assert = False
        msg_err = None
        IPY_OUT = 'Out['
        eye_to_find = IPY_OUT
#        file_name_to_compile = os.devnull
        all_rows = False

        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find, all_rows=all_rows)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}",DEBUG_LVL)
            try:
                espressione_con_variabili = None
                pattern = EXP_CON_VARIABILI  # verifico che ci sia un'espressione con variabili
                                             # il match viene eseguito anche sul commento
                # esegue ogni row tra due OUTPUT se globs è impostata
                # la variabile globale crr_row_execution_successfully_completed è impostata a True da catch_rex_row
                # se la variabile '_' è stata aggiornata vi è stato un assegnamento o la valutazione di un'espressione
                # se si vuole escludere il commento impostare match_comment_off = True
                # se Out[..] deve essere saltata impostare match_out_line_skip=True
                (espressione_con_variabili,
                 row,
                 no_return_group) = catch_rex(self,lista, pattern,
                                                   on_match_return_next_row=True,
                                                   match_comment_off=True,
                                                   globs=globals()  # esegue ogni row
                                                                            )
                msg_err = "espressione con variabili non presente"
                check_ok = espressione_con_variabili is not None and crr_row_execution_successfully_completed
                self.assertTrue(check_ok, msg_err)
                pattern = EXP_RIS_INT  # verifico il risultato prelevato
                lista = []
                lista.append(row)
                matched, no_row, risultato_prelevato = catch_rex(self,lista,
                                                                 pattern,
                                                                 match_group_alone=False,
                                                                 on_match_return_group=True
                                                                 )
                msg_err = f"espressione con variabili '{istruzioni_da_eseguire_insieme}' " + \
                          f"fornita con risultato '{risultato_prelevato}' " + \
                          f"non coincide con quello '{_}' calcolato"
                self.assertTrue(str(_) == risultato_prelevato, msg_err)
                superati_gli_assert = True
            except AssertionError as ae:
                log_pbst(self, ae,DEBUG_LVL)
            except Exception as exc:
                log_pbst(self, exc, DEBUG_LVL)
            finally:
                if superati_gli_assert or doc_rows == doc_rows_rimanenti:  # trovato o finita lista
                    break
                elif not superati_gli_assert and doc_rows != doc_rows_rimanenti:  # continuare
                    doc_rows = doc_rows_rimanenti
                elif not superati_gli_assert and doc_rows == doc_rows_rimanenti:  # non superato e finita lista
                    continue
                else:
                    msg_critical = "condizioni non previste"
                    log_pbst(self, msg_critical, CRITICAL_LVL)
                    self.assertTrue(False, msg_critical + self._testMethodName)
        self.assertTrue(superati_gli_assert, msg_err)
        log_pbst(self,"ended successfully.\n")

    def test_90_Traceback_NameError(self):
        log_pbst(self,"started")
        doc_rows = get_doc_rows()
        log_pbst(self,f"doc_rows\n{doc_rows}",DEBUG_LVL)

        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        all_rows = False
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find, all_rows=all_rows)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}",DEBUG_LVL)
            try:
                pattern = EXP_TRACEBACK_NAME_ERROR  # verifico che ci sia un'espressione che restituisce errore
                stringa_unica_con_cr = "\n".join(lista)
                matches = re.finditer(pattern, stringa_unica_con_cr)
                group_matched = None
                for matchNum, match in enumerate(matches, start=1):
                    msg_match = "Match {matchNum} was found at {start}-{end}: {match}"\
                          .format(matchNum=matchNum,
                                  start=match.start(),
                                  end=match.end(),
                                  match=match.group())
                    log_pbst(self,msg_match)
                    group_matched = match.group()

                msg_err = "Traceback per NameError non presente"
                self.assertTrue(group_matched is not None, msg_err)

                superati_gli_assert = True
            except AssertionError as ae:
                log_pbst(self, ae,DEBUG_LVL)
            except Exception as exc:
                log_pbst(self, exc, DEBUG_LVL)
            finally:
                if superati_gli_assert or doc_rows == doc_rows_rimanenti:  # trovato o finita lista
                    break
                elif not superati_gli_assert and doc_rows != doc_rows_rimanenti:  # continuare
                    doc_rows = doc_rows_rimanenti
                elif not superati_gli_assert and doc_rows == doc_rows_rimanenti:  # non superato e finita lista
                    continue
                else:
                    self.assertTrue(False, "errore imprevisto in " + self._testMethodName)
        self.assertTrue(superati_gli_assert, msg_err)
        log_pbst(self,"ended successfully.\n")

    def test_98_calcola_iva(self):
        global istruzioni_da_eseguire_insieme \
            , exec_tassa_calcolata \
            , _ #  last espressione valutata
        log_pbst(self,"started")

        lista_pattern = EXP_LIST_IVA_PATTERN
        lista_msg_err = EXP_LIST_IVA_MSG_ERR
        lista_length = EXP_LIST_IVA_MSG_ERR.__len__() if EXP_LIST_IVA_MSG_ERR.__len__() == EXP_LIST_IVA_PATTERN.__len__() else 0

        file_name_to_compile = 'nul'
        out_tassa_rilevata = None
        out_costo_rilevato = None
        exec_tassa_calcolata = None
        exec_costo_calcolato = None
        tassa_da_calcolare = costo_da_calcolare = None
        for index_lista in range(lista_length):
            current_pattern = lista_pattern[index_lista]
            current_msg_err = lista_msg_err[index_lista]

            doc_rows = get_doc_rows()
            log_pbst(self, f"doc_rows\n{doc_rows}", DEBUG_LVL)

            superati_gli_assert = False
            msg_err = None
            eye_to_find = 'Python 3.13'
            all_rows = True

            lista = catch_rows_from_eye(doc_rows, eye_to_find, all_rows=all_rows)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            log_pbst(self, f"doc_rows_rimanenti\n{doc_rows_rimanenti}", DEBUG_LVL)

            stringa_unica_con_cr = "\n".join(lista)
            try:
                pattern = current_pattern
                log_pbst(self,f"current_pattern : {current_pattern}", DEBUG_LVL)
                matches = re.finditer(pattern, stringa_unica_con_cr)
                group_matched = ""
                for matchNum, match in enumerate(matches, start=1):
                    msg_match = "Match {matchNum} was found at {start}-{end}: \n{match}"\
                          .format(matchNum=matchNum,
                                  start=match.start(),
                                  end=match.end(),
                                  match=match.group())
                    log_pbst(self,msg_match, DEBUG_LVL)
                    group_matched = match.group()

                msg_err = current_msg_err
                self.assertTrue(group_matched is not None, msg_err)

                if group_matched.count("*") > 0 or group_matched.count("+") > 0:
                    istruzioni_da_eseguire_insieme += "_ = "
                    istruzioni_da_eseguire_insieme += f"{group_matched}"
                    if group_matched.count("*") > 0:
                        tassa_da_calcolare = True
                    elif group_matched.count("+") > 0:
                        costo_da_calcolare = True
                    log_pbst(self,f"istruzioni_da eseguire_insieme: \n{istruzioni_da_eseguire_insieme}",DEBUG_LVL)
                elif group_matched.count("=") > 0:
                    istruzioni_da_eseguire_insieme += f"{group_matched}"
                    log_pbst(self,f"istruzioni_da eseguire_insieme: \n{istruzioni_da_eseguire_insieme}",DEBUG_LVL)
                elif group_matched.startswith("Out[") :
                    if out_tassa_rilevata is None:
                      out_tassa_rilevata = re.match(r"Out\[\d+]: (\d{1}\.\d{1,3})",group_matched).group(1)
                      log_pbst(self,f"tassa_rilevata = {out_tassa_rilevata}",INFO_LVL)
                    elif out_costo_rilevato is None:
                        out_costo_rilevato = re.match(r"Out\[\d+]: (\d{3}\.\d{1,3})",group_matched).group(1)
                        log_pbst(self,f"costo_rilevato = {out_costo_rilevato}",INFO_LVL)
                try:
                    namespace = globals()
                    exec(compile(istruzioni_da_eseguire_insieme, file_name_to_compile, mode='exec'),
                         namespace
                         )
                    if tassa_da_calcolare:
                        tassa_da_calcolare = False
                        exec_tassa_calcolata = _
                        log_pbst(self,f"tassa_calcolata = {exec_tassa_calcolata}",INFO_LVL)
                    elif costo_da_calcolare:
                        costo_da_calcolare = False
                        exec_costo_calcolato = _
                        log_pbst(self,f"costo_calcolato = {exec_costo_calcolato}",INFO_LVL)
                except AssertionError as ae:
                    log_pbst(self, ae,DEBUG_LVL)
                except Exception as e:
                    log_pbst(self, exc, DEBUG_LVL)

            except AssertionError as ae:
                log_pbst(self, ae,DEBUG_LVL)
            except Exception as exc:
                log_pbst(self, exc, DEBUG_LVL)
        try:
            namespace = globals()
            log_pbst(self,f"istruzioni da eseguire insieme: \n{istruzioni_da_eseguire_insieme}",DEBUG_LVL)
            single_line = compact_in_single_line(istruzioni_da_eseguire_insieme)
            log_pbst(self,f"compattate in unica linea: \n{single_line}",DEBUG_LVL)
            exec(compile(single_line, file_name_to_compile, mode='exec'),
                 namespace
                 )
            msg_err = f"Valore tassa calcolata '{exec_tassa_calcolata}' differisce da quella rilevata '{out_tassa_rilevata}'"
            self.assertTrue(out_tassa_rilevata == str(exec_tassa_calcolata), msg_err)
            msg_err = f"Valore costo calcolato '{exec_costo_calcolato}' differisce da quello rilevato {out_costo_rilevato}"
            self.assertTrue(out_costo_rilevato == str(exec_costo_calcolato), msg_err)

            superati_gli_assert = True
        except AssertionError as ae:
            log_pbst(self, ae,DEBUG_LVL)
        except Exception as exc:
            log_pbst(self, exc, DEBUG_LVL)

        finally:
            if superati_gli_assert or doc_rows == doc_rows_rimanenti:  # trovato o finita lista
                pass
            elif not superati_gli_assert and doc_rows != doc_rows_rimanenti:  # continuare
                doc_rows = doc_rows_rimanenti
            elif not superati_gli_assert and doc_rows == doc_rows_rimanenti:  # non superato e finita lista
                pass
            else:
                self.assertTrue(False, "errore imprevisto in " + self._testMethodName)

        self.assertTrue(superati_gli_assert, msg_err)
        log_pbst(self,"ended successfully.\n")
