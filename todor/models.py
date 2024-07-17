from todor import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)


def _init_(self, userName, password):
    self.userName = userName
    self.password = password


def _repr_(self):
    return f"<User: {self.username}> "
