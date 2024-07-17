from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    #  Project settings

    app.config.from_mapping(
        DEBUG=True, SECRETE_KEY="dev", SQLALCHEMY_DATABASE_URI="sqlite:///todoList.db"
    )

    db.init_app(app)

    # Blueprint register

    from . import todo

    app.register_blueprint(todo.bp)

    from . import auth

    app.register_blueprint(auth.bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    # Migrar modelos a la base de datos
    with app.app_context():
        db.create_all()

    return app
