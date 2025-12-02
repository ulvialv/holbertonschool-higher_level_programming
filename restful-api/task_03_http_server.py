#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_reponse(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simle API!")

        elif self.path == "/data":
            sample_data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
            }
            json_data = json.dumps(sample_data).encode()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data)

 
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            info = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
            }
            json_info = json.dumps(info).encode()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_info)

        else:
            self.send_response(404)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
            
           
def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the API server on  port 8000."""
    server = server_class(("0.0.0.0" 8000), handler_class)
    print("Starting server on port 8000...")
    server.serve_forever()


if __name__ == "__main__":
    run()
