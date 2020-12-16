#python t80.py
#Web server ... tests ...
#2-4-2016
#from http.server import BaseHTTPServer.HTTPServer#, BaseHTTPServer.BaseHTTPRequestHandler
import http.server

#no...
def run_while_true(server_class=BaseHTTPServer.HTTPServer,
                   handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    """
    This assumes that keep_running() is a function of no arguments which
    is tested initially and after each request.  If its return value
    is true, the server continues.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    while keep_running():
        httpd.handle_request()

		
run_while_true()