import json
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

START_TIME = time.time()
BASE_DIR = Path(__file__).resolve().parent

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Grab the header you configured Nginx to send!
        real_ip = self.headers.get('X-Real-IP', 'Unknown / Bypassed Proxy')
        
        # Route 1: Serve the HTML frontend
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            try:
                with open(BASE_DIR / 'index.html', 'rb') as f:
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.wfile.write(b"<h1>Dashboard missing! Check file paths.</h1>")
                
        # Route 2: Serve the JSON API backend
        elif self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            uptime = round(time.time() - START_TIME)
            data = {
                "status": "online",
                "uptime_seconds": uptime,
                "client_ip": real_ip,
                "server_time": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            # Send data back to the browser's JavaScript
            self.wfile.write(json.dumps(data).encode('utf-8'))
            
        # Route 3: Catch everything else (404)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 - Not Found")

if __name__ == '__main__':
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, AppHandler)
    print("Dashboard Microservice running on 127.0.0.1:8000...", flush=True)
    httpd.serve_forever()
