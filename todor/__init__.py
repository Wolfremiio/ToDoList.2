from flask import Flask


def create_app():
    app = Flask(__name__)

    #  Project settings

    app.config.from_mapping(DEBUG=True, SECRETE_KEY="dev")

    # Blueprint register

    from . import todo

    app.register_blueprint(todo.bp)

    from . import auth

    app.register_blueprint(auth.bp)

    @app.route("/")
    def index():
        return "Hola Mundo"

    return app
