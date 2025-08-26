def output_console():
    """

PyDev console: using IPython 9.4.0
PYCHARM_PROJECT_ID=724bbcf
PYCHARM_UUID=5c50fe76-07c4-3629-8aa8-444bec70c20f
PBST_CONSOLE_ID=0be5871e88718ed1
PBST_UUID=dc28efe5-ab9f-5d5b-8d03-fd1b7901b1e6
USERNAME=rober
USERDOMAIN=DESKTOP-1UMSUP8
Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
a=2
b=3
a*b
Out[4]: 6


"""
    pass
doc_output_console = output_console.__doc__ # questa istruzione imposta nella variabile
                                            # il valore dell'attributo __doc__
                                            # della funzione 'outputConsole'
                                            # che corrisponde al contenuto della 'docstring'
print(doc_output_console)  # stampa il valore della variabile sullo console
import pbst_console as pc
pc.check(doc_output_console) # check sulle variabili di ambiente
