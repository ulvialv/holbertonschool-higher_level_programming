#!/usr/bin/python3
"""
A simple HTTP server API using Python's http.server module.
This server handles multiple endpoints and serves JSON data.
"""

import http.server
import socketserver
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler that serves different endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests for different endpoints.
        """
        if self.path == '/':
            # Root endpoint - serve simple text response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            # Data endpoint - serve JSON data
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Sample dataset
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            # Convert dictionary to JSON string and encode to bytes
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == '/status':
            # Status endpoint - return OK
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            # Info endpoint - serve API information
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            json_info = json.dumps(info)
            self.wfile.write(json_info.encode('utf-8'))

        else:
            # Handle undefined endpoints - 404 Not Found
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            error = {
                "error": "Endpoint not found"
            }

            json_error = json.dumps(error)
            self.wfile.write(json_error.encode('utf-8'))


def run_server(port=8000):
    """
    Start the HTTP server on the specified port.

    Args:
        port (int): Port number to run the server on (default: 8000)
    """
    with socketserver.TCPServer(("", port), SimpleAPIHandler) as httpd:
        print(f"Server running on port {port}...")
        print(f"Access it at http://localhost:{port}")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
