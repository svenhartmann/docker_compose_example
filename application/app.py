from flask import Flask
from redis import Redis
import os
import socket
app = Flask(__name__)
redis = Redis(host='redis', port=6379)
host = socket.gethostname()

@app.route('/')
def start():
    redis.incr('hits' + host)
    return '<h1>Scale / HAProxy example</h1><br>Requests: %s times.<br>Hostname: %s\n\n' % (redis.get('hits' + host), host)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
