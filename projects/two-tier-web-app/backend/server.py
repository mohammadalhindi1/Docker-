from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import socket


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            payload = {"status": "healthy"}
            status = 200
        else:
            payload = {
                "message": os.getenv("APP_MESSAGE", "Hello from the backend"),
                "hostname": socket.gethostname(),
                "path": self.path,
            }
            status = 200

        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
