from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember_me = BooleanField('Angemeldet Bleiben')
    submit = SubmitField('Anmelden')

class EditProfileForm(FlaskForm):
    firstname = StringField('Vorname')
    surname = StringField('Nachname')
    text_area = TextAreaField('Über mich')
    school_year = SelectField('Klasse' , choices=[(7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])
    submit = SubmitField('Änderungen Übernehmen')

class RegistrationForm(FlaskForm):
    firstname = StringField('Vorname', validators=[DataRequired()])
    surname = StringField('Nachname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Passwort', validators=[DataRequired()])   
    school_year = SelectField('Klasse' , choices=[(7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])
    subject_latin = BooleanField('Latein')
    subject_math = BooleanField('Mathe')
    subject_english = BooleanField('Englisch')
    submit = SubmitField('Registrieren')

class Nav(FlaskForm):
    dropdown = SelectField('Dropdown', choices=[(0, '' ), (1, 'Profil'), (2, 'News'), (3, 'Abmelden')])