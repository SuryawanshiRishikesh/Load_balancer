from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		self.wfile.write(b"Response from Server 3")

if __name__ == "__main__":
	server = HTTPServer(("10.0.2.15", 8083), SimpleHandler)
	print("Server 3 running on port 8083")
	server.serve_forever()
