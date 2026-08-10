from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = int(os.getenv("BACKEND_PORT", "8000"))
APP_ENV = os.getenv("APP_ENV", "development")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"healthy")
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = f"""
        <html>
        <body>
            <h1>Samet Docker Final Project</h1>
            <p>Backend calisiyor.</p>
            <p>Environment: {APP_ENV}</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

server = HTTPServer(("0.0.0.0", PORT), Handler)
print(f"Backend {PORT} portunda calisiyor")
server.serve_forever()
