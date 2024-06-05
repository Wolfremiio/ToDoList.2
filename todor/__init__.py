from flask import Flask


def create_app():
    app = Flask(__name__)

    #  Project settings

    app.config.from_mapping(DEBUG=True, SECRETE_KEY="dev")

    # Blueprint register

    @app.route("/")
    def index():
        return "Hola Mundo"

    return app
