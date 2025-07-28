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
            self.send_text_response("Hello, world!!! 🚀 Your serverless function is working!")
    
    def do_POST(self):
        # Handle POST requests
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
            name = data.get('name', 'Anonymous')
            
            self.send_json_response({
                "message": f"Hello, {name}! Thanks for the POST request!",
                "received_data": data,
                "timestamp": datetime.now().isoformat(),
                "method": "POST"
            })
        except json.JSONDecodeError:
            self.send_json_response({
                "error": "Invalid JSON",
                "message": "Please send valid JSON data"
            }, status=400)
    
    def send_json_response(self, data, status=200):
        """Helper method to send JSON responses"""
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))
    
    def send_text_response(self, text, status=200):
        """Helper method to send text responses"""
        self.send_response(status)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(text.encode('utf-8'))
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()