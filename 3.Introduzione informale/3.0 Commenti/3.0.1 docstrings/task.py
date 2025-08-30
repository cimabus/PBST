def output_console():
    """
    Questo è un commento particolare che si chiama 'docstring'
    e descrive il funzionamento della funzione 'output_console'
    che ha una unica istruzione 'pass' che non esegue nulla.

    Esegui nella console le istruzioni indicate nella descrizione del
    task, inserisci qui l'output della console e configura l'esecuzione
    'Current File' con '3.0.1 docstrings' prima di eseguire il task.
    """
    pass


# questa istruzione imposta nella variabile il valore dell'attributo __doc__
# della funzione 'output_console' che corrisponde al contenuto della 'docstring'
doc_output_console = output_console.__doc__
print(doc_output_console)

# dal modulo importa solo la funzione e quelle a lei collegate
from pbst_console import check

# check di validità della console PBST
check(doc_output_console)
