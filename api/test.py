from http.server import BaseHTTPRequestHandler
from utils.helper import randomString


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = randomString()
        self.wfile.write(message.encode())
        return
