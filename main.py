#testing an HTTP web server based on a python script

from http.server import HTTPServer, BaseHTTPRequestHandler


HOST = "192.168.1.12"
PORT = 5000

class MyHTTPhandler(BaseHTTPRequestHandler):

    #This method handles a GET request
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        htmlText = """
        <html><body>
		<H1> HELLO HAMZA </h1>
		</body></html>
        """
        self.wfile.write(bytes(htmlText,"utf-8"))

print('Starting the web server.')

server = HTTPServer((HOST, PORT), MyHTTPhandler)
print('Server now running ..')

server.serve_forever()
server.server_close()

print('Server stopped.')
