from flask import Flask
app = Flask(__name__) #muuttuja app viittaa Flaskiin

from application import views #views.py sisältö ladataan käyttöön sovelluksen käynnistyessä