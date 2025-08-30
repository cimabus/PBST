def output_console():
    """
    Questo è un commento particolare che si chiama 'docstring'
    e descrive il funzionamento della funzione 'output_console'
    che ha una unica istruzione 'pass' che non esegue nulla.

    Eseguire nella console le istruzioni indicate nella descrizione del task,
    poi inserire qui l'output della console e configurare l'esecuzione
    'Current File' con '3.0.1 docstrings' prima di eseguire il task.
    """
    pass

doc_output_console = output_console.__doc__ # questa istruzione imposta nella variabile
                                            # il valore dell'attributo __doc__
                                            # della funzione 'output_console'
                                            # che corrisponde al contenuto della 'docstring'
print(doc_output_console)  # stampa il valore della variabile

import pbst_console as pc
pc.check(doc_output_console) # check di validità della console
