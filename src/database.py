import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        create_tables()

def create_tables():
    with db.engine.connect() as connection:
        with open(os.path.join(os.path.dirname(__file__), 'database', 'schema.sql'), 'r') as file:
            schema = file.read()
        statements = schema.split(';')
        for statement in statements:
            if statement.strip():
                try:
                    connection.execute(text(statement))
                except Exception as e:
                    print(f"Error executing statement: {statement}\n{e}")

def get_db_session():
    return db.session