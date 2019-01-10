from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    password = StringField('Passwort', validators=[DataRequired()])
    remember_me = BooleanField('Angemeldet Bleiben')
    submit = SubmitField('Anmelden')

class EditProfileForm(FlaskForm):
    firstname = StringField('Vorname')
    surname = StringField('Nachname')
    text_area = TextAreaField('Über mich')
    school_year = SelectField('Klasse' , choices=[(7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])
    submit = SubmitField('Änderungen Übernehmen')
