from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from courses import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from courses.routes import courses_bp
    app.register_blueprint(courses_bp)

    from courses import models

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)