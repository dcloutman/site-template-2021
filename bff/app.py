from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import smtplib

app = Flask(__name__)

@app.route('/')
def home ():
	return render_template("home.jinja", page_headline="Site Template 2021", show_page_aside=True)

@app.route('/about')
def about():
	return render_template("about.jinja", page_headline="About Us")

@app.route('/contact', methods=['GET'])
def contact():
	return render_template("contact.jinja", page_headline="Contact Us")

@app.route('/contact', methods=['POST'])
def contact_process_form():
	return '0'

@app.route('/contact/send-message')
def send_message():
	return "Send message."
	
@app.route('/products')
def products():
	return "Products"

@app.route('/login')
def login():
	return "Login"

if __name__ == "app.py":
	app.run()