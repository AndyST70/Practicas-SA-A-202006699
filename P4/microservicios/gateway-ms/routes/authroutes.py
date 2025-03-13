from flask import  request, jsonify
import requests
import os
from utils.security import generate_token, verify_token
from main import app


AUTH_MS = os.getenv("AUTH_MS")

AUTH_MS = os.getenv("AUTH_MS")
CATALOGO_MS = os.getenv("CATALOGO_MS")
REGISTRO_MS = os.getenv("REGISTRO_MS")

@app.route('/login', methods=['POST'])
def login():
    """Ruta para autenticación de usuarios"""
    usuario = request.form.get("usuario")
    password = request.form.get("password")
    
    if not usuario or not password:
        return jsonify({"error": 1, "message": "Faltan datos en la petición"}), 400

    
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(f"{AUTH_MS}/login", data={"usuario": usuario, "password": password}, headers=headers)

    if response.status_code != 200:
        return jsonify({"error": 1, "message": "Credenciales incorrectas"}), 401

    user_data = response.json()
    token = generate_token(user_data)

    response = jsonify({"error": 0, "message": "Login exitoso"})
    response.set_cookie("access_token", token, httponly=True, secure=False, samesite="Lax", max_age=60)
    return response

@app.route('/verify-token', methods=['GET'])
def verify():
    """Verifica si el token es válido"""
    token_data = verify_token(request.headers)
    if not token_data:
        return jsonify({"error": 1, "message": "Token inválido o expirado"}), 401
    return jsonify({"error": 0, "message": "Token válido", "user": token_data})

@app.route('/catalogo', methods=['POST'])
def catalogo():
    """Redirige solicitudes a catalogo-ms"""
    token_data = verify_token(request.headers)
    if not token_data:
        return jsonify({"error": 1, "message": "Token inválido o expirado"}), 401

    response = requests.post(CATALOGO_MS, json=request.get_json())
    return response.json()

@app.route('/registro', methods=['POST'])
def registro():
    """Redirige solicitudes a registro-ms"""
    token_data = verify_token(request.headers)
    if not token_data:
        return jsonify({"error": 1, "message": "Token inválido o expirado"}), 401

    response = requests.post(REGISTRO_MS, json=request.get_json())
    return response.json()
