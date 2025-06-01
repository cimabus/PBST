def outputConsole():
    """
        Questo è un commento particolare che si chiama 'docstring'
    e descrive il funzionamento del programma chiamato 'outputConsole'
    che in particolare ha una unica istruzione 'pass' che non esegue nulla.
    Inserisci qui l'intero output della console escludendo la prima riga!
    Attenzione:
    Per eseguire nella console è possibile eseguire il comando
    `Run File in Python Console' nel menù contestuale dell'editor clicca il bottone destro del mouse

# SVOLGIMENTO: inserire l'output della console ad ognuno dei seguenti prompt
# autore:inserisci il tuo nome

rl1.1>>>'Questa "parola" è tra doppi apici, quest\'altra \'parola\' invece è tra apici singoli'
rl1.1'Questa "parola" è tra doppi apici, quest\'altra \'parola\' invece è tra apici singoli'

rl1.2>>>"Questa 'parola' è tra apici, quest'altra \"parola\" invece è tra apici doppi"
rl1.2'Questa \'parola\' è tra apici, quest\'altra "parola" invece è tra apici doppi'

rl1.3>>>" Mi 'piaace' così e \"anche\" così"
rl1.3' Mi \'piaace\' così e "anche" così'

rl1.4>>>''' questa 'prevede' anche gli "apici" \'''tripli non usati\''' però nella docstring'''
rl1.4' questa \'prevede\' anche gli "apici" \'\'\'tripli non usati\'\'\' però nella docstring'

rl2.1>>>a = 'stringa che precede il newline\nstringa che succede al newline'
print(a)
rl2.1stringa che precede il newlinestringa che succede al newline

rl2.2>>>a
rl2.2'stringa che precede il newline\qstringa che succede al newline'

rl2.3>>>print('C:\\Users\name') # inserire nell'output solo l'ultima riga della risposta
rl2.3SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \\UXXXXXXXX escape

rl2.4>>>print(r'C:\AppData\Roaming')
rl2.4C:\AppData\Roaming

rl2.5>>>print('C:\\\\Users\name')
rl2.5C:\\Users
ame

rl2.6>>>print('C:\\\\Users\\name')
rl2.6C:\\Users\name

rl2.7>>># SVOLGIMENTO: stringhe su più righe 'as is written' con apici tripli '''
    """
    pass


outputConsole.__doc__  # questa scrittura invoca la variabile, detta anche proprietà, '__doc__' dell'oggetto 'outputConsole' che viene impostata al suo 'docstring'
outputConsole()  # questa scrittura invoca la funzione outputConsole che presenta l'istruzione di impostzione della propria 'docstring' '__doc__' e la 'pass' che non fa nulla
