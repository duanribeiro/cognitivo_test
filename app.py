from flask import Flask
import pandas as pd
from apis.api import blueprint

def create_app():
    app = Flask(__name__)


    from models.model import db
    db.init_app(app)


    app.config.from_object('config.DevelopConfig')

    app.register_blueprint(blueprint)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True)
