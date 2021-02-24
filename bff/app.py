from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from bff.views.home_view import HomeView
from bff.views.contact_view import ContactView
from bff.views.about_view import AboutView
from bff.views.icons_view import IconsView

import smtplib

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template("home.jinja", show_page_aside=True)

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