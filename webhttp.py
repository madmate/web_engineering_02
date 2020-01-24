from http.server import HTTPServer, BaseHTTPRequestHandler

count = 0

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global count
        count += 1
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(str(count),'utf-8'))

server_address = ('localhost', 80)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.serve_forever()