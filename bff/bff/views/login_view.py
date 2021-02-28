from flask import make_response, current_app, render_template, url_for, jsonify, request
from flask_classful import FlaskView, route
from .. net.http_response_codes import HTTPResponseCodes
from os import environ
import json
import requests

class LoginView(FlaskView):
    route_prefix = '' # Could be used to set a configurable site path using os.environ. Need config system.
    route_base = '/login'

    def after_request(self, name, response):
        return response

    def post(self):
        return HTTPResponseCodeConstants.FORBIDDEN, HTTPResponseCodes.FORBIDDEN
