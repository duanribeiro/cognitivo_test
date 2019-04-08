from flask import Flask
from apis.api import blueprint
# from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)


    from models.model import db
    db.init_app(app)

    app.config.from_object('config.DevelopConfig')

    app.register_blueprint(blueprint)
    with app.app_context():
        db.create_all()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port='5000', debug=True)
