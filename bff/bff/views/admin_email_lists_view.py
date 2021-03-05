from flask import make_response, current_app, render_template, url_for, jsonify, request
from flask_classful import FlaskView, route
from .. net.http_response_codes import HTTPResponseCodes
from .. models.email_lists import EmailList
from os import environ


class AdminEmailListsView(FlaskView):
    route_prefix = '' # Could be used to set a configurable site path using os.environ. Need config system.
    route_base = '/admin/email-lists'

    def after_request(self, name, response):
        return response

    def index(self):
        all_email_lists = EmailList.query.all()
        return render_template("admin_email_lists.jinja", all_email_lists=all_email_lists), HTTPResponseCodes.OK

    def post(self):
        return HTTPResponseCodes.INTERNAL_SERVER_ERROR

    #def get(self):
    #	return HTTPResponseCodes.NOT_IMPLEMENTED
