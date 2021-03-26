"""
server.py
Example server that can respond to specific get requests and dynamically assign port numbers
"""

import sys
import json
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
import sqlite3


def SimpleServer(ServerClass=BaseHTTPServer.HTTPServer):
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
            except ValueError:
                host = sys.argv[1]

    server_address = (host, port)

    class Handler(SimpleHTTPRequestHandler):
        def setup(self):
            SimpleHTTPRequestHandler.setup(self)
            self.request.settimeout(60)

        def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

        def do_GET(self):
            if self.path == "/api/v1/status/":
                # For the very specific request/path print back a message in json
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()

                # Here you could do all sorts of python scripting to produce a different return response
                # e.g. run a SELECT Query on your sqlite database and return some formatted json packet with the data

                self.wfile.write(json.dumps({'message': 'API Available'}))
                return
            else:
                # Else, let the underlying server handle the request as usual
                return SimpleHTTPRequestHandler.do_GET(self)

        def do_POST(self):
            request_headers = self.headers
            content_length = request_headers.getheaders('content-length')
            length = int(content_length[0]) if content_length else 0

            # Let's assume and extract some json data from the request
            jsonData = self.rfile.read(length)
            record = jsonData
            data = json.loads(record)

            # Connect to the database file
            conn = sqlite3.connect("sample.db")
            try:
                cur = conn.cursor()
                # Generally, we shouldn't assume this data is non-malicious but here we are...
                message = data['message']
                cur.execute('INSERT INTO Log (log_message) VALUES (?)', [message])
                conn.commit()

            except Exception as e:
                print('There was some kind of error:\n\n' + str(e))
            finally:
                conn.close()

            # Tell the request we did something
            self.send_response(200)
            self.send_header("Content-type", "application/javascript")
            self.end_headers()

    httpd = ServerClass(server_address, Handler)

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()


if __name__ == "__main__":
    SimpleServer()
