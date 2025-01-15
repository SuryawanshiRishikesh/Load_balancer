from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		self.wfile.write(b"Response from Server 1")

if __name__ == "__main__":
	server = HTTPServer(("10.0.2.15", 8081), SimpleHandler)
	print("Server 1 running on port 8081")
	server.serve_forever()
