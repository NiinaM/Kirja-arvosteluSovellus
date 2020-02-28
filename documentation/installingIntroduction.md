# Asennusohje

### Asenna nämä ennen kumpaakin tapaa käyttää sovellusta
* pythonin 3 jokin versio
* pip
* sqlite3

### Sovellus toimimaan paikallisesti

* Ensin lataa tai kloonaa projektin repositorio githubista.
* Sitten luo ja aktivoi virtuaaliympäristö `venv`.

`python -m venv venv`
`source venv/bin/activate`

* Nyt asenna sovelluksen riippuvuudet `pip install -r requirements.txt`

* Aja sovellus kirjoittamalla `python run.py`

* Sovelluksen paikallista testiversiota voi käyttää osoitteessa http://localhost:5000.

### Sovellus toimimaan Herokussa

* Asenna ensin Herokun CLI-työkalut.
* Aja sitten komentoriviltä projektin kansiosssa `heroku create <nimi>` luodaksesi näin projektin Herokuun.
* Halutessassasi voit käyttää Herokussa Postgress-tietokantaa.
* Asenna ensin Postgress liitännäinen Herokussa ja aseta sitten asetuksissa ympäristömuuttujat:
`HEROKU=1`
`DATABASE_URL=osoite postgreskantaan`