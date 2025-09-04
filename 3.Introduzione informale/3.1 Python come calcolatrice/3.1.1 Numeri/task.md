<style> 
    .yel { color : yellow }
    .gil { color : greenyellow }
    .red { color : red }
    .cyan { color : cyan }
    .wit { color : white ; font-family: "Source Code Pro",monospace; }
    .gre { color : green ; font-family: "Source Code Pro",monospace; }
    .cya { color : green ; font-family: "Source Code Pro",monospace; }
</style>
**Usare Python come una calcolatrice**

**Numeri: i tipi Int e Float**

Per la teoria <a href=https://pytutorial-it.readthedocs.io/it/python3.13/introduction.html#numeri>qui</a>
trovi le indicazioni per rispondere agli esercizi.

Per lo svolgimento degli esercizi vedi **la lezione sui commenti**
<a href="course://3.Introduzione informale/3.0 Commenti/3.0.1 docstrings"><span class=gil>3.0 Commenti</span></a> che spiega come [attivare l'interprete ](https://drive.google.com/file/d/1Xuy6vo1cvDAQemLDIM3RS_6afwmgdxZm/view?usp=drive_link) <span class=cyan>(link in dominio ITT Molinari)</span> ed eseguire gli esercizi nella
console, [stampare lo standard output della console python in un file locale ](https://drive.google.com/file/d/1EOvc01A_T4QV4BD3pk8Rk4HIw9KyPXj8/view?usp=drive_link)<span class=cyan>(link in dominio ITT Molinari)</span>,
svolgere gli esercizi, verificandone la correttezza con il check, una vota ottenutolo <span class=yel>rieseguire il task ancora una volta accertandosi di averlo nominato nella configurazione '3.1.1 Numeri' e stamparlo.</span>

Svolgere nella console e poi <span class=gil> riportare nel placeholder</span>, rettagolo evidenziato con bordi visibili, 
<span class=gil>il comando inserito nella console e il risultato ottenuto delle seguenti operazioni</span>, 
<span class=yel>copiando l'output ottenuto nella console </span> <span class=red> (senza la prima riga) </span>, <span class=gil>posizionandosi col cursore su di essa </span> <span class=white>(cursore scompare) </span> <span class=gil> cliccando Ctrl+A </span> <span class=cyan>(il testo nella console viene evidenziato)</span> <span class=gil> posizionandosi poi col cursore nel placeholder e cliccando Ctrl+C </span> per riportarla:

1. <span class=gil>una espressione aritmetica su interi </span> con tutti gli operatori aritmetici in modo che il risultato sia di tipo intero
   <br>es.<br><span class=gre>In [2]: </span>1+2\*3-4<br><span class=wit>Out[2]: </span>3
   <br>cosa succede se metto due operatori successivi ?
   <br>es.<br><span class=gre>In [3]: </span>3\* +5 \* -2 - +5
   <br>es.<br><span class=gre>In [4]: </span>-7 + \* -5<br>
2. <span class=gil>Aggiungiamo l'operatore di divisione</span> e notiamo che il risultato non è più un Int ma un Float
   <br>es.<br><span class=gre>In [5]: </span>3\*4/5<br><span class=wit>2.4<br>
3. Quindi la divisione tra interi <span class=yel>restituisce un float</span> anche se il resto è nullo.
   <br><span class=gre>In [6]: </span>18 / 5 # Scegli due numeri e <span class=gil>dividili in modo da avere un resto</span><br><span class=wit>Out[6.1]:  </span>3.6<br>
   <br><span class=gre>In [6.1]: </span>18 // 5 # Adesso Scegli due numeri e <span class=gil>dividili in modo da troncare il resto e avere un numero intero</span><br><span class=wit>Out[6.1]:  </span>3<br>
   <br><span class=gre>In [7]: </span> _ + 18 % 5 # <span class=gil>aggiungi </span>il resto 18 % 5 al risultato appena stampato e referenziato da '\_'<br><span class=wit>Out[7]: </span>5.4<br>

4. <span class=gil>Assegna </span>due valori interi a due variabili, il secondo come risultato di una espressione aritmetica, poi li
   moltiplichi
   <br><span class=gre>In [8]: </span>base = 16
   <br><span class=gre>In [9]: </span>altezza = 5 + 2
   <br><span class=gre>In [10]: </span>base * altezza<br><span class=wit>Out[10]:  </span>112<br>
5. Scrivi <span class=gil>un literal non ancora utilizzato</span>
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
<span class="gil">ComeEseguireNellaConsole</span> presente nelle 
[configurazione da eseguire]()
<a href="course://3.Introduzione informale/3.0 Commenti/3.0.1 docstrings">configurazioni di esecuzione</a>
</p>

<p>
Per sapere come <span class="yel">salvare l'output di un task</span> in un file .pdf vedere il video eseguendo lo script 
<span class="gil">ComeSalvareOutputTaskInPdf</span> presente nelle 
<a href="course://3.0 Introduzione informale/3.0 Commenti/3.0.1 docstrings">configurazioni di esecuzione</a>
</p>
</div>
     
