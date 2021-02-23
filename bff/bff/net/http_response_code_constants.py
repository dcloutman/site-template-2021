class HTTPResponseCodeConstants:
    # HTTP Constants
    OK = 200 # The request has succeeded.
    CREATED = 201 # The request has succeeded and a new resource has been created as a result.
    ACCEPTED = 202 # The request has been received but not yet acted upon. Intended for cases where another process or server handles the request, or for batch processing.
    NO_CONTENT = 204 # There is no content to send for this request, but the headers may be useful.

    MOVED_PERMANENTLY = 301 # The URL of the requested resource has been changed permanently.
    MOVED_TEMPORARILY = 302 # Used for temporary redirects. This response code means that the URI of requested resource has been changed temporarily.
    NOT_MODIFIED = 304 # This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response.

    BAD_REQUEST = 400 # The server could not understand the request due to invalid syntax.
    UNAUTHORIZED = 401 # Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.
    FORBIDDEN = 403 # The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401, the client's identity is known to the server.
    NOT_FOUND = 404 # The server can not find requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 to hide the existence of a resource from an unauthorized client. This response code is probably the most famous one due to its frequent occurrence on the web.
    METHOD_NOT_ALLOWED = 405 # The request method is known by the server but has been disabled and cannot be used. For example, an API may forbid DELETE-ing a resource. The two mandatory methods, GET and HEAD, must never be disabled and should not return this error code.
    NOT_ACCEPTABLE = 406 # This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent.
    PROXY_AUTHENTICATION_REQUIRED = 407 # This is similar to 401 but authentication is needed to be done by a proxy.
    REQUEST_TIMEOUT = 408 # This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message.
