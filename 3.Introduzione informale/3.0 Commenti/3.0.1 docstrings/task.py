def output_console():
    """
PyDev console: using IPython 9.5.0
PYCHARM_PROJECT_ID=724bbcf
PYCHARM_UUID=9f3211ff-fba3-346b-bcaf-80207cc36bb1
PBST_CONSOLE_ID=0be5871e88718ed1
PBST_UUID=019063ca-bf28-5403-8408-ee99228c1961
USERNAME=rober
USERDOMAIN=DESKTOP-1UMSUP8
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
# autore Roberto Lupo
888 # numero preferito
Out[3]: 888
'rossonero' # colore preferito
Out[4]: 'rossonero'

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
