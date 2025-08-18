# NON ELIMINARE import __init__
# il riferimento a outputConsole verrà risolto dinamicamente dalla import __init__
# se si esegue test_task.py con l'interprete
import __init__
import sys, os
import unittest
from typing import AnyStr

# il riferimento a outputConsole verrà risolto dinamicamente dalla except
# se eseguito dal check, cioè dall'unittest
try:
    from rePatterns import EXP_CON_PARENTESI as EXP_CON_PARENTESI
except ImportError as ie:
    print('file:',__file__,'dirpath:',os.path.abspath(os.path.dirname(os.path.dirname(__file__))),sep="\n",end="\n\n")
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
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

from task import output_console as outputConsole
import sys
import re


# suddivide in righe la stringa multilinea
#outputConsole.replace('/', '\\') # rimpiazza ogni slash '/' con backslash '\'
def get_doc_rows():
    return str(outputConsole.__doc__).split('\n')


def catch_rows_from_eye(rows, eye, all_rows=False):
    """
 elimina intestazione dalle righe fino a quella che inizia con eye,
 riga precedente e quella con eye non sono eliminate

    :param rows: stringa multilinea
    :param eye: start linea
                se 'Python 3.' skip questa e restituisce tutte le altre
                se 'Out[' inserisce la precedente ( istruzione ) e questa che è l'output
    :param all_rows: True comprende anche le successive, default False
    :return:
    """
    new_list = []
    for i, riga in enumerate(rows):
        # Se la riga inizia con eye, aggiungiamo la riga precedente alla nuova lista
        # e se All_rows is True aggiungo le righe successive a eye
        if new_list.__len__() >= 0 and all_rows is True:
            if rows[i] != eye:
                new_list.append(rows[i])
        elif new_list.__len__() == 0 and eye == 'Python 3.' and all_rows is True:
            new_list.append(rows[i])
        elif riga.startswith(eye) and new_list.__len__() == 0 and eye == 'Python 3.':
            all_rows = True  # al primo elemento da inserire se 'Python 3.' imposto di scrivere tutte le successive
        elif riga.startswith(eye) and new_list.__len__() == 0 and eye == 'Out[':
            new_list.append(
                rows[i - 1])  # al primo elemento da inserire se 'Out[' appendo la riga precedente ( istruzione )
            new_list.append(rows[i])  # e questa ( output generato )
        else:
            pass

    return new_list


def catch_rex_row(row,
                  regex,
                  match_group_alone=True,
                  match_group_num=1,
                  pos=1
                  ):
    group_matched = None
    group_num_matched = None

    print("row:", row)
    matches = re.finditer(regex, row)
    for matchNum, match in enumerate(matches, start=pos):
        print("Match {matchNum} was found at {start}-{end}: {match}"
              .format(matchNum=matchNum,
                      start=match.start(),
                      end=match.end(),
                      match=match.group()))
        group_matched = match.group()
        if match_group_alone:
            break
        for group_num in range(0, len(match.groups())):
            group_num = group_num + 1
            print("Group {groupNum} found at {start}-{end}: {group}"
                  .format(groupNum=group_num,
                          start=match.start(group_num),
                          end=match.end(group_num),
                          group=match.group(group_num)))
            if match_group_num == group_num:
                group_num_matched = match.group(group_num)
            break
    return group_matched, row, group_num_matched


def catch_rex(lista,
              regex,
              match_group_alone=True,
              on_match_return_next_row=False,
              on_match_return_group=False,
              match_group_num=1,
              pos=1
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
        group_matched, return_row, return_group = catch_rex_row(row,
                                                                regex,
                                                                match_group_alone,
                                                                match_group_num,
                                                                pos)

        if group_matched is not None:
            matching_done = True
    return group_matched, return_row if on_match_return_next_row else None, return_group if on_match_return_group else None


# globals
_ = None
_: int | float
istruzioni_da_eseguire_insieme: str = ""


class TestCase(unittest.TestCase):
    def test_05_parentesi_non_consentite(self):
        print(end=f"\n{self._testMethodName}\n")
        doc_rows = get_doc_rows()
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            print('doc_rows :', doc_rows, 'doc_rows_rimanenti :', doc_rows_rimanenti, sep="\n")
            try:
                pattern = EXP_CON_PARENTESI  # verifico che non ci siano parentesi
                msg_err = "parentesi non ammesse nelle espressioni aritmetiche"
                espressione, no_value, no_value = catch_rex(lista, pattern)
                self.assertTrue(espressione is not None, msg_err)
            except AssertionError as ae:
                print(ae)
            except Exception as e:
                msg_err = f"{e}"
            finally:
                if doc_rows == doc_rows_rimanenti:
                    superati_gli_assert = True
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)

    def test_10_espressione_con_naturali(self):
        global _
        print(end=f"{self._testMethodName}\n\n")
        doc_rows = get_doc_rows()
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            print('doc_rows :', doc_rows, 'doc_rows_rimanenti :', doc_rows_rimanenti, sep="\n")
            try:
                pattern = EXP_SOLO_NATURALI  # verifico che ci sia un'espressione con naturali senza divisioni
                msg_err = "espressione aritmetica con numeri naturali senza divisioni non trovata"
                espressione_naturale, row, no_value = catch_rex(lista, pattern, on_match_return_next_row=True)
                self.assertTrue(espressione_naturale is not None, msg_err)
                risultato = eval(espressione_naturale)
                msg_err = "risultato espressione aritmetica con naturali con risultato non intero"
                self.assertTrue(type(risultato) == type(1234567890), msg_err)
                pattern = EXP_RIS_INT
                matched_da_console, no_row, risultato_da_console = catch_rex_row(row,
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
                print(ae)
            except Exception as e:
                msg_err = f"{e}"
            finally:
                if doc_rows == doc_rows_rimanenti:
                    break;
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)

    def test_20_espressione_con_interi(self):
        global _
        print(end=f"{self._testMethodName}\n\n")
        doc_rows = get_doc_rows()
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            print('doc_rows :', doc_rows, 'doc_rows_rimanenti :', doc_rows_rimanenti, sep="\n")
            try:
                pattern = EXP_SOLO_NATURALI  # verifico che ci sia un'espressione con naturali
                msg_err = "espressione aritmetica con solo numeri naturali, invece che anche con interi, presente"
                espressione_con_naturali, row, no_value = catch_rex(lista, pattern, on_match_return_next_row=True)
                self.assertTrue(espressione_con_naturali is None, msg_err)

                pattern = EXP_SENZA_DIV  # verifico che ci sia un'espressione anche con divisioni
                msg_err = "espressione aritmetica con numeri interi e senza divisioni non presente"
                espressione_con_interi, row, no_value = catch_rex(lista, pattern, on_match_return_next_row=True)
                self.assertTrue(espressione_con_interi is not None, msg_err)
                risultato = eval(espressione_con_interi)
                msg_err = "risultato calcolato non intero dell'espressione aritmetica"
                self.assertTrue(type(risultato) == type(1234567890), msg_err)
                pattern = EXP_RIS_INT
                matched_out, no_row, risultato_da_console = catch_rex_row(row, pattern, match_group_alone=False)
                msg_err = f"risultato valutato '{risultato}' dell'espressione aritmetica con interi '{espressione_con_interi}'" + \
                          f" non coincide col risultato '{risultato_da_console}' indicato in console"
                self.assertTrue(int(risultato_da_console) == risultato, msg_err)
                _ = risultato
                superati_gli_assert = True
            except AssertionError as ae:
                print(ae)
            except Exception as e:
                msg_err = f"{e}"
            finally:
                if doc_rows == doc_rows_rimanenti:
                    break
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)

    def test_30_espressione_con_risultato_float(self):
        global _
        print(end=f"\n{self._testMethodName}\n")
        doc_rows = get_doc_rows()
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            print('doc_rows :', doc_rows, 'doc_rows_rimanenti :', doc_rows_rimanenti, sep="\n")
            try:
                pattern = EXP_CON_DIV  # verifico che ci sia un'espressione anche con divisioni
                msg_err = "espressione aritmetica con divisioni tra numeri interi, e quindi risultato float, non presente "
                espressione_float, row, no_value = catch_rex(lista,
                                                             pattern,
                                                             on_match_return_next_row=True)
                self.assertTrue(espressione_float is not None, msg_err)
                risultato = eval(espressione_float)
                msg_err = "risultato non float dell'espressione aritmetica"
                self.assertTrue(type(risultato) == type(0.123456789), msg_err)
                pattern = EXP_RIS_FLOAT
                matched_group, matched_group_num, risultato_da_console = catch_rex_row(row,
                                                                                       pattern,
                                                                                       match_group_alone=False)
                msg_err = f"risultato valutato '{risultato}' dell'espressione aritmetica con interi '{espressione_float}' \
                                non coincide col risultato '{risultato_da_console}' indicato in console"
                self.assertTrue(float(risultato_da_console) == risultato, msg_err)
                _ = risultato
                superati_gli_assert = True
            except AssertionError as ae:
                print(ae)
            except Exception as e:
                msg_err = f"{e}"
            finally:
                if doc_rows == doc_rows_rimanenti:
                    break
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)

    def test_40_divisione_troncata(self):
        global _
        print(end=f"\n{self._testMethodName}\n")
        doc_rows = get_doc_rows()
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            print('doc_rows :', doc_rows, 'doc_rows_rimanenti :', doc_rows_rimanenti, sep="\n")
            try:
                pattern = EXP_CON_DIV_TRONCATA  # verifico che ci sia un'espressione anche con divisione troncata
                msg_err = "espressione aritmetica con divisione troncata non presente"
                espressione_intero, row, no_value = catch_rex(lista,
                                                              pattern,
                                                              on_match_return_next_row=True)
                self.assertTrue(espressione_intero is not None, msg_err)
                risultato_intero = eval(espressione_intero)
                msg_err = "calcolato risultato non intero dell'espressione aritmetica tra interi con divisione troncata"
                self.assertTrue(type(risultato_intero) == type(123456789), msg_err)
                pattern = EXP_RIS_INT
                matched_group, no_value, risultato_da_console = catch_rex_row(row,
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
                print(ae)
            except Exception as e:
                msg_err = f"{e}"
            finally:
                if doc_rows == doc_rows_rimanenti:
                    break
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)

    def test_50_underscore_con_divisione_in_modulo(self):
        global _, istruzioni_da_eseguire_insieme
        istruzioni_da_eseguire_insieme = ""
        print(end=f"\n{self._testMethodName}\n")
        print("istruzioni da eseguire", istruzioni_da_eseguire_insieme, "underscore =", _, sep="\n")
        doc_rows = get_doc_rows()
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Out['
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            print('doc_rows :', doc_rows, 'doc_rows_rimanenti :', doc_rows_rimanenti, sep="\n")
            try:
                pattern = EXP_UND_CON_DIV_IN_MOD  # verifico che ci sia un'espressione anche con divisioni
                msg_err = "espressione aritmetica con underscore e divisione in modulo non presente"
                espressione_underscore, row, matched_group_num = catch_rex(lista,
                                                                           pattern,
                                                                           on_match_return_next_row=True)
                self.assertTrue(espressione_underscore is not None, msg_err)
                globs = globals()
                istruzioni_da_eseguire_insieme += "_ = "
                istruzioni_da_eseguire_insieme += espressione_underscore
                exec(compile(istruzioni_da_eseguire_insieme, 'nul', mode='exec'), globs)
                msg_err = f"risultato '{_}' non intero dell'espressione aritmetica con divisione in modulo, underscore '{_}'"
                self.assertTrue(type(_) == type(123456789), msg_err)
                pattern = EXP_RIS_INT
                matched_group, no_value, risultato_da_console = catch_rex_row(row, pattern, match_group_alone=False)
                msg_err = f"risultato valutato '{_}' dell'espressione aritmetica '{espressione_underscore}'" + \
                          f"non coincide col risultato '{risultato_da_console}' indicato in console"
                self.assertTrue(int(risultato_da_console) == _, msg_err)
                superati_gli_assert = True
            except AssertionError as ae:
                print(ae)
            except Exception as e:
                msg_err = f"{e}"
                print(msg_err)
            finally:
                if doc_rows == doc_rows_rimanenti:
                    break
                else:
                    doc_rows = doc_rows_rimanenti
        self.assertTrue(superati_gli_assert, msg_err)
        _ = None
        istruzioni_da_eseguire_insieme = ""

    def test_60_assegnamento_intero(self):
        global istruzioni_da_eseguire_insieme
        print(end=f"\n{self._testMethodName}\n")
        doc_rows = get_doc_rows()
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Python 3.'
        file_name_to_compile = os.devnull
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            print('doc_rows :', doc_rows, 'doc_rows_rimanenti :', doc_rows_rimanenti, sep="\n")
            try:
                pattern = EXP_ASS_INT  # verifico che ci sia un'espressione con assegnamento intero
                msg_err = "assegnamento intero non presente"
                assegnamento_intero, no_row, espressione_numerica = catch_rex(lista, pattern)
                self.assertTrue(assegnamento_intero is not None, msg_err)
                exec(compile(assegnamento_intero, file_name_to_compile, mode='exec'))
                istruzioni_da_eseguire_insieme += f"{assegnamento_intero};"
                superati_gli_assert = True
            except AssertionError:
                pass
            except Exception as e:
                msg_err = f"{e}"
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

    def test_70_assegnamento_espressione_intera(self):
        global istruzioni_da_eseguire_insieme
        print(end=f"\n{self._testMethodName}\n")
        print(f"istruzioni_da_eseguire_insieme: {istruzioni_da_eseguire_insieme}")
        doc_rows = get_doc_rows()
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Python 3.'
        file_name_to_compile = os.devnull
        all_rows = False
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find, all_rows=all_rows)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            print('doc_rows :', doc_rows, 'doc_rows_rimanenti :', doc_rows_rimanenti, sep="\n")
            try:
                pattern = EXP_ASS_EXP_INT  # verifico che ci sia un'espressione con assegnamento intero
                assegnamento_esp_intera, no_row, espressione_numerica = catch_rex(lista, pattern,
                                                                                  on_match_return_group=True,
                                                                                  match_group_alone=False,
                                                                                  match_group_num=1
                                                                                  )
                msg_err = "assegnamento espressione intera non presente"
                self.assertTrue(assegnamento_esp_intera is not None, msg_err)
                msg_err = "assegnamento espressione intera non presenta l'espressione numerica"
                self.assertTrue(espressione_numerica is not None, msg_err)
                msg_err = "assegnamento espressione intera non presenta un'espressione ma un numero"
                if espressione_numerica.strip().isdigit():
                    doc_rows_rimanenti = lista
                    eye_to_find = assegnamento_esp_intera
                    all_rows = True
                    continue  # proviamo se esiste un'altra riga esclusa quella matched
                globs = globals()
                exec(compile(assegnamento_esp_intera, file_name_to_compile, mode='single'), globs)
                superati_gli_assert = True
                istruzioni_da_eseguire_insieme += f"{assegnamento_esp_intera};"
            except AssertionError as ae:
                print(ae)
            except Exception as e:
                print(f"{e}")
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

    def test_80_espressione_con_variabili(self):
        global istruzioni_da_eseguire_insieme
        global _
        print(end=f"\n{self._testMethodName}\n")
        print('istruzioni_da_eseguire_insieme: ', istruzioni_da_eseguire_insieme)
        print('_: ', _)
        doc_rows = get_doc_rows()
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Python 3.'
        #eye_to_find = 'Out['
        file_name_to_compile = os.devnull
        all_rows = False
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find, all_rows=all_rows)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            print('doc_rows :', doc_rows, 'doc_rows_rimanenti :', doc_rows_rimanenti, sep="\n")
            try:
                pattern = EXP_CON_VARIABILI  # verifico che ci sia un'espressione con variabili
                espressione_con_variabili, row, no_return_group = catch_rex(lista, pattern,
                                                                            on_match_return_next_row=True
                                                                            )
                msg_err = "espressione con variabili non presente"
                self.assertTrue(espressione_con_variabili is not None, msg_err)
                istruzioni_da_eseguire_insieme += f"_ = {espressione_con_variabili}"

                namespace = globals()
                exec(compile(istruzioni_da_eseguire_insieme, file_name_to_compile, mode='exec'),
                     namespace
                     )

                print("istruzioni_da eseguire_insieme: ", istruzioni_da_eseguire_insieme)
                print('_ =', _)
                pattern = EXP_RIS_INT  # verifico il risultato prelevato
                lista = []
                lista.append(row)
                matched, no_row, risultato_prelevato = catch_rex(lista,
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
                print(ae)
            except Exception as e:
                print(f"{e}")
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

    def test_90_Traceback_NameError(self):
        print(end=f"\n{self._testMethodName}\n")
        doc_rows = get_doc_rows()
        superati_gli_assert = False
        msg_err = None
        eye_to_find = 'Python 3.'
        all_rows = False
        while not superati_gli_assert:
            lista = catch_rows_from_eye(doc_rows, eye_to_find, all_rows=all_rows)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            print('doc_rows :', doc_rows, 'doc_rows_rimanenti :', doc_rows_rimanenti, sep="\n")
            try:
                pattern = EXP_TRACEBACK_NAME_ERROR  # verifico che ci sia un'espressione che restituisce errore
                stringa_unica_con_cr = "\n".join(lista)
                matches = re.finditer(pattern, stringa_unica_con_cr)
                group_matched = None
                for matchNum, match in enumerate(matches, start=1):
                    print("Match {matchNum} was found at {start}-{end}: {match}"
                          .format(matchNum=matchNum,
                                  start=match.start(),
                                  end=match.end(),
                                  match=match.group()))
                    group_matched = match.group()

                msg_err = "Traceback per NameError non presente"
                self.assertTrue(group_matched is not None, msg_err)

                superati_gli_assert = True
            except AssertionError as ae:
                print(ae)
            except Exception as e:
                print(f"{type(e)}: {e}")
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

    def test_100_calcola_iva(self):
        global istruzioni_da_eseguire_insieme \
            , _ \
            , _ #  last espressione valutata
        print(end=f"\n{self._testMethodName}\n")
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
            get_first_match = True
            doc_rows = get_doc_rows()
            superati_gli_assert = False
            msg_err = None
            eye_to_find = 'Python 3.'
            all_rows = True
            lista = catch_rows_from_eye(doc_rows, eye_to_find, all_rows=all_rows)
            doc_rows_rimanenti = [elemento for elemento in doc_rows if elemento not in lista]
            stringa_unica_con_cr = "\n".join(lista)
            try:
                pattern = current_pattern
                print("current_pattern :", current_pattern)
                matches = re.finditer(pattern, stringa_unica_con_cr)
                group_matched = ""
                for matchNum, match in enumerate(matches, start=1):
                    print("Match {matchNum} was found at {start}-{end}: {match}"
                          .format(matchNum=matchNum,
                                  start=match.start(),
                                  end=match.end(),
                                  match=match.group()))

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
                    print("istruzioni_da eseguire_insieme: \n", istruzioni_da_eseguire_insieme, sep="")
                elif group_matched.count("=") > 0:
                    istruzioni_da_eseguire_insieme += f"{group_matched}"
                    print("istruzioni_da eseguire_insieme: \n", istruzioni_da_eseguire_insieme, sep="")
                elif group_matched.startswith("Out[") :
                    if out_tassa_rilevata is None:
                      out_tassa_rilevata = re.match(r"Out\[\d+]: (\d{1}\.\d{1,3})",group_matched).group(1)
                      print('tassa_rilevata =',out_tassa_rilevata)
                    elif out_costo_rilevato is None:
                        out_costo_rilevato = re.match(r"Out\[\d+]: (\d{3}\.\d{1,3})",group_matched).group(1)
                        print('costo_rilevato =', out_costo_rilevato,flush=True)
                try:
                    namespace = globals()
                    exec(compile(istruzioni_da_eseguire_insieme, file_name_to_compile, mode='exec'),
                         namespace
                         )
                    if tassa_da_calcolare:
                        tassa_da_calcolare = False
                        exec_tassa_calcolata = _
                        print('tassa_calcolata =',exec_tassa_calcolata)
                    elif costo_da_calcolare:
                        costo_da_calcolare = False
                        exec_costo_calcolato = _
                        print('costo_calcolato =', exec_costo_calcolato)
                except AssertionError as ae:
                    print(ae)
                except Exception as e:
                    print(f"{type(e)}: {e}")

            except AssertionError as ae:
                print(ae)
            except Exception as e:
                print(f"{type(e)}: {e}")
        try:
            namespace = globals()
            exec(compile(istruzioni_da_eseguire_insieme, file_name_to_compile, mode='exec'),
                 namespace
                 )
            msg_err = f"Valore tassa calcolata '{exec_tassa_calcolata}' differisce da quella rilevata '{out_tassa_rilevata}'"
            self.assertTrue(out_tassa_rilevata == str(exec_tassa_calcolata), msg_err)
            msg_err = f"Valore costo calcolato '{exec_costo_calcolato}' differisce da quello rilevato {out_costo_rilevato}"
            self.assertTrue(out_costo_rilevato == str(exec_costo_calcolato), msg_err)

            superati_gli_assert = True
        except AssertionError as ae:
            print(ae)
        except Exception as e:
            print(f"{type(e)}: {e}")

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
