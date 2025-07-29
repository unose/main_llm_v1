from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Parse the URL path
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        # Simple routing
        if path == '/api/hello':
            self.send_json_response({
                "message": "🎉 Hello from enhanced Vercel function!",
                "timestamp": datetime.now().isoformat(),
                "success": True
            })
        elif path == '/api/greet':
            name = query_params.get('name', ['World'])[0]
            self.send_json_response({
                "greeting": f"Hello, {name}!",
                "message": "Welcome to serverless!",
                "platform": "Vercel"
            })
        elif path == '/api/time':
            self.send_json_response({
                "current_time": datetime.now().isoformat(),
                "timezone": "UTC",
                "serverless": True
            })
        else:
            # Default response
            self.send_text_response("Hello, world!!! ** Your serverless function is working!")
    
    def send_json_response(self, data, status=200):
        """Helper method to send JSON responses"""
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))
    
    def send_text_response(self, text, status=200):
        """Helper method to send text responses"""
        self.send_response(status)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(text.encode('utf-8'))

