from flask import  request, jsonify
from models.gestoruser import GestorUser
from main import app


@app.route('/register', methods=['POST'])
def register():
    email = request.form["email"]
    password = request.form["password"]
    nombre = request.form["nombre"]

    if GestorUser.search_user(email):
        return jsonify({"error": 1, "message": "Ya existe un usuario con este email"}), 400

    GestorUser.register_user(email, password, nombre)
    return jsonify({"error": 0, "message": "Usuario registrado"}), 200

