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


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.models.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    state = db.Column(db.Boolean, default=False)


def _init_(self, created_by, title, desc, state=False):
    self.created_by = created_by
    self.title = title
    self.desc = desc
    self.state = state


def _repr_(self):
    return f"<Todo: {self.title}> "
