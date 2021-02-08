from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home ():
	return render_template("home.jinja", page_headline="Site Template 2021")

@app.route('/about')
def about():
	return "About"

@app.route('/contact')
def contact():
	return "Contact"

@app.route('/products')
def products():
	return "Products"

if __name__ == "app.py":
	app.run()