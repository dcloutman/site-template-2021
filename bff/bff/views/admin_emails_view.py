from flask import make_response, current_app, render_template, url_for, jsonify, request
from flask_classful import FlaskView, route
from .. net.http_response_codes import HTTPResponseCodes
from os import environ


class AdminEmailsView(FlaskView):
    route_prefix = '' # Could be used to set a configurable site path using os.environ. Need config system.
    route_base = '/admin/emails'

    def after_request(self, name, response):
        return response

    def index(self):
        all_emails = ['f392039@example.com', 'fxx9@example.com']
        return render_template("admin_emails_view.jinja", all_emails=all_emails), HTTPResponseCodes.OK

    def post(self):
        return HTTPResponseCodes.INTERNAL_SERVER_ERROR

    #def get(self):
    #	return HTTPResponseCodes.NOT_IMPLEMENTED
