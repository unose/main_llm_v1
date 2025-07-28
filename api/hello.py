def handler(request):
    """
    Simple serverless function for Vercel
    This format is more compatible with Vercel's system
    """
    import json
    from datetime import datetime
    
    # Get the path from the request
    path = request.url.path if hasattr(request, 'url') else '/'
    
    # Simple routing based on path
    if path == '/api/test':
        response_data = {
            "test": "This endpoint works perfectly!",
            "deployed_on": "Vercel",
            "timestamp": datetime.now().isoformat(),
            "status": "success"
        }
    else:
        response_data = {
            "message": "🎉 Hello from my first serverless function!",
            "platform": "Vercel",
            "python_version": "3.11.3", 
            "status": "working!",
            "timestamp": datetime.now().isoformat()
        }
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(response_data)
    }
