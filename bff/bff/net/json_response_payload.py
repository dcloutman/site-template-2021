from flask import jsonify, make_response
from .. net.http_response_codes import HTTPResponseCodes
"""
Generates a JSON response payload with the following members:
    data: Jsonified data that is being passed to the client for parsing and consumption. Use data from this field for your standard logic flows.
    error_code: Internal error codes defined by your application's protocol. Use these to control client error handling.
    error_trace: A place for attaching server-side stack traces. This should only be used in development and debugging. Do not send stack traces to the client in production.
    message: A human readable message regarding the application's state. The content of this field should not be parsed, modified, or used to create logic flows in the client application. Do not store application data or stack traces in this field. Use the `data` field instead to pass parseable data to the client instead.  
"""


class JsonResponsePayload():
    _payload = None

    def __init__(self, data=None, error_code=None, error_trace=None, message=""):
        _payload = self.generate_empty_payload()
        self._payload["data"] = data

        if type(error_code) in ["str", "int"]:
            self._payload["error_code"] = error_code
        else:
            raise TypeError("The error_code member in the response payload should be a string or integer")

        # Stack traces should not be sent when debugging is turned off.
        if 'FLASK_DEBUG' in os.environ and os.environ['FLASK_DEBUG'] == 1 and "str" == type(error_trace):
            self._payload["error_trace"] = error_trace

        if "str" == type(message):
            self._payload["message"] = message
        else:
            raise TypeError("Message must be a string.")

    def get_payload(self):
        return self._payload

    def get_json_payload(self):
        """
        Returns a json string payload.
        """
        return jsonify(self._payload)

    def get_json_response(self, response_code = HTTPResponseCodes.OK):
        """
        Returns a JSON formatted Flask response.
        """
        return make_response(jsonify(_payload), response_code)

    def _generate_empty_payload(self):
        """
        Generates the payload dictionary internally.
        """
        return {
            "error_code" : None,
            "error_trace" : None,
            "message" : "",
            "data" : None
        }
