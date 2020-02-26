from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, HiddenField

class ReviewForm(FlaskForm):
    rating = IntegerField("Arvosana väliltä 1-10", [validators.NumberRange(min=1, max=10), validators.DataRequired()])
    reviewText = StringField("Kirjoita arvostelu", [validators.length(min=4, max=144), validators.DataRequired()])
    book_id = HiddenField()

    class Meta: 
        csrf = False