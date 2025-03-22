from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Microservicio de Usuario activo'

from routes.userRoutes import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
