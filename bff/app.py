from flask import Flask, render_template
import smtplib

app = Flask(__name__)

@app.route('/')
def home ():
	return render_template("home.jinja", page_headline="Site Template 2021", show_page_aside=True)

@app.route('/about')
def about():
	return render_template("about.jinja", page_headline="About Us")

@app.route('/contact')
def contact():
	return render_template("contact.jinja", page_headline="Contact Us")

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