"""
server.py
Example server that can respond to specific get requests and dynamically assign port numbers
"""

import sys
import json
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer


def SimpleServer(HandlerClass=SimpleHTTPRequestHandler, ServerClass=BaseHTTPServer.HTTPServer):
    protocol = "HTTP/1.0"
    host = ''
    port = 8080
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if ':' in arg:
            host, port = arg.split(':')
            port = int(port)
        else:
            try:
                port = int(sys.argv[1])
            except:
                host = sys.argv[1]

    server_address = (host, port)

    #HandlerClass.protocol_version = protocol
    class Handler(SimpleHTTPRequestHandler):
        def setup(self):
            SimpleHTTPRequestHandler.setup(self)
            self.request.settimeout(60)

        def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_GET(self):
            if self.path=="/api/v1/status/":
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
            	self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'API Available'}))
            	return
            else:
                return SimpleHTTPRequestHandler.do_GET(self)

        def do_POST(self):
            request_path = self.path
            print("\n----- Request Start ----->\n")


    httpd = ServerClass(server_address, Handler)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == "__main__":
    SimpleServer()
