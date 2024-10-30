import sys

sys.path.append("/code/src")  # noqa

from flask import Flask
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from settings import config
from extensions import db
from blueprints.orders import bp as orders_bp


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True
    )
    app.config.from_object(config)
    app.register_blueprint(orders_bp)
    db.init_app(app)
    return app, db


app, db = create_app()
migrate = Migrate(app, db)

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

if not database_exists(engine.url):
    create_database(engine.url)
    print(f"Database 'quicktask' created.")


if __name__ == '__main__':
    app.run(debug=True)

    
    
    