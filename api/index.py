from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        data = {
            "message": "Hello World from Vercel!",
            "success": True,
            "path": self.path
        }
        
        self.wfile.write(json.dumps(data).encode())
