# Reseptisovellus
*Aineopintojen harjoitustyö: Tietokantasovellus (Tsoha)*

Sovellus löytyy osoitteesta
https://polar-hamlet-77249.herokuapp.com/

Sovellus sisältää reseptejä, joita voi hakutoiminnolla rajata ainesosan tai ruuan tyypin perusteella (keitto, kasvisruoka, jälkiruoka jne.). Reseptit ovat kaikkien luettavissa, mutta kirjautumalla sisään käyttäjä saa lisätoimintoja käyttöönsä. Ilman kirjautumista käyttäjä voi etsiä ja rajata reseptejä, sekä kirjautua tai luoda uuden tunnuksen. Kirjautunut käyttäjä voi lisätä uusia reseptejä ja muokata lisäämiään sekä merkitä reseptin suosikiksi.

### Resepti
Reseptin tulee sisältää ainakin seuraavat tiedot: 
- uniikki nimi 
- montako annosta reseptistä tulee 
- ainesosalista 
- valmistusohje 

Suositeltavia reseptin tietoja on lisäksi ruuan tyyppi sekä valmistusaika (aktiivinen/passiivinen)

Reseptit voi listata eri tavoin. Automaattinen listaus on kronologisessa järjestyksessä, eli reseptit näkyvät lisäysjärjestyksessä. Lisäksi reseptit voi listata suosituimmaista vähiten suosittuun, joka tapahtuu suosikkimerkintöjen avulla. 

-------------------------------------------------------------------------------------

### Ideoita jatkokehitykseen
#### Käyttäjä voi lisätä omat aineet
- Käyttäjä voi lisätä kotoaan löytyvät ainekset ja hakea reseptejä joihin aineet löytyvät. Jos voi myös lisätä aineksiinsa määrät, haku on tarkempi.
- Reseptien haku listaisi ainekset sen mukaan mihin löytyy parhaiten aineksia

#### Resepti 
- Reseptin annosmäärän muuttaminen - ainesosalistan ainesosien määrät muuttuvat kun valikosta muutetaan annosmäärää
- Reseptiin voisi lisätä kuvan ja/tai esittelytekstin ja reseptisivulla voisi näkyä suosikkimerkintöjen määrä
- Ylläolevien toteutuksen jälkeen olisi mahdollista lisätä omien ainesten hakuun valinta montako annosta kyseistä ruokaa pitäisi saada
- Reseptiä voi mahdollista kommentoida ja kommentteihin voisi vastata
- Reseptihakuun voisi laittaa useampia aineksia

#### Käyttäjäroolit
Uusi käyttäjärooli, ylläpitäjä
 - ylläpitäjä voisi muokata mitä tahansa reseptiä tai poistaa reseptin
 - ylläpitäjä voisi lisätä uusia ylläpitäjiä
 - ylläpitäjä voisi asettaa käyttäjän "jäähylle"

-------------------------------------------------------------------------------------

### Välipalautusten sisällöt
#### Välipalautus 1: Suunnitelma
Alustava suunnitelma

#### Välipalautus 2: Pohja ja sisäänkirjautuminen
Sovelluksen pohja on valmis. Käyttäjä voi luoda uuden tunnuksen tai kirjautua sisään. Kirjautunut käyttäjä voi kirjautua ulos. Kirjautuneen käyttäjän silmille tarkoitetut sivut eivät näy kirjautumattomille käyttäjille.

#### Välipalautus 3: Resepteihin liittyvät toiminnot - lisääminen/haku/listaus. Ulkoasun parantelu.
- Ohjelman ulkoasu on huoliteltu. 
- Ohjelman komponentit on aseteltu niin, että sitä on mukava käyttää myös mobiilissa
- Käyttäjä voi lisätä reseptin, kaikki reseptit ovat listana reseptit-sivulla. Käyttäjän omalta sivulta pääsee selaamaan käyttäjän lisäämiä reseptejä.
- Reseptin lisäämisen yhteydessä tapahtuva ainesosien lisääminen toimii. Reseptin sivulla ainesosat ovat listattuina. Reseptit-sivulla on hakutoiminto jolla voi etsiä tiettyä ruoka-ainetta sisältäviä reseptejä. 
- Käyttäjä voi "tykätä" reseptistä, eli merkitä sen suosikikseen. Samasta napista suosikkireseptin voi merkitä ei-suosikiksi. Kirjautunut käyttäjä voi suosikit-sivulla selata suosikkireseptejään.
- (käyttäjä voi muokata omia reseptejään)

#### Loppupalautus: Viimeistely.
Ulkoasun viimeistely, haku ja reseptin ainesosien syöttö toimii pienillä kirjaimilla, reseptille voi antaa tagejä joita voi etsiä ainesosien tapaan ja jotka on lueteltuna reseptit-sivulla
