class HTTPResponseCodes:
    """
    HTTP Constants
    """
    # The request has succeeded.
    OK = 200

    # The request has succeeded and a new resource has been created as a result.
    CREATED = 201

    # The request has been received but not yet acted upon. Intended for cases where another process or server handles the request, or for batch processing.
    ACCEPTED = 202

    # There is no content to send for this request, but the headers may be useful.
    NO_CONTENT = 204

    # The URL of the requested resource has been changed permanently.
    MOVED_PERMANENTLY = 301

    # Used for temporary redirects. This response code means that the URI of requested resource 
    # has been changed temporarily.
    MOVED_TEMPORARILY = 302

    # This is used for caching purposes. It tells the client that the response has not been 
    # modified, so the client can continue to use the same cached version of the response.
    NOT_MODIFIED = 304

    # 305 is deprecated.
    # 306 is no longer used, but reserved.

    # The server sends this response to direct the client to get the requested resource at
    # another URI with same method that was used in the prior request. This has the same 
    # semantics as the 302 Found HTTP response code, with the exception that the user agent
    # must not change the HTTP method used: If a POST was used in the first request, a POST
    # must be used in the second request.
    TEMPORARY_REDIRECT = 307

    # This means that the resource is now permanently located at another URI, specified by 
    # the Location: HTTP Response header. This has the same semantics as the 301 Moved Permanently
    # HTTP response code, with the exception that the user agent must not change the HTTP method 
    # used: If a POST was used in the first request, a POST must be used in the second request.
    PERMANENT_REDIRECT = 308 


    # The server could not understand the request due to invalid syntax.
    BAD_REQUEST = 400

    # Although the HTTP standard specifies "unauthorized", semantically this response means 
    # "unauthenticated". That is, the client must authenticate itself to get the requested response.
    UNAUTHORIZED = 401

    # The client does not have access rights to the content; that is, it is unauthorized, so the server
    # is refusing to give the requested resource. Unlike 401, the client's identity is known to the server.
    FORBIDDEN = 403

    # The server can not find requested resource. In the browser, this means the URL is not recognized. In 
    # an API, this can also mean that the endpoint is valid but the resource itself does not exist. 
    # Servers may also send this response instead of 403 to hide the existence of a resource from an 
    # unauthorized client. This response code is probably the most famous one due to its frequent 
    # occurrence on the web.
    NOT_FOUND = 404

    # The request method is known by the server but has been disabled and cannot be used. For example,
    # an API may forbid DELETE-ing a resource. The two mandatory methods, GET and HEAD, must never be
    # disabled and should not return this error code.
    METHOD_NOT_ALLOWED = 405

    # This response is sent when the web server, after performing server-driven content negotiation, 
    # doesn't find any content that conforms to the criteria given by the user agent.
    NOT_ACCEPTABLE = 406

    # This is similar to 401 but authentication is needed to be done by a proxy.
    PROXY_AUTHENTICATION_REQUIRED = 407

    # This response is sent on an idle connection by some servers, even without any previous request
    # by the client. It means that the server would like to shut down this unused connection. This 
    # response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP 
    # pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the 
    # connection without sending this message.
    REQUEST_TIMEOUT = 408

    # This response is sent when a request conflicts with the current state of the server. (Huh?)
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    PAYLOAD_TOO_LARGE = 413
    URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417

    # "I'm a teapot". Barf.-
    TEAPOT = 418
    MISDIRECTED_REQUEST = 421 
    UNPROCESSABLE_ENTITY_WEBDAV = 422
    LOCKED_WEBDAV = 423
    FAILED_DEPENDENCY_WEBDAV = 424
    TOO_EARLY = 425
    UPGRADE_REQUIRED = 426
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451


    # The server has encountered a situation it doesn't know how to handle.
    INTERNAL_SERVER_ERROR = 500

    # The request method is not supported by the server and cannot be handled. The 
    # only methods that servers are required to support (and therefore that must not
    # return this code) are GET and HEAD.
    NOT_IMPLEMENTED = 501

    # The server has encountered a situation it doesn't know how to handle.
    BAD_GATEWAY = 502

    # The server is not ready to handle the request. Common causes are a server
    # that is down for maintenance or that is overloaded. Note that together with
    # this response, a user-friendly page explaining the problem should be sent. This
    # responses should be used for temporary conditions and the Retry-After: HTTP 
    # header should, if possible, contain the estimated time before the recovery of the
    # service. The webmaster must also take care about the caching-related headers that
    # are sent along with this response, as these temporary condition responses should 
    # usually not be cached.
    SERVICE_UNAVAILABLE = 503

    # This error response is given when the server is acting as a gateway and cannot get
    # a response in time.
    GATEWAY_TIMEOUT = 504

    # The HTTP version used in the request is not supported by the server.
    HTTP_VERSION_NOT_SUPPORTED = 505

    # The server has an internal configuration error: the chosen variant resource is 
    # configured to engage in transparent content negotiation itself, and is therefore not
    # a proper end point in the negotiation process.
    VARIANT_ALSO_NEGOTIATES = 506

    # The method could not be performed on the resource because the server is unable to
    # store the representation needed to successfully complete the request.
    INSUFFICIENT_STORAGE_WEBDAV = 507

    # The server detected an infinite loop while processing the request.
    LOOP_DETECTED_WEBDAV = 508

    # Further extensions to the request are required for the server to fulfill it.
    NOT_EXTENDED = 510

    # The 511 status code indicates that the client needs to authenticate to gain network access.
    NETWORK_AUTHENTICATION_REQUIRED = 511
