from http import server
from http.server import HTTPServer,BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.path.encode()) # for the echo server
        # self.wfile.write(bytes("<html><body><h1>PYTHON TEST MESSAGE</h1></body>></html>","utf-8"))        


def main():
    PORT = 8000
    server = HTTPServer(('',PORT),Handler)
    print('Server running on %s' % PORT)
    server.serve_forever()
    server.server_close()

if __name__ == '__main__':
    main()