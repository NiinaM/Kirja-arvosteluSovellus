from flask import render_template # views.py ohjeistaa Flaskia käsittelemään jokaisen sovelluksen juuripolkuun / tulevan pyynnön, että käyttäjälle näytetään tiedoston index.html sisält
from application import app
from application.auth.models import User

@app.route('/')
def index():
    return render_template("index.html", needs_books=User.find_users_with_who_have_not_read_any_books())