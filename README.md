# Reseptisovellus
*Aineopintojen harjoitustyö: Tietokantasovellus (Tsoha)*

Sovellus löytyy osoitteesta
https://polar-hamlet-77249.herokuapp.com/

Sovellus sisältää reseptejä, joita voi hakutoiminnolla rajata ainesosan tai ruuan tyypin perusteella (keitto, kasvisruoka, jälkiruoka jne.). Reseptit ovat kaikkien luettavissa, mutta kirjautumalla sisään käyttäjä saa lisätoimintoja käyttöönsä.

- Ilman kirjautumista käyttäjä voi etsiä ja rajata reseptejä, sekä kirjautua tai luoda uuden tunnuksen.
- Kirjautunut käyttäjä voi lisätä uusia reseptejä tai merkitä reseptin suosikiksi.
- Ylläpitäjä voi lisäksi poistaa tai muokata reseptejä sekä lisätä uuden ylläpitäjän.

**Seuraavista ominaisuuksista toteutetaan ainakin toinen:**
1. Kirjautunut käyttäjä voi kommentoida reseptiä
2. Kirjautunut käyttäjä voi syöttää kotoaan löytyvät ainekset, ja etsiä reseptejä joihin sopivat ainekset löytyvät kaapista. Sovellus muistaa käyttäjän ainekset ja niitä voi päivittää.


### Resepti
Reseptin tulee sisältää ainakin seuraavat tiedot: 
- uniikki nimi 
- montako annosta reseptistä tulee 
- ainesosalista 
- valmistusohje 

Suositeltavia reseptin tietoja on lisäksi ruuan tyyppi sekä valmistusaika (aktiivinen/passiivinen)

### Ideoita jatkokehitykseen
- idea 1: Suunnitelmissa on syöttää kotona olevista aineksista alkuun vain tuotteet ilman määriä. Mikäli aikaa jää, toteutan omiin aineksiin mahdollisuuden lisätä ainesosien määrät.
- Reseptin annosmäärän muuttaminen - ainesosalistan ainesosien määrät muuttuvat kun valikosta muutetaan annosmäärää
- Ylläolevien toteutuksen jäälkeen on mahdollista lisätä omien ainesten hakuun valinta montako annosta kyseistä ruokaa pitäisi saada
- idea 1: Reseptien järjestäminen sen mukaan, mihin löytyy parhaiten aineksia valmiiksi
- idea 2: Reseptiä voi mahdollista kommentoida ja kommentteihin voisi vastata
- Reseptiin voisi lisätä kuvan ja/tai esittelytekstin
- Reseptisivulla voisi näkyä suosikkimerkintöjen määrä

### Välipalautusten sisällöt
#### Välipalautus 1: Suunnitelma
Alustava suunnitelma

#### Välipalautus 2: Pohja ja sisäänkirjautuminen
Sovelluksen pohja on valmis. Käyttäjä voi luoda uuden tunnuksen tai kirjautua sisään. Kirjautunut käyttäjä voi kirjautua ulos. Kirjautuneen käyttäjän silmille tarkoitetut sivut eivät näy kirjautumattomille käyttäjille.

#### Välipalautus 3: Resepteihin liittyvät toiminnot sekä ylläpitäjän toiminnot. Ulkoasun parantelu.
- Ohjelman värit ovat yhtenäiset ja CSS koodi luotu. Sovellus näyttää lähes tuotantoon soveltuvalta.
- Käyttäjä voi lisätä reseptin, kaikki reseptit ovat listana reseptit-sivulla. Käyttäjän omalta sivulta pääsee selaamaan käyttäjän lisäämiä reseptejä.
- Reseptin lisäämisen yhteydessä tapahtuva ainesosien lisääminen toimii. Reseptin sivulla ainesosat ovat listattuina. Reseptit-sivulla on hakutoiminto jolla voi etsiä tiettyä ruoka-ainetta sisältäviä reseptejä. 
- Käyttäjä voi "tykätä" reseptistä, eli merkitä sen suosikikseen. Samasta napista suosikkireseptin voi merkitä ei-suosikiksi. Kirjautunut käyttäjä voi suosikit-sivulla selata suosikkireseptejään.
- (käyttäjä voi muokata omia reseptejään)
- (reseptille voi antaa tagejä joita voi etsiä ainesosien tapaan ja jotka on lueteltuna reseptit-sivulla)
- (reseptin annosmäärää voi muokata, jolloin ainesten määrät muuttuvat)
- (ylläpitäjän toiminnot - voi muokata kaikkia reseptejä - voi lisätä uuden yllääpitäjän)

#### Loppupalautus: Viimeistely.
