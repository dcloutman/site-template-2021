from bff import app # Triggers the bff/__init__.py

from bff.views.home_view import HomeView
from bff.views.contact_view import ContactView
from bff.views.about_view import AboutView
from bff.views.icons_view import IconsView
from bff.views.login_view import LoginView
from bff.views.admin_emails_view import AdminEmailsView
from bff.views.admin_email_lists_view import AdminEmailListsView

"""
See bff/__init__.py for the initialization of `app` and the importation of application
configurations. This allow the libraries to share the app variable, which is where most
of the interesting stuff happens. The directory bff/views contains view controllers 
written using the excellent Flask Classful library, which nicely structures the
`@app.route` functions usually found in this file into classes with methods for each
HTTP method.
"""

# Register view classes with the Flask app.
HomeView.register(app)
ContactView.register(app)
AboutView.register(app)
IconsView.register(app)
LoginView.register(app)
AdminEmailsView.register(app)
AdminEmailListsView.register(app)

@app.route('/products')
def products():
    return "Products"
 

@app.route('/login')
def login():
    return "Login"

if __name__ == "app.py":
    app.run()

