from flask import make_response, current_app, url_for, jsonify, request
from flask_classful import FlaskView, route
from .. net.http_response_code_constants import HTTPResponseCodeConstants
from os import environ
import json
import requests

class ContactView(FlaskView):
    route_prefix = '/contact'
    route_base = ''

def after_request(self, name, response):
	return response

def index(self):
	return 