from flask import  request, jsonify
from models.gestoruser import GestorUser
from main import app


@app.route('/recuperar', methods=['POST'])
def update_user():
    email = request.form["email"]
    new_password = request.form["new_password"]

    usuario = GestorUser.search_user(email)

    if not usuario:
        return jsonify({"message": "Usuario no encontrado"}), 404

    GestorUser.update_user(email, new_password)
    return jsonify({"error":0, "message":"Actualizacion correcta"}), 200
