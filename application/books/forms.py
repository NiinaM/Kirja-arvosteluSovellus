from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class BookForm(FlaskForm):
    name = StringField("Kirjan nimi", [validators.length(min=3)])
    read = BooleanField("Luettu")

    class Meta:
        #turvautuminen cross-site request forgery -hyökkäyksiä vastaan kytketään pois päältä.
        csrf = False