## NON ELIMINARE
# serve per aggiungere alla sys.path la directory del file task.py
# deve essere invocata dal file test_task.py
import sys , os
def ottieni_directory_padre_padre(percorso):
    """
    Questa funzione prende un percorso di file come argomento e restituisce
     la directory padre_padre ../../
    :param percorso: Il percorso del file
    :return: La directory padre_padre del file
    """
    return os.path.dirname(os.path.dirname(percorso))

sys.path.append(os.path.abspath(ottieni_directory_padre_padre(__file__)))
