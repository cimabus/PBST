def output_console():
    """
  Questo è un commento particolare che si chiama 'docstring'
  e descrive il funzionamento della funzione 'output_console'
  che ha una unica istruzione 'pass' che non esegue nulla.

  Esegui nella console le istruzioni indicate nella descrizione del
  task, inserisci qui l'output della console e configura l'esecuzione
  'Current File' con '3.1.1 Numeri' prima di eseguire il task.

# SVOLGIMENTO: inserire l'output della console a ognuno dei seguenti prompt
# DA COMPLETARE: inserire il nome e cognome

rl1.1>>>'Questa "parola" è tra doppi apici, quest\'altra \'parola\' invece è tra apici singoli'
rl1.1DA COMPLETARE lasciando il tag rl1.1 a inizio riga

rl1.2>>>"Questa 'parola' è tra apici, quest'altra \"parola\" invece è tra apici doppi"
rl1.2DA COMPLETARE lasciando il tag rl1.2 a inizio riga

rl1.3>>>" Mi 'piaace' così e \"anche\" così"
rl1.3DA COMPLETARE lasciando il tag rl1.3 a inizio riga

rl1.4>>>''' questa 'prevede' anche gli "apici" \'''tripli non usati\''' però nella docstring'''
rl1.4DA COMPLETARE lasciando il tag rl1.4 a inizio riga

rl2.1>>>a = 'stringa che precede il newline\nstringa che succede al newline'; print(a)
rl2.1DA COMPLETARE lasciando il tag rl2.1 a inizio riga

rl2.2>>>a
rl2.2DA COMPLETARE lasciando il tag rl2.2 a inizio riga

rl2.3>>>print('C:\\Users\name') # inserire nell'output solo l'ultima riga della risposta
rl2.3DA COMPLETARE lasciando il tag rl2.3 a inizio riga

rl2.4>>>print(r'C:\app\fuel')
rl2.4DA COMPLETARE lasciando il tag rl2.4 a inizio riga

rl2.5>>>print('C:\\\\Users\name')
rl2.5DA COMPLETARE lasciando il tag rl2.5 a inizio riga

rl2.6>>>print('C:\\\\Users\\name')
rl2.6DA COMPLETARE lasciando il tag rl2.6 a inizio riga

rl2.7>>># SVOLGIMENTO: stringhe su più righe 'as is written' con apici tripli '''
rl2.7DA COMPLETARE lasciando il tag rl2.7 a inizio riga
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