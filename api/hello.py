import json

def handler(request):
    body = {"message": "Hello from Vercel!", "success": True}
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }

