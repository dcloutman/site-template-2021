from flask import make_response, current_app, url_for, jsonify, request
from flask_classful import FlaskView, route
from .. net.http_response_codes import HTTPResponseCodes
from .. util.render_helpers import render_standard_nonauthorized
from os import environ
import json
import requests

class AboutView(FlaskView):
    route_prefix = '' # Could be used to set a configurable site path using os.environ. Need config system.
    route_base = '/about'

    def after_request(self, name, response):
        return response

    def index(self):
        return render_standard_nonauthorized("about.jinja", template_vars={"show_page_aside": False, "hide_page_header": False}), HTTPResponseCodes.OK
