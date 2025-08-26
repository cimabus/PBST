def output_console():
    """
import pbst_console as pc
pc.start()
PyDev console: using IPython 9.4.0
PYCHARM_PROJECT_ID=724bbcf
PYCHARM_UUID=f7f1b8d3-374b-3f5e-bb22-00d921d7213f
PBST_CONSOLE_ID=0be5871e88718ed1
PBST_UUID=8074ecac-7796-5e04-b0ce-03250e0751f3
USERNAME=rober
USERDOMAIN=DESKTOP-1UMSUP8
Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
3+4
Out[2]: 7
a=4
b=6
a*b
Out[5]: 24

"""
    pass
doc_output_console = output_console.__doc__ # questa istruzione imposta nella variabile
                                            # il valore dell'attributo __doc__
                                            # della funzione 'outputConsole'
                                            # che corrisponde al contenuto della 'docstring'
print(doc_output_console)  # stampa il valore della variabile sullo console
import pbst_console as pc
pc.check(doc_output_console) # check sulle variabili di ambiente
