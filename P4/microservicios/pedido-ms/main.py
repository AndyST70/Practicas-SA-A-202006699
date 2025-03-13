from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Microservicio de Pedidos corriendo'

from routes.pedidoRoutes import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
