from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class ReviewForm(FlaskForm):
    rating = IntegerField("Arvosana väliltä 1-10", [validators.NumberRange(min=1, max=10)])
    reviewText = StringField("Kirjoita arvostelu")

    class Meta: 
        csrf = False