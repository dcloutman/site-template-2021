from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class EmailSignupLightboxForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="Email required."), Email(granular_message=True)])
    