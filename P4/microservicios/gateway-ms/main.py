from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os


app = Flask(__name__)
CORS(app, supports_credentials=True)  

SECRET_KEY = os.getenv("JWT_KEY", "supersecreto")
PEDIDOS_MS = os.getenv("PEDIDOS_MS", "http://localhost:5002")

@app.route('/')
def index():
    return 'Bienvenido a la API de la practica 1'

from routes.authroutes import *


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
