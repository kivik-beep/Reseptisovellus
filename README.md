# Reseptisovellus
*Aineopintojen harjoitustyö: Tietokantasovellus (Tsoha)*

Sovellus löytyy osoitteesta
https://polar-hamlet-77249.herokuapp.com/

Sovellus sisältää reseptejä, joita voi hakutoiminnolla etsiä ainesosan tai ruuan tyypin perusteella (keitto, kasvisruoka, jälkiruoka jne.). Reseptit ovat kaikkien luettavissa, mutta kirjautumalla sisään käyttäjä saa lisätoimintoja käyttöönsä. Alla eri käyttäjäroiminnot eriteltynä.

### Käyttäjätyypit
#### Ei kirjautunut käyttäjä voi
- luoda uuden käyttäjätunnuksen
- lukea reseptejä
- käyttää perushakua reseptinetsintään

#### Kirjautunut käyttäjä voi lisäksi
- kirjautua sisään 
- lisätä uusia reseptejä
- ehdottaa muokkausta tai ilmiantaa olemassaolevaan reseptiin
- merkitä olemassa olevan reseptin suosikkeihin
- voi lisätä "omat ainekset" ja hakea resepteistä niitä, joihin löytyy ainekset valmiiksi
- voi muokata "omia aineksia" vapaasti

#### Ylläpitäjä voi edellämainittujen lisäksi
- käsitellä muokkausehdotuksia, eli muokata olemassaolevaa ohjetta
- poistaa ohjeita
- lisätä uuden ylläpitäjän 


### Resepti
Reseptin tulee sisältää ainakin seuraavat tiedot:
- uniikki nimi
- montako annosta resseptistä tulee
- ainesosalista 
- valmistusohje
- ruuan tyyppi

Suositeltavia reseptin tietoja on lisäksi
- valmistusaika (aktiivinen/passiivinen), käyttäjän lisättävissä

### Ideoita jatkokehitykseen
- Suunnitelmissa on syöttää kotona olevista aineksista alkuun vain tuotteet ilman määriä. Mikäli aikaa jää, toteutan omiin aineksiin mahdollisuuden lisätä ainesosien määrät.
- Reseptin annosmäärän muuttaminen - ainesosalistan ainesosien määrät muuttuvat kun valikosta muutetaan annosmäärää
- Ylläolevien toteutuksen jäälkeen on mahdollista lisätä omien ainesten hakuun valinta montako annosta kyseistä ruokaa pitäisi saada
- Reseptien järjestäminen sen mukaan, mihin löytyy parhaiten aineksia valmiiksi
- Reseptiä voisi olla mahdollista kommentoida, ja suosikkimerkintöjen määrä voisi lukea reseptisivulla
- Reseptiin voisi lisätä kuvan ja/tai esittelytekstin
- Reseptisivulla voisi näkyä suosikkimerkintöjen määrä

### Palautusten sisältötavoitteet
Välipalautus 1: vain suunnitelma. 

Välipalautus 2: mahdollisimman paljon käyttäjien ja reseptien ominaisuuksia

Välipalautus 3: käyttäjien ja reseptien ominaisuudet valmiiksi, sekä toivottavasti jotain jatkokehityslistan - ominaisuuksia mukaan.

Loppupalautus: viimeistely, eli mahdollisimman eheä ja hyvin toimiva ohjelma valmiiksi.
