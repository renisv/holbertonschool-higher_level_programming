import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status_code=200, content_type='text/plain'):
        """Helper method to set HTTP headers"""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self._handle_root()
        elif self.path == '/data':
            self._handle_data()
        elif self.path == '/status':
            self._handle_status()
        elif self.path == '/info':
            self._handle_info()
        else:
            self._handle_not_found()

    def _handle_root(self):
        """Handle root endpoint"""
        response = "Hello, this is a simple API!"
        self._set_headers(200, 'text/plain')
        self.wfile.write(response.encode('utf-8'))

    def _handle_data(self):
        """Handle /data endpoint - serve JSON data"""
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        response = json.dumps(data)
        self._set_headers(200, 'application/json')
        self.wfile.write(response.encode('utf-8'))

    def _handle_status(self):
        """Handle /status endpoint - return API status"""
        response = "OK"
        self._set_headers(200, 'text/plain')
        self.wfile.write(response.encode('utf-8'))

    def _handle_info(self):
        """Handle /info endpoint - return API information"""
        info = {
            "version": "1.0",
            "description": "A simple API built with http.server"
        }
        response = json.dumps(info)
        self._set_headers(200, 'application/json')
        self.wfile.write(response.encode('utf-8'))

    def _handle_not_found(self):
        """Handle undefined endpoints"""
        error_message = "Endpoint not found"
        self._set_headers(404, 'text/plain')
        self.wfile.write(error_message.encode('utf-8'))

    def log_message(self, format, *args):
        """customize log format"""
        client_ip = self.client_address[0]
        timestamp = self.log_date_time_string()
        message = format % args
        print(f"{client_ip} - - [{timestamp}] {message}")


def run_server(port=8000):
    """Start the HTTP server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on port {port}")
    print("Available endpoints:")
    print("  GET /              - Welcome message")
    print("  GET /data          - Sample JSON data")
    print("  GET /status        - API status")
    print("  GET /info          - API information")
    print("\nPress Ctrl+C to stop the server")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server")
        httpd.shutdown()


if __name__ == '__main__':
    run_server(8000)
