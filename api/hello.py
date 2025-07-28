from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response_data = {
            "message": "🎉 Hello from Vercel!",
            "timestamp": datetime.now().isoformat(),
            "path": self.path,
            "method": "GET",
            "status": "success"
        }
        
        self.wfile.write(json.dumps(response_data).encode())
        return
