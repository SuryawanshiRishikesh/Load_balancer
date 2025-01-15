from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		self.wfile.write(b"Response from Server 2")

if __name__ == "__main__":
	server = HTTPServer(("10.0.2.15", 8082), SimpleHandler)
	print("Server 2 running on port 8082")
	server.serve_forever()
