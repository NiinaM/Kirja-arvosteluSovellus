from flask import render_template # views.py ohjeistaa Flaskia käsittelemään jokaisen sovelluksen juuripolkuun / tulevan pyynnön, että käyttäjälle näytetään tiedoston index.html sisält
from application import app

@app.route("/")
def index():
    return render_template("index.html")