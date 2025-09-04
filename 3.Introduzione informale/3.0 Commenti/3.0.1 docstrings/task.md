<style> 
   .yel { color:yellow } 
   .gil { color:greenyellow } 
   .red { color:red }
   .cya { color:cyan }
   .whi { color:white }
   .gry {
      background-color: darkgrey; /* Colore dello sfondo */
      color: black; /* Colore del testo */
      display: inline; /* Assicurati che lo sfondo si adatti al testo */
      /* padding: 0 2px; /* Spazio intorno al testo (opzionale) */
    }
</style>

**Esempi di commenti e docstring**

Leggi <a href="https://pytutorial-it.readthedocs.io/it/python3.13/introduction.html">l'introduzione informale</a>
, poi <span class=yel>invoca l'interprete da console</span> da Tools -> <span class=gre>Python Debug Console</span> ( oppure View -> ToolWindows -> <span class=cya>Python Console</span> ) puoi impostare uno shortcut ( File -> Settings -> Keymap -> Tool Windows -> <span class=cya>Python console</span> ) e <span class=yel>esegui le istruzioni</span> seguenti:
1. <span class=yel> clicca </span>nell'area di output sul tooltip <span class=gry>Python Console</span> per visualizzare il messaggio di avvio della console interattiva <span class=gil>PyDev console: using IPython 9.5.0</span> insieme ad altre segnalazioni di ambiente;<span class=red> se console standard</span><span class=cya> prompt '>>>'</span> <span class=yel>cambiala selezionando </span><span class=cya>Use IPython </span>da File -> Settings -> Python -> Console -> General settings;
2. <span class=whi> scrivi </span>al prompt dell'interprete IPython <span class=gil>In [numero di riga del comando]</span> <span class=whi>una riga di commento </span><br>
   <span class=gil> In [2]: </span> <span class=whi># autore nome cognome</span>
3. un numero ed un commento sulla stessa riga <br> 
   <span class=gil> In [3]: </span> <span class=whi>314 # numero preferito </span>
4. una stringa (sequenza di caratteri racchiusa da apici singoli o doppi) e un commento sulla stessa riga<br>
   <span class=gil> In [4]: </span> <span class=whi>'rossonero' # colore preferito </span>
5. <span class=whi>copia l'output</span> della console nella <span class=yel>docstring</span> della funzione <span class=cya>output_console()</span>
   <span class=whi> posiziona il cursore nell'output della console e premi:</span> <br>
   <span class=gil>Ctrl-a</span> per selezionare <br> 
   <span class=gil>Ctrl-c</span> per copiare nella clipboard del sistema operativo
6. <span class=gil>in task.py</span> <span class=yel> esegui Ctrl-v </span>del testo nel placeholder, evidenziato, <br> 
   <span class=gre>selezionando tutto</span> in modo da sostituirlo interamente con l'output della console e <span class=yel>assicura la chiusura dei tre doppi apici <span class=gre>"""</span><span class=red> e togli le prime righe</span> fino a far rimanere <span class=gil>PyDev console: using IPython 9.4.0</span> come prima riga della selezione
7. <span class=gil>task.py</span>,in focus,cioè <span class=gil>visibile</span>, imposta <span class=yel>'Current File'</span> nel target di esecuzione, posizionato nel Menu Personalizzato <br> 
   ( <span class=yel>sulla sinistra</span> del <span class=gil>bottone run di esecuzione</span> ) ti sposti sull'icona <span class=yel>'più opzioni'</span> ( tre puntini verticali ) e dal menù a tendina scegli <span class=gre>'esecuzione con parametri'</span> e comparirà la frame di configurazione di esecuzione: <span class=red>modifica</span> al posto di 'task' il nome della directory padre <span class=red>'3.0.1 docstrings'</span>, <span class=gre>seleziona</span> la check box 'store as project file',<span class=gre>accetta</span> l'impostazione del path di default e <span class=gre>conferma</span> su 'done', e poi <span class=yel>applica le modifiche</span> cliccando su <span class=red>'apply'</span>: Così avrai impostato <span class=yel>il nome dell'esecuzione</span> nella console al <span class=gre>nome della configurazione</span>;
8. <span class=gil>esegui la configurazione '3.0.1 docstrings'</span>, che compare nella lista, cliccando sul bottone di <span class=gil>run</span>;
9. <span class=gil>modifica e ripeti 8.</span> fin quando il risultato non ti soddisfa <span class=gre>chiudi 'Python Console'</span>, cliccando su X, e riprova raddoppiando il carattere backslash del path dell'interprete <span class=red> se hai dimenticato di <span class=yel>eliminare il codice lasciando come prima riga <span class=gil>PyDev console: using IPython 9.4.0</span>
10. <span class=gil>registra il risultato </span>cliccando sull'icona della stampante dalla <span class=gre>vista </span><span class=cya>RUN ( Alt-4 )</span>, nelle impostazioni scegli il font per il <span class=yel>testo</span> e poi anche per <span class=yel>header e footer</span>, <span class=gil> source code pro 12 </span>,<br> <span class=gil>come header:</span> `Esecuzione $FILE$ di NOME COGNOME`,<br><span class=gil>come footer:</span> `Pagina $PAGE$ di $TOTALPAGES$ - Stampato il $DATE$ alle $TIME$`;<br> <span class=gre>seleziona </span> <span class=cya>Console Text, Landscape e Line Numbers</span>, imposta come stampante <span class=cya>Microsoft Print to pdf</span>, imposta come font per <span class=gil> header e footer</span>, <span class=cya>source code pro 12</span>, e in <span class=gil>Advanced</span> imposta <span class=cya>0.5 inches</span> come distanza dai bordi</span> esegui <span class=gil>Apply delle modifiche</span>, e salvi in una directory locale nominandolo <span class=yel>3.0.1.cognome_nome.pdf</span>. 

<div class=hint>
<p>
Per sapere come eseguire un task nella console vedere il video eseguendo lo script 
<span class=gil>ComeEseguireNellaConsole.py</span> presente nelle configurazioni, ma <span class=yel>>ci sono differenze rispetto al video</span>: <br>
    1. <span class=yel>console IPython</span> al posto della standard;<br>
    2. <span class=yel>riportare da 'PyDev console: using IPython 9.5.0'</span>, dal tooltip della scritta evidenziata 'Pyton Console', visualizzata nella console cliccandola</p>
<p>
Per <span class=yel>salvare l'output di un task come file .pdf</span> vedere il video eseguendo lo script 
<span class=gil>ComeSalvareOutputTaskInPdf.py</span> presente nelle configurazioni
</p>

<p> Esempio richiesto: <br>
<span class=gil>In [2]:</span> # autore nome e cognome  <br>
<span class=gil>In [3]:</span> <span class=cya>888 </span># numero preferito<br>
<span class=whi>Out[3]: 888</span><br>
<span class=gil>In [4]: "rosso-nero"</span> # colore preferito <br>
<span class=whi>Out[4]: 'rosso-nero'</span><br>
</p>
</div>
