from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import smtplib
from bff.views.home_view import HomeView
from bff.views.contact_view import ContactView
from bff.views.about_view import AboutView
from bff.views.icons_view import IconsView
import os

app = Flask(__name__)


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
if 'DB_NAME'  in os.environ:
    db_name = os.environ['DB_NAME']

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
db = SQLAlchemy(app)

# Register view classes with the Flask app.
HomeView.register(app)
ContactView.register(app)
AboutView.register(app)
IconsView.register(app)

@app.route('/products')
def products():
    return "Products"

#@app.route('/icons')
#def icons():
#    return render_template("icons.jinja")

@app.route('/login')
def login():
    return "Login"

if __name__ == "app.py":
    app.run()
