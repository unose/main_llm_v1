from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        path = self.path.split('?')[0]
        
        if path == '/api/hello':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = '{"message": "Hello from Vercel!", "success": true}'
            self.wfile.write(response.encode('utf-8'))
            
        elif path == '/api/time':
            self.send_response(200)
            self.send_header('Content-type', 'application/json') 
            self.end_headers()
            response = '{"message": "Time endpoint works!", "serverless": true}'
            self.wfile.write(response.encode('utf-8'))
            
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Hello, world!!! @@@'.encode('utf-8'))