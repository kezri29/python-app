from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.datetime.now().isoformat(),
        'version': '1.0.0',
        'hostname': socket.gethostname(),
        'description': 'This is a sample Flask application for demonstration purposes.'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

# '/api/v1/details --> basic details of the application'
# '/api/v1/healthz --> for checking kubernetes health'