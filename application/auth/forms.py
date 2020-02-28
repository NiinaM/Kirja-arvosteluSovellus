from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from application.auth.models import User
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.length(min=3, max=15), validators.DataRequired()])
    password = PasswordField("Salasana", [validators.length(min=6, max=20), validators.DataRequired()])

    class Meta:
        csrf = False

class SignInForm(FlaskForm):
    name = StringField("Anna nimesi", [validators.length(min=3, max=15), validators.DataRequired()])
    username = StringField("Uusi käyttäjätunnus", [validators.length(min=3, max=15), validators.DataRequired()])
    password = PasswordField("Uusi salasana", [validators.length(min=6, max=20), validators.DataRequired(), validators.EqualTo('confirm_password', message='Salasanojen pitää täsmätä.')])
    confirm_password = PasswordField("Toista salasana", [validators.DataRequired(), validators.length(min=6, max=20)])

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
    
    def validate(self):
        initial_validation = super(SignInForm, self). validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Käyttäjätunnus on jo olemassa!")
            return False
        return True


    class Meta:
        csrf = False