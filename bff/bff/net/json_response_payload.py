from flask import jsonify, make_response
"""
Generates a JSON response payload with the following members:
    data: Jsonified data that is being passed to the client for parsing and consumption. Use data from this field for your standard logic flows.
    error_code: Internal error codes defined by your application's protocol. Use these to control client error handling.
    error_trace: A place for attaching server-side stack traces. This should only be used in development and debugging. Do not send stack traces to the client in production.
    message: A human readable message regarding the application's state. The content of this field should not be parsed, modified, or used to create logic flows in the client application. Do not store application data or stack traces in this field. Use the `data` field instead to pass parseable data to the client instead.  
"""


class JsonResponsePayload:
    _payload = None

    def __init__(self, data=None, error_code=None, error_trace=None, message=""):
        _payload = self.generate_empty_payload()
        self._payload["data"] = data
        self._payload["error_code"] = error_code

        # TODO: Disable when debug is turned off.
        self._payload["error_trace"] = error_trace

        if "str" == type(message):
            self._payload["message"] = message
        else:
            raise TypeError("Message must be a string.")

    def get_payload(self):
        return self._payload

    def get_json_payload(self):
        """
        Returns a json stringpayload.
        """
        pass

    def get_json_response(self, response_code = 200):
        """
        Returns a JSON formatted Flask response.
        """
        pass

    def _generate_empty_payload(self):
        return {
            "error_code" : None,
            "error_trace" : None,
            "message" : "",
            "data" : None
        }