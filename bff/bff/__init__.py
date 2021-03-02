from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

"""
Initialize app and db globals.
"""
LIBARY_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT =  os.path.join(LIBARY_PATH, os.pardir)
STATIC_PATH = os.path.join(os.pardir, "static")

app = Flask(__name__, template_folder=os.path.join(PROJECT_ROOT, "templates"), static_folder=STATIC_PATH)

def initialize_db(app):
    # Get database config.
    db_username = ''
    if 'DB_USERNAME' in os.environ:
        db_username = os.environ['DB_USERNAME']

    db_password = ''
    if 'DB_PASS' in os.environ:
        db_password = os.environ['DB_PASS']

    db_host = ''
    if 'DB_HOST' in os.environ:
        db_host = os.environ['DB_HOST']

    db_name = ''
    if 'DB_NAME' in os.environ:
        db_name = os.environ['DB_NAME']


    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_username}:{db_password}@{db_host}/{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Run initialization in private namespace.
initialize_db(app)
db = SQLAlchemy(app)
