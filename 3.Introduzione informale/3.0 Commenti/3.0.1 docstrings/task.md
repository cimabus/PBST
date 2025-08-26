<style> 
   .yel { color:yellow } 
   .gil { color:greenyellow } 
   .red { color:red }
</style>

**Esempi di commenti e docstring**

Leggi <a href="https://pytutorial-it.readthedocs.io/it/python3.13/introduction.html">qui</a>
l'introduzione informale, poi esegui le seguenti istruzioni.<br>
Invoca l'interprete (View|ToolWindows|PythonConsole) [puoi impostare uno shortcut andando su File|Settings|keymap](https://www.jetbrains.com/help/pycharm/2025.2/configuring-keyboard-and-mouse-shortcuts.html)
1. <span class=yel> Clicca nell'area di output sul marked Python Console dove comparirà </span> <span class=gil>PyDev console: using IPython 9.4.0</span> per far visualizzare il messaggio di avvio della console
2. e scrivi al prompt dell'interprete IPython <span class=gil>In[numero riga comando input]</span> una riga di commento <br>
   <span class=yel> es. In[2] # autore nome cognome
3. un numero ed un commento sulla stessa riga <br> 
   <span class=yel> es. In[3] 3.14 # numero preferito
4. una stringa (sequenza di caratteri racchiusa da apici singoli o doppi) ed un commento sulla stessa riga<br>
   <span class=yel> es. In[4] 'rossonero' # colore preferito
5. copia l'output della console 
   (posiziona il cursore nell'output della console e premi <br>
   <span class=yel> Ctrl-a per selezionare <br>
   Ctrl-c per copiare nella clipboard del sistema operativo)
6. vai in task.py ed <span class=yel> inserisci con Ctrl-v il testo nel placeholder, dalla superfice evidenziata, </span><br> 
   e selezionando tutto in modo da sostituirlo interamente con l'output della console e <br>
   <span class=yel> verificado la presenza dei tre doppi apici in fondo, <span class=red>ma togli le prime righe fino a far rimanere <span class=gil>PyDev console: using IPython 9.4.0</span> come prima riga della selezione
7. assicurandoti che la finestra attiva ( <span class=gil>in focus, cioè visibile </span>) sia <br> <span class=yel> task.py</span>, imposta <span class=yel>'Current File' </span> nel target di esecuzione, che è posizionato nel Menu Personalizzato <br> 
   ( <span class=yel>sulla sinistra</span> del <span class=gil>bottone run |> di esecuzione</span> ) ti sposti sull'icona 'più opzioni' (tre puntini) e dal menù a tendina scegli modifica 'l'esecuzione con parametri': nella casella 'name' inserisci al posto di 'task' il nome della directory padre '3.0.1 docstrings', seleziona la check box 'store as project file' conferma su 'done', e poi su 'apply'. In questo modo l'esecuzione nella console avrà il nome della configurazione. 
8. esegui ora la configurazione salvata che compare nella lista '3.0.1 docstrings' cliccando sul bottone di run |>
9. Se il <span class=red> risultato non ti soddisfa chiudi la finestra 'Python Console' cliccando su X <br>
   <span class=gil> e riprova magari raddoppiando il carattere backslash del path dell'interprete <span class=red>se hai dimenticato di eliminare le prime righe fino a far rimanere come prima riga <span class=gil> PyDev console: using IPython 9.4.0  
10. Quando vuoi registrare il risultato <span class=yel> clicca sull'icona della stampante dalla vista RUN ( Alt-4 )
11. Nelle impostazioni scegli il font per il <san class=yel>testo</span> e poi anche per <span class=yel>header e footer <span class=gil> source code pro 12, </span> come header (ricopiare con il segno del $) <span class=gil>`$FILE$ - NOME COGNOME`</span>, come footer <span class=gil>`Pagina $PAGE$ of $TOTALPAGES$ - Stampato il $DATE$ alle $TIME$`
11. Stampa, selezionando Console Text e dopo aver fatto Apply delle modifiche, selezionando come stampante <span class=red>Microsoft Print to pdf</span> impostando il font <span class=gil> source code pro 13, </span>per header e footer, e nominandolo <span class=yel> 3.0.1.cognome_nome.pdf<br> lo salvi in una directory. 

<div class="hint">
<p>
Per sapere come eseguire un task nella console vedere il video eseguendo lo script 
<span class="gil">ComeEseguireNellaConsole.py</span> presente nelle configurazioni, ma ci sono delle modifiche rispetto al video : <br>
    1. al posto della console standard è usata la interattiva IPython;<br>
    2. la selezione da copiare è da 'PyDev console: using IPython ...' che compare nel tooltip 'Pyton Console' dentro l'area della console una volta che si è cliccati sopra appena partita la console</p>
<p>
Per sapere come salvare l'output di un task come file .pdf vedere il video eseguendo lo script 
<span class="gil">ComeSalvareOutputTaskInPdf.py</span> presente nelle configurazioni
</p>


<p> Esempio: <br>
>>> # autore nome e cognome  <br>
>>> 888 # numero preferito<br>
888<br>
>>> "rosso-nero" # colore preferito <br>
rosso-nero<br>
</p>
</div>
