from flask import request, jsonify
from utils.security import Security
from main import app

@app.route('/verify_session', methods=['GET'])
def verify_session():
    print("Cookies recibidas en el servidor:", request.cookies)
    access_token = request.cookies.get("access_token")
    
    if not access_token:
        return jsonify({"error": 1, "message": "No autenticado"}), 401
    
    payload = Security.verify_token({"Authorization": f"Bearer {access_token}"})
    
    if not payload:
        return jsonify({"error": 1, "message": "Token inválido o expirado"}), 401

    return jsonify({"error": 0, "message": "Usuario autenticado", "user": payload})
