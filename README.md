# I AM MUSIC - Music Streaming Service

**Student:** Liam Renzini (matricola: 7110050)
**Project Type:** Full-Stack Web Application
**Framework:** Django

## Description
I AM MUSIC è un sito di streaming musicale dal design minimalistico bianco e nero, con la possibilità di gestire le proprie playlist una volta eseguito l'accesso, con una sezione news con le ultime notizie in ambito musicale. La sezione centrale della pagina principale del sito se non si è loggati presenta una sezione "YOU MAY LIKE" dove vengono proposti 6 barni casuali dal databse e in basso una sezione con le playliust create dagli utenti, se invece si è loggati con un account, la sezione centrale diventa "MADE 4 U, nome utente" dove vengono proposti 6 brani suggeriti in base ai generi delle canzon i già presenti nelle playlist create dall'utente, personalizzando la schermata di ogni utente, inoltre nella sezione "MADE BY U" si aggiunge un + dove è possibili creare nuove playlist.

## Features
* **Not Logged:** Può vistare il sito e cercare nella barra di ricerca della home page.
* **Listener:** Può visitare il sito e gestire le proprie playlist nella sezione in basso "MADE BY U", nella creazione e modifica delle playlist è presente una barra di ricerca con un filtro per genere per facilitare la ricerca delle canzoni da aggiungere alla playlist. Il nome delle playlist deve essere lungo almeno due caratteri e non deve contenere alcune parole vietate, altrimenti viene restituito un messaggio di errore.
* **Curator:** Ha le stesse feature dell'account Listener e in più ha una dashboard dedicata dove è possibile aggiungere eliminare e gestire canzoni e generi che aggiornano in tempo reale il database, nota: se viene eliminato un genere musicale, vengono eliminate a cascata tutte le canzoni relative a quel genere musicale.

## Local Installation
1. Copia repository: `git clone https://github.com/ItsLiammm/ProgettoBACKEND`
2. Crea e attiva un ambiente virtuale.
3. Installa dependencies: `pip install -r requirements.txt`
4. Fai partire il server: `python manage.py runserver`
*(Nota: Le migrazioni sono già state applicate e il database è gia incluso).*


## Database & Demo Accounts
La repository include un SQLiter database pre popolato (`db.sqlite3`) con dati di prova realistici (songs, genres, playlists). 


**Demo Accounts:**
* **Curator:** `username:` curatorDemo | `password:` curDemo123 | `role:` Curator
* **Listener:** `username:` listenerDemo | `password:` listDemo123 | `role:` Listener
E' presente anche un account admin utilizzabile solo nella dashboard di django accessibile aggiungendo `/admin/` all'URL del sito, che è in grado di gestire tutto:
* **Superuser:** `username:` utentesup | `password:` supp1234 | `role:` Admin

## Deployment
Il sito è online e può essere testato qui:
**[INSERISCI IL LINK AL SITO DEPLOYATO]**

## Testing Scenario
1. Aprire il link di deployment.
2. Accedere con l'account da **Curator** (`curatorDemo`).
3. Clicca su "MANAGE LIBRARY" nell'header per accedere alla dashboard del curatore.
4. Aggiungi una nuova canzone o un genere o eliminane alcune, ritorna alla home e verifica i cambiamenti.
5. Esci, e riaccedi con l'account da **Listener** (`listenerDemo`).
6. Crea una nuova playlist o cancella o modifica una delle già presenti.
7. Prova ad accedere alla sezione curatore senza loggarti come tale aggiungendo `/management/` all'URL del sito (dovrebbe non essere permesso).
