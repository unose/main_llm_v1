from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "message": "🎉 Welcome to your Flask Serverless API!",
        "platform": "Vercel + Flask",
        "status": "running",
        "timestamp": datetime.now().isoformat(),
        "endpoints": [
            "/",
            "/about", 
            "/api/hello",
            "/api/time",
            "/api/greet/<name>",
            "/api/echo (POST)"
        ]
    }

@app.route('/about')
def about():
    return {
        "about": "This is a Flask serverless application running on Vercel",
        "version": "1.0.0",
        "author": "Your Name",
        "deployed_on": "Vercel"
    }

@app.route('/api/hello')
def hello_api():
    return {
        "message": "Hello from Flask API endpoint!",
        "timestamp": datetime.now().isoformat(),
        "success": True,
        "endpoint": "/api/hello"
    }

@app.route('/api/time')
def time_api():
    return {
        "current_time": datetime.now().isoformat(),
        "timezone": "UTC",
        "unix_timestamp": datetime.now().timestamp(),
        "serverless": True
    }

@app.route('/api/greet/<name>')
def greet_api(name):
    return {
        "greeting": f"Hello, {name}!",
        "message": "Welcome to the Flask serverless API!",
        "personalized": True,
        "name_provided": name
    }

@app.route('/api/echo', methods=['POST'])
def echo_api():
    """Echo back JSON data sent via POST"""
    try:
        data = request.get_json()
        if not data:
            return {"error": "No JSON data provided"}, 400
            
        return {
            "echo": "Data received successfully!",
            "received_data": data,
            "timestamp": datetime.now().isoformat(),
            "method": "POST"
        }
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/api/status')
def status_api():
    """API status and health check"""
    return {
        "status": "healthy",
        "service": "Flask Serverless API",
        "uptime": "Always available (serverless)",
        "memory_usage": "Managed by Vercel",
        "last_check": datetime.now().isoformat()
    }

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return {
        "error": "Endpoint not found",
        "status_code": 404,
        "available_endpoints": [
            "/",
            "/about",
            "/api/hello", 
            "/api/time",
            "/api/greet/<name>",
            "/api/echo (POST)",
            "/api/status"
        ]
    }, 404

@app.errorhandler(500)
def internal_error(error):
    return {
        "error": "Internal server error",
        "status_code": 500,
        "message": "Something went wrong on the server"
    }, 500

# For local development
if __name__ == '__main__':
    app.run(debug=True)