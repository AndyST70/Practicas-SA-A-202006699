from flask import  request, jsonify
from app.models.gestoruser import GestorUser
from main import app


@app.route('/update_user', methods=['POST'])
def update_user():
    data = request.json
    email = data.get('email')
    new_password = data.get('new_password')

    usuario = GestorUser.search_user(email)

    if not usuario:
        return jsonify({"message": "Usuario no encontrado"}), 404

    GestorUser.update_user(email, new_password)
    return jsonify({"error":0, "message":"Actualizacion correcta"}), 200
