from flask import  request, jsonify
from app.models.gestoruser import GestorUser
from main import app


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    nombre = data.get('nombre')

    if GestorUser.search_user(email):
        return jsonify({"error": 1, "message": "Ya existe un usuario con este email"}), 400

    GestorUser.register_user(email, password, nombre)
    return jsonify({"error": 0, "message": "Usuario registrado"}), 200

