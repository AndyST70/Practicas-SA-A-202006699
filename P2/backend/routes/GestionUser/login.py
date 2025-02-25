from flask import  request, jsonify
from models.gestoruser import GestorUser
from utils.encription import verificar_password
from utils.security import Security 
from main import app




@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    usuario = GestorUser.search_user(email)

    if not usuario or not verificar_password(password, usuario.password):
        return jsonify({"message": "Credenciales incorrectas"}), 401

    access_token = Security.generate_token(usuario)

    return jsonify({"error":0, "message": "Login exitoso", "access_token": access_token})

