def output_console():
    """
PyDev console: using IPython 9.5.0
PBST_CONSOLE_ID_v2=0be5871e88718ed1
USERNAME=rober
USERDOMAIN=DESKTOP-1UMSUP8
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
1+2* 3-4
Out[2]: 3
3* +5 * -2 - +5
Out[3]: -35
-7 + * -5
  Cell In[4], line 1
    -7 + * -5
         ^
SyntaxError: invalid syntax
3*4/5
Out[5]: 2.4
18 / 5 # Scegli due numeri e dividili in modo da avere un resto
Out[6]: 3.6
18 // 5 # Scegli due numeri e dividili troncando il resto e avere un intero
Out[7]: 3
_ + 18 % 5 # aggiungi il resto 18 % 5 al risultato appena stampato e referenziato da '_'
Out[8]: 6
b = 16 # base
h = 5 + 2 # altezza
b * h # base x altezza
Out[10]: 112
literal_corretto_ma_non_ancora_utilizzato
Traceback (most recent call last):
NameError: name 'literal_corretto_ma_non_ancora_utilizzato' is not defined
iva = 8.5 / 100 # percentuale tassa
prezzo = 100 # prezzo
prezzo * iva # tassa
Out[13]: 8.5
prezzo + _ # prezzo + tassa, ultimo valore stampato in output
Out[14]: 108.5

   """
# questa istruzione imposta nella variabile il valore dell'attributo __doc__
#  della funzione 'output_console' che corrisponde al contenuto della 'docstring'
doc_output_console = output_console.__doc__
print(doc_output_console)

# dal modulo importa solo la funzione e quelle a lei collegate
from pbst_console import check

# check di validità della console PBST
check(doc_output_console)
