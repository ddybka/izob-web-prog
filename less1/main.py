import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer

class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path.endswith("/"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            output = """
            Hello World!
            """
            self.wfile.write(output.encode("utf8"))
            return

port = 8000
server = HTTPServer(('', port), WebServerHandler)
print("Сервер запущен на порту: " + str(port))
print("Для открытия в браузере используйте адрес: http://localhost:" + str(port))
server.serve_forever()
