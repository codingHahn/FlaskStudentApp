from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True)
    surname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))

    has_english = db.Column(db.Boolean, index=True)
    has_latin = db.Column(db.Boolean, index=True)
    has_math = db.Column(db.Boolean, index=True)

    #name = db.Column(db.String(64))
    #surname = db.Column(db.String(64))

    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.id)    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
