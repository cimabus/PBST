<style> 
   body { font-size: 15px}
    .yel { color : yellow }
    .gil { color : greenyellow }
    .red { color : red }
    .cyan { color : cyan }
    .wit { color : white ; font-family: "Source Code Pro",monospace; }
    .gre { color : green ; font-family: "Source Code Pro",monospace; }
    .cya { color : green ; font-family: "Source Code Pro",monospace; }
   .gry {
      background-color: darkgrey; /* Colore dello sfondo */
      color: black; /* Colore del testo */
      display: inline; /* Assicurati che lo sfondo si adatti al testo */
      /* padding: 0 2px; /* Spazio intorno al testo (opzionale) */
    }

</style>
<span class=cyan>**3.1 Usare Python come una calcolatrice**</span>

<span class=gil>**3.1.1 Numeri: i tipi Int e Float**</span>

Per la teoria <a href=https://pytutorial-it.readthedocs.io/it/python3.13/introduction.html#numeri>qui</a>
trovi le indicazioni per rispondere agli esercizi.

Per lo svolgimento degli esercizi vedi <span class=cyan>**la lezione sui commenti**</span>
<a href="course://3.Introduzione informale/3.0 Commenti/3.0.1 docstrings"><span class=gil>3.0.1 docstrings</span></a> che spiega come [attivare l'interprete ](https://drive.google.com/file/d/1utNhK1t8zRGV2NLA3Ujr_7xJI_vwTIpG/view?usp=drive_link)ed eseguire gli esercizi nella
console, [stampare lo standard output della console python in un file locale ](https://drive.google.com/file/d/1RzCAVIWbOW1kr9lTXmu7Apo041IzqkGI/view?usp=drive_link),
svolgere gli esercizi e verificata la correttezza con il check <span class=yel>rieseguire il task nominandolo</span> nella configurazione col suo nome <span class=yel>'3.1.1 Numeri'</span> e stamparlo.</span>

Svolgere nella console e poi <span class=gil> riportare nel placeholder</span>, rettagolo evidenziato con bordi visibili, 
<span class=gre>il comando inserito nella console</span> e il <span class=whi>**risultato ottenuto**</span> delle seguenti operazioni</span>, 
<span class=yel>copiando l'output dalla console </span> (dalla riga <span class=red> PyDev console: using IPython 9.5.0 </span>), <span class=gil>posizionandosi col cursore su di essa </span> <span class=white>(cursore scompare) </span> <span class=gil> digitando Ctrl+A </span> per selezionare il testo <span class=white>(il testo nella console viene evidenziato)</span> <span class=gil> posizionando il cursore nel placeholder e digitando Ctrl+C </span> per riportarla:

1. <span class=yel> clicca </span>nell'area di output sul tooltip <span class=gry>Python Console</span> per visualizzare il messaggio di avvio della console interattiva <span class=gil>PyDev console: using IPython 9.5.0</span> insieme ad altre segnalazioni di ambiente;<span class=red> se console standard</span><span class=cya> prompt '>>>'</span> <span class=yel>cambiala selezionando </span><span class=cya>Use IPython </span>da File -> Settings -> Python -> Console -> General settings;
2. <span class=yel>scrivi</span><span class=gil> una espressione aritmetica su interi </span> con tutti gli operatori aritmetici in modo che il risultato sia di tipo intero
   <br>es.<br><span class=gre>In [2]: </span>1+2\*3-4<br><span class=wit>Out[2]: </span>3
   <br>cosa succede se metto due operatori successivi ?
   <br>es.<br><span class=gre>In [3]: </span>3\* +5 \* -2 - +5
   <br>es.<br><span class=gre>In [4]: </span>-7 + \* -5<br>
3. <span class=gil>Aggiungiamo l'operatore di divisione</span> e notiamo che il risultato non è più un Int ma un Float
   <br>es.<br><span class=gre>In [5]: </span>3\*4/5<br><span class=wit>2.4<br>
4. Quindi la divisione tra interi <span class=yel>restituisce un float</span> anche se il resto è nullo.
   <br><span class=gre>In [6]: </span>18 / 5 # Scegli due numeri e <span class=gil>dividili in modo da avere un resto</span><br><span class=wit>Out[6.1]:  </span>3.6<br>
   <br><span class=gre>In [6.1]: </span>18 // 5 # Adesso Scegli due numeri e <span class=gil>dividili in modo da troncare il resto e avere un numero intero</span><br><span class=wit>Out[6.1]:  </span>3<br>
   <br><span class=gre>In [7]: </span> _ + 18 % 5 # <span class=gil>aggiungi </span>il resto 18 % 5 al risultato appena stampato e referenziato da '\_'<br><span class=wit>Out[7]: </span>5.4<br>

5. <span class=gil>Assegna </span>due valori interi a due variabili, il secondo come risultato di una espressione aritmetica, poi li
   moltiplichi
   <br><span class=gre>In [8]: </span>base = 16
   <br><span class=gre>In [9]: </span>altezza = 5 + 2
   <br><span class=gre>In [10]: </span>base * altezza<br><span class=wit>Out[10]:  </span>112<br>
6. Scrivi <span class=gil>un literal non ancora utilizzato</span>
   <br><span class=gre>In [11]: </span>literal_corretto_ma_non_ancora_utilizzato<br>
   <span class=yel>riporta dall'output </span>la riga che comincia con Traceback e l'ultima che riporta il messaggio di errore <span class=red><br>Traceback (most recent call last):<br>NameError: name 'literal_corretto_ma_non_ancora_utilizzato' is not defined</span>
7. <span class=gil>Assegna </span>8.5% alla variabile iva, 100 alla variabile prezzo e calcola prezzo + iva utilizzando la variabile '_' che in
   modalità interattiva ha come valore l'ultima espressione calcolata
   <br><span class=gre>In [12]: </span>iva = 00.00 / 100 # percentuale della tassa
   <br><span class=gre>In [13]: </span>prezzo = 0000 # prezzo
   <br><span class=gre>In [14]: </span>prezzo * iva # tassa<br><span class=wit>Out[14]: </span>?<br>
   <br><span class=gre>In [15]: </span>prezzo + _ # prezzo + tassa<br><span class=wit>Out[15]: </span>?<br>

<div class="hint">

<p>
Per sapere come <span class="yel">eseguire un task</span> nella console vedere il video eseguendo lo script
<a href="course://3.Introduzione informale/3.0 Commenti/3.0.1 docstrings/ComeEseguireNellaConsole.py">ComeEseguireNellaConsole.py</a>
selezionandolo e <span class="gil">scegliendo Run</span> dal menù contestuale (tasto destro mouse).

<p>
Per sapere come <span class="yel">salvare l'output di un task</span> in un file .pdf vedere il video eseguendo lo script 
<span class="gil">ComeSalvareOutputTaskInPdf</span> presente, come il precedente, nelle 
<a href="course://3.0 Introduzione informale/3.0 Commenti/3.0.1 docstrings">configurazioni di esecuzione</a>
</p>
</div>
     
