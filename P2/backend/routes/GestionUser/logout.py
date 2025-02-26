from flask import jsonify, make_response
from main import app

@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify({"error": 0, "message": "Sesión cerrada"}))
    response.set_cookie("access_token", "", httponly=True, secure=True, samesite="Strict", max_age=0)  # 🔹 Borra la cookie
    return response
