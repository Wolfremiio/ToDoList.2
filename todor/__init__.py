from flask import Flask


def create_app():
    app = Flask(__name__)

    #  Project settings

    app.config.from_maping(
        DEBUG=True,
        secret_key="dev",
    )

    @app.route("/")
    def index():
        return "Hola Mundo"

    return app