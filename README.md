Il seguente progetto consiste in una semplice applicazione Django progettata per gestire gli allenamenti, tracciare gli obiettivi e monitorare i progressi degli utenti. L'applicazione consente agli utenti di registrare i loro allenamenti, impostare obiettivi, monitorare i progressi e visualizzare semplici statistiche.

## Funzionalità

- **Autenticazione Utente**: Registrazione, login, logout e gestione dei profili utente.
- **Tracciamento degli Obiettivi**: Gli utenti possono impostare obiettivi personali e monitorarne il completamento.
- **Monitoraggio dei Progressi**: Gli utenti possono visualizzare le statistiche dei loro progressi attraverso grafici.
- **Gestione degli Allenamenti**: Gli utenti possono iniziare, aggiornare e concludere i loro allenamenti, registrando i dettagli degli esercizi svolti.

##Struttura del progetto
-**users**: App per la gestione degli utenti e dei 
-**goals**: App per la gestione degli 
-**training**: App per la gestione degli 
-**templates**: Directory dei template HTML per login e registrazione.

##URLS
-**Pagina di registrazione**
	URL: /users/register/
	Descrizione: Questa pagina consente agli utenti di registrarsi creando un nuovo 					        account
-**Pagina di login**
	URL: /accounts/login/
	Descrizione: Questa pagina consente agli utenti di effettuare il login.
-**Pagina del profilo utente**
	URL: /users/profile/
	Descrizione: Questa pagina consente agli utenti di visualizzare e aggiornare il 						     proprio profilo.
-**Pannello di amministrazione**
	URL: /admin/
	Descrizione: Questa pagina consente agli amministratori di gestire il sito tramite il 					    pannello di amministrazione di Django.
	Credenziali Admin: lova1926/Batistuta-9
-**Pagina per creare un goal**
	     URL: /goals/create/
	     Descrizione: Pagina per creare un nuovo obiettivo	
-**Pagina per visualizzare i dettagli di un goal**
     URL:  /goals/<int:pk>/
     Descrizione: Pagina per visualizzare i dettagli di un obiettivo.  
-**Pagina per iniziare un allenamento**       
       URL:`/training/start/`
       Descrizione: Pagina per iniziare un nuovo allenamento.
-**Pagina per aggiornare l’allenamento con un esercizio appena svolto**
       URL: /training/update/<int:workout_id>/
       Descrizione:Pagina per aggiornare un allenamento in corso con nuovi esercizi. 
 -**Pagina per interrompere un allenamento**
      URL: /training/stop/<int:workout_id>/`
      Descrizione: Pagina per fermare un allenamento e registrare la durata. 
-**Pagina per vedere i dettagli di un allenamento**
     URL:/training/<int:workout_id>/`
     Descrizione:Pagina per visualizzare i dettagli di un allenamento completato.

##Descrizione
Questo sito una volta che ci si è registrati permette di accedere alla propria pagina nella quale, oltre a vedere le proprie informazioni principali, è possibile creare degli obbiettivi ai quali si attribuisce un titolo, una descrizione, un livello di difficoltà da 1 a 5 e l’etichetta di “completato”/“non completato”. È possibile inoltre avviare un allenamento e registrare via via gli esercizi che si sono svolti, una volta terminato l’allenamento sarà possibile visualizzare gli esercizi che si sono svolti e la durata dello stesso. Il sito crea  un grafico che permette di vedere la percentuale di obbiettivi portati a termine rispetto al totale di quelli che ci è predisposti, questa semplice statistica dà la possibilità di tenere traccia dei propri progressi.

   ##Account Registrati
   1) lova1926/Batistuta-9
   2) greg1926/Batistuta-9
   3)ele_gaetani/Batistuta-9
