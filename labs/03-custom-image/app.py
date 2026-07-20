from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = os.getenv("APP_MESSAGE", "Hello from a custom Docker image!")
        body = (
            f"{message}\n"
            f"Container hostname: {socket.gethostname()}\n"
            f"Request path: {self.path}\n"
        ).encode()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Server listening on port 8000", flush=True)
    server.serve_forever()
