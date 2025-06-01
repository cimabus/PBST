def output_console():
    """
  C:\\Users\\lupoji\\PythonBaseStandardTutorial-v0.4.2\\.venv\\Scripts\\python.exe "C:/Program Files/JetBrains/PyCharm 2025.1/plugins/python-ce/helpers/pydev/pydevconsole.py" --mode=client --host=127.0.0.1 --port=60485
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\lupoji\\PythonBaseStandardTutorial-v0.4'])
PyDev console: starting.
Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
# autore : roberto lupo
888 # numero preferito
888
'rossonero' # colore preferito
'rossonero'

"""
    pass

doc_output_console = output_console.__doc__ # questa istruzione imposta nella variabile
                                            # il valore dell'attributo __doc__
                                            # della funzione 'outputConsole'
                                            # che corrisponde al contenuto della 'docstring'
print(doc_output_console)  # stampa il valore della variabile sullo console

