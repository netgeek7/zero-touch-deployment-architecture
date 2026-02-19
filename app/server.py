import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Grab the specific header Nginx is sending
        real_ip = self.headers.get('X-Real-IP')
        
        # 2. Print it clearly to the logs (flushing ensures it appears immediately)
        print(f"\n[DEBUG] TCP Source: {self.client_address[0]}")
        print(f"[DEBUG] Nginx Header says Real IP is: {real_ip}\n", flush=True)

        # 3. Response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Check your logs now.")

# Start server
httpd = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
print("Server started on 127.0.0.1:8000...", flush=True)
httpd.serve_forever()
