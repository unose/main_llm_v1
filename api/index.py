# api/index.py

from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify(message="Hello from Vercel!", success=True)

@app.route('/api/time')
def time_endpoint():
    return jsonify(
        message="Time endpoint works!",
        serverless=True,
        time=datetime.utcnow().isoformat() + "Z"
    )

# catch‑all for anything else
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def fallback(path):
    return "Hello, world!!! 🚀", 200, {"Content-Type": "text/plain"}
