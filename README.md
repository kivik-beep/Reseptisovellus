# Reseptisovellus
*Aineopintojen harjoitustyö: Tietokantasovellus (Tsoha)*

Sovellus löytyy osoitteesta
https://polar-hamlet-77249.herokuapp.com/

Kyseessä on sovellus, joka sisältää käyttäjien lisäämiä reseptejä. Sovellusta voi käyttää joko kirjautumatta tai kirjautumalla sisään.

----------------------------------------------------------------------------------
### Käyttäjätoiminnot
#### Kirjautumaton käyttäjä voi
- Selata reseptejä
  - Suodattaa reseptejä ainesosahaun avulla (etsii reseptit joissa haettu sana esiintyy jossain aineksessa)
  - Suodattaa reseptejä tagien perusteella
  - Järjestää kaikki reseptit sisältävän listan aakkosjärjestyksen, uutuuden, suosion, ainesosien määrän sekä valmistusajan perusteella
- Kirjautua sisään tai luoda uuden tunnuksen

#### Kirjautuessaan käyttäjä pystyy lisäksi
- tykkäämään lisätyistä resepteistä, sekä poistamaan antamansa tykkäyksen
- Selata reseptejä jotka
  - On itse lisännyt (omat reseptit)
  - On merkinnyt suosikikseen (omat suosikit)
- Muokkaamaan reseptejä jotka on lisännyt
  - muokkaus sivulle pääsee joko omien reseptien tai ko. reseptin sivulta
  - muokkaus sivulla lisätään reseptiin tagit
  - muokkaus sivulla voi reseptin lisäksi muokata ja poistaa tagejä
------------------------------------------------------------------------------------

### Resepti
Reseptin tulee sisältää ainakin seuraavat tiedot: 
- uniikki nimi 
- montako annosta reseptistä tulee 
- ainesosalista 
- valmistusohje 

Suositeltavia reseptin tietoja on lisäksi ruuan tyyppi sekä valmistusaika (aktiivinen/passiivinen)

Reseptit voi listata eri tavoin. Automaattinen listaus on aakkosjärjestyksessä. Lisäksi reseptit voi listata uusimmasta vanhimpaan, ainesosien määrän tai valmistusajan pituuden perusteella, sekä suosituimmaista vähiten suosittuun. Reseptiä voi muokata, ja muokkauksen yhteydessä siihen voi liittää asiasanoja eli tagejä. Reseptejä voi etsiä tagien tai ainesosien perusteella.

-------------------------------------------------------------------------------------

### Ideoita jatkokehitykseen
Kriittisimmät kehitysideat esitetty **paksunnetulla** tekstillä.
#### Käyttäjä voi lisätä omat aineet
- Käyttäjä voi lisätä kotoaan löytyvät ainekset ja hakea reseptejä joihin aineet löytyvät. Jos voi myös lisätä aineksiinsa määrät, haku on tarkempi.
- Reseptien haku listaisi ainekset sen mukaan mihin löytyy parhaiten aineksia

#### Resepti 
- **reseptin ainesosien listauksessa olisi hyvä jos kokonaisluvuissa ei olisi perässä '.00'**
- **reseptin voi poistaa**
- Ainesosien lisäys voisi tunnistaa jos merkkijonossa on osana ',' ja sovellus osaisi vaihtaa sen tilalle '.'
- Tagejä lisätessä voisi nähdä listan käytössä olevista tageistä, joiden perusteella käyttäjän olisi helpompi lisätä tagejä
- Tagit voisi esittää niihin liitettyjen reseptien määrän perusteella järjestettyinä, suosituimmasta vähiten suosittuun 
- Reseptin annosmäärän muuttaminen - ainesosalistan ainesosien määrät muuttuvat kun valikosta muutetaan annosmäärää
- Reseptiin voisi lisätä kuvan ja/tai esittelytekstin ja reseptisivulla voisi näkyä suosikkimerkintöjen määrä
- Ylläolevien toteutuksen jälkeen olisi mahdollista lisätä omien ainesten hakuun valinta montako annosta kyseistä ruokaa pitäisi saada
- Reseptiä voi mahdollista kommentoida ja kommentteihin voisi vastata
- Reseptihakuun voisi laittaa useampia aineksia

#### Käyttäjät
Käyttäjänimen voisi tallentaa erikseen, niin että se esitettäisiin jatkossa käyttäjän alunperin syöttämässä muodossa. Tällä hetkellä nimet tallennetaan pienellä kirjoittaen.

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
- On olemassa sivu ja linkit joissa käyttäjä pääsee muokkaamaan reseptejään
- Käyttäjä voi järjestää reseptilistaa (aika, suosio, ainesten määrä)

#### Loppupalautus: Viimeistely
- Listan järjestys reseptit-sivulla toimii
- Uuden käyttäjätunnuksen luomisen ongelmat on korjattu
- CSRF-haavoittuvuus on poistettu
- Tagien lisäys, muokkaus ja poisto toimii
- Reseptin muokkaus toimii
- Reseptille annetut virhesyötteet eivät kaada sivua.
- Syötteet tarkistetaan, kriittisimmät virheet aiheuttavat erillisen virheviestin
  - Muut virheet hylätään html-pohjan input-kentän rajoitusten avulla
- Haku ja sisäänkirjautuminen toimii kirjainkoosta välittämättä
- Hakuun syötetty sana saa nyt esiintyä myös vain osamerkkijonona
- Tagit on esitettyinä reseptit-sivulla, sekä niihen liitetyn reseptin sivulla
- Reseptin tekijä näkee reseptin sivulla napin josta pääsee muokkaamaan reseptiä
- Kirjautuneelle käyttäjälle on lisätty navigointipalkki josta pääsee siirtymään eri toimintoihin
- Sivujen muotoilut on päivitetty
- Koodia on siistitty

