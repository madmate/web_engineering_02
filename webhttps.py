from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

count = 0

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global count
        count += 1
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(str(count),'utf-8'))

server_address = ('localhost', 443)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile="server.pem",
                               keyfile="key.pem",
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()