# NON ELIMINARE
# serve per aggiungere la directory del file task.py alla sys.path
# deve essere invocata, tramite import, nel file test_task.py
# il percorso è quello di questo file e la directory in append è quella della lezione
import sys, os


def ottieni_directory_padre_padre(percorso):
    """
    Questa funzione prende un percorso di file come argomento e restituisce
     la directory padre_padre ../../
    :param percorso: Il percorso del file
    :return: La directory padre_padre del file
    """
    return os.path.dirname(os.path.dirname(percorso))


sys.path.append(os.path.abspath(ottieni_directory_padre_padre(__file__)))
