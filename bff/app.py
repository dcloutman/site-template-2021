from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from bff.views.contact_view import ContactView
import smtplib

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template("home.jinja", show_page_aside=True)

@app.route('/about')
def about():
    return render_template("about.jinja")

ContactView.register(app)

@app.route('/contact/send-message')
def send_message():
    return "Send message."

@app.route('/products')
def products():
    return "Products"

@app.route('/icons')
def icons():
    return render_template("icons.jinja")

@app.route('/login')
def login():
    return "Login"

if __name__ == "app.py":
    app.run()