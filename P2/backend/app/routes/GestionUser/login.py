from flask import  request, jsonify
from app.models.gestoruser import GestorUser
from app.utils.encription import verificar_password
from app.utils.token import generate_jwt
import main as app

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    usuario = GestorUser.search_user(email)

    if not usuario or not verificar_password(password, usuario.password):
        return jsonify({"message": "Credenciales incorrectas"}), 401

    access_token = generate_jwt(usuario.email)

    return jsonify({"error":0, "message": "Login exitoso", "access_token": access_token})

