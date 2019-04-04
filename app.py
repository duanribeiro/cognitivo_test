from flask import Flask
from sqlalchemy_utils import database_exists, create_database
from apis.api import blueprint

def create_app():
    app = Flask(__name__)


    from models.model import db
    db.init_app(app)
    # db.create_all()


    app.config.from_object('config.DevelopConfig')

    app.register_blueprint(blueprint)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port='5000', debug=True)
