from flask import current_app, render_template
from .. forms.email_signup_lightbox_form import EmailSignupLightboxForm

def render_standard_nonauthorized(template_name, insert_email_lightbox=True, template_vars={}):
    if not type(template_vars) is dict:
        raise TypeError("`template_vars` must be a dictionary")

    if insert_email_lightbox:
        email_lightbox_form = EmailSignupLightboxForm()
        return render_template(template_name, email_lightbox_form=email_lightbox_form, **template_vars)
    else:
        return render_template(template_name, email_lightbox_form=None, **template_vars)


def render_standard_authorized (template_name, template_vars={}):
    pass

def render_lite_nonauthorized (template_name, template_vars={}):
    pass

def render_lite_authorized (template_name, template_vars={}):
    pass