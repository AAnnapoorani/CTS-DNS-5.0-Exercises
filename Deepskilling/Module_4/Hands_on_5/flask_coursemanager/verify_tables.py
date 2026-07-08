from app import app
from app import db

with app.app_context():

    inspector = db.inspect(db.engine)

    print(
        inspector.get_table_names()
    )
    