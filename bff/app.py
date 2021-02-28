from flask import render_template
from bff import app
from bff import db

from bff.views.home_view import HomeView
from bff.views.contact_view import ContactView
from bff.views.about_view import AboutView
from bff.views.icons_view import IconsView
from bff.views.login_view import LoginView


# Register view classes with the Flask app.
HomeView.register(app)
ContactView.register(app)
AboutView.register(app)
IconsView.register(app)
LoginView.register(app)

@app.route('/products')
def products():
    return "Products"
 

@app.route('/login')
def login():
    return "Login"

if __name__ == "app.py":
    app.run()

