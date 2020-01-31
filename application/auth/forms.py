from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.length(min=3)])
    password = PasswordField("Salasana", [validators.length(min=3)])
  
    class Meta:
        csrf = False

#uusien käyttäjien tekemiseen
class SignInForm(FlaskForm):
    name = StringField("Anna nimesi", [validators.length(min=3)])
    username = StringField("Keksi käyttäjätunnus", [validators.length(min=3)])
    password = PasswordField("Keksi salasana", [validators.length(min=3)])

    class Meta:
        csrf = False