from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Benutzername", validators=[DataRequired()])
    password = StringField('Passwort', validators=[DataRequired()])
    remember_me = BooleanField('Angemeldet Bleiben')
    submit = SubmitField('Anmelden')
