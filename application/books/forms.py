from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class BookForm(FlaskForm):
    name = StringField("Kirjan nimi", [validators.length(min=3, max=30), validators.DataRequired()])
    read = BooleanField("Luettu")

    class Meta:
        csrf = False

class BookUpdateForm(FlaskForm):
    updated_name = StringField("Muokkaa kirjan nimeä", [validators.length(min=3, max=30), validators.DataRequired()])

    class Meta:
        csrf = False