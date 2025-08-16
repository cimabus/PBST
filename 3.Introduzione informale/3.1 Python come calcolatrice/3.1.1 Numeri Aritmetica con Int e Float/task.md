<style> 
    .yel { color : yellow }
    .gil { color : greenyellow }
    .red { color : red }
    .cyan { color : cyan }
</style>
**Usare Python come una calcolatrice**

**Numeri: i tipi Int e Float**

Per la teoria <a href=https://pytutorial-it.readthedocs.io/it/python3.11/introduction.html#numeri>qui</a>
trovi le indicazioni per rispondere agli esercizi.

Per lo svolgimento degli esercizi vedi **la lezione sui commenti**
in [PythonBaseStandardTutorial\3.Introduzione informale\3.0 Commenti](course://3.0 Introduzione informale/3.0 Commenti/3.0.1 docstrings)
che spiega
come [attivare l'interprete](https://drive.google.com/file/d/1Xuy6vo1cvDAQemLDIM3RS_6afwmgdxZm/view?usp=drive_link) ed
eseguire gli esercizi nella
console, [stampare lo standard output della console python in un file locale](https://drive.google.com/file/d/1EOvc01A_T4QV4BD3pk8Rk4HIw9KyPXj8/view?usp=drive_link),
svolgere gli esercizi,
nonché verificare se l'esercizio è stato svolto correttamente.

Svolgere nella console e poi <span class=gil> riportare nel placeholder</span>, rettagolo evidenziato con bordi visibili, 
<span class=gil>il comando inserito nella console e il risultato ottenuto delle seguenti operazioni</span>, 
<span class=yel>copiando l'output ottenuto nella console </span> <span class=red> (senza la prima riga) </span>, <span class=gil>posizionandosi col cursore su di essa </span> <span class=white>(cursore scompare) </span> <span class=gil> cliccando Ctrl+A </span> <span class=cyan>(il testo nella console viene evidenziato)</span> <span class=gil> posizionandosi poi col cursore nel placeholder e cliccando Ctrl+C </span> per riportarla:

1. <span class=gil>una espressione aritmetica su interi </span> con tutti gli operatori aritmetici in modo che il risultato sia di tipo intero
   <br>es. >>> 1+2*3-4
   <br>3
   <br>cosa succede se metto due operatori successivi ?
   <br>es. >>> 3* +5 * -2 - +5
   <br>es. >>> -7 + * -5
2. <span class=gil>Aggiungiamo l'operatore di divisione</span> e notiamo che il risultato non è più un Int ma un Float
   <br>es. >>> 3*4/5
   <br> 2.4
3. Quindi la divisione tra interi <span class=yel>restituisce un float</span> anche se il resto è nullo.
   <br>>>> 17 / 5 # Scegli due numeri e <span class=gil>dividili in modo da avere un resto</span>
   <br>3.4
   <br>>>> 17 // 5 # Questo operatore <span class=gil>tronca il float prendendo solo la parte intera</span>
   <br>3
   <br>>>> _ + 17 % 5 # <span class=gil>aggiungi </span>il resto 17 % 5 al risultato appena stampato e referenziato da '_'
   <br>5
4. <span class=gil>Assegna </span>due valori interi a due variabili, il secondo come risultato di una espressione aritmetica, poi li
   moltiplichi
   <br>>>> base = 16
   <br>>>> altezza = 5 + 2
   <br>>>> base * altezza
5. Scrivi <span class=gil>un literal non ancora utilizzato</span>
   <br>>>> literal_corretto_ma_non_ancora_utilizzato
   <br><span class=yel>riporta dall'output </span>la riga che comincia con Traceback e l'ultima che riporta il messaggio di errore 
7. <span class=gil>Assegna </span>8.5% alla variabile iva, 100 alla variabile prezzo e calcola prezzo + iva utilizzando la variabile '_' che in
   modalità interattiva ha come valore l'ultima espressione calcolata
   <br>>>> iva = 00.00 / 100 # percentuale della tassa
   <br>>>> prezzo = 0000 # prezzo
   <br>>>> prezzo * iva # tassa
   <br>>>> prezzo + _ # prezzo + tassa

<div class="hint">

<p>
Per sapere come <span class="yel">eseguire un task</span> nella console vedere il video eseguendo lo script 
<span class="gil">ComeEseguireNellaConsole</span> presente nelle 
<a href="course://3.0 Introduzione informale/3.0 Commenti/3.0.1 docstrings">configurazioni di esecuzione</a>
</p>

<p>
Per sapere come <span class="yel">salvare l'output di un task</span> in un file .pdf vedere il video eseguendo lo script 
<span class="gil">ComeSalvareOutputTaskInPdf</span> presente nelle 
<a href="course://3.0 Introduzione informale/3.0 Commenti/3.0.1 docstrings">configurazioni di esecuzione</a>
</p>
</div>
     
