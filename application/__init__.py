#Tuodaan Flask kayttoon
from flask import Flask
app = Flask(__name__) #muuttuja app viittaa Flaskiin

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
# Käytetään books.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

 #views.py sisältö ladataan käyttöön sovelluksen käynnistyessä
from application import views

#tuodaan luokka käyttöön
from application.books import models
from application.books import views

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()