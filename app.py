from flask import Flask, jsonify, render_template_string
from datetime import datetime
import platform

app = Flask(__name__)

# HTML template for the home page
HOME_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Python Web API Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f0f2f5;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #1a73e8;
        }
        .endpoint {
            background-color: #f8f9fa;
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
            border-left: 4px solid #1a73e8;
        }
        code {
            background-color: #e9ecef;
            padding: 2px 4px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Python Web API Demo!</h1>
        <p>This is a demonstration of a Flask web application deployed on Azure.</p>
        
        <h2>Available Endpoints:</h2>
        <div class="endpoint">
            <strong>GET /</strong> - This home page
        </div>
        <div class="endpoint">
            <strong>GET /api/info</strong> - System information
        </div>
        <div class="endpoint">
            <strong>GET /api/time</strong> - Current server time
        </div>
        <div class="endpoint">
            <strong>GET /api/health</strong> - Service health check
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    """Render the home page with API documentation"""
    return render_template_string(HOME_TEMPLATE)

@app.route('/api/info')
def system_info():
    """Return system information"""
    info = {
        'python_version': platform.python_version(),
        'platform': platform.platform(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'system': platform.system()
    }
    return jsonify(info)

@app.route('/api/time')
def get_time():
    """Return current server time"""
    time_info = {
        'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'timezone': datetime.now().astimezone().tzinfo.tzname(datetime.now()),
        'timestamp': datetime.now().timestamp()
    }
    return jsonify(time_info)

@app.route('/api/health')
def health_check():
    """Return service health status"""
    health_info = {
        'status': 'healthy',
        'service': 'Python Web API',
        'version': '1.0.0',
        'uptime': 'Active'
    }
    return jsonify(health_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
