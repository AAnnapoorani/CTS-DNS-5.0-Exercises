from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from courses import courses_bp
from courses import models

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(
        courses_bp,
        url_prefix="/api"
    )
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)