from flask import  request, jsonify, make_response
from models.gestoruser import GestorUser
from utils.encription import verificar_password
from utils.security import Security 
from main import app
from dotenv import load_dotenv
import os
load_dotenv()
time =int(os.getenv('EXPIRED_TIME', 3600))


@app.route('/login', methods=['POST'])
def login():

    email = request.form["email"]
    password = request.form["password"]

    usuario = GestorUser.search_user(email)

    if not usuario or not verificar_password(password, usuario.password):
        return jsonify({"error": 1, "message": "Credenciales incorrectas"}), 401 

    access_token = Security.generate_token(usuario)

    response = make_response(jsonify({"error": 0, "message": "Login exitoso"}))
    response.set_cookie(
        "access_token",
        access_token,
        httponly=True,  
        secure=False,    # 🔹 Solo se enviará en HTTPS
        samesite="Lax",  # 🔹 No permitas que el navegador envíe la cookie en una solicitud que no sea de navegación
        max_age = time
    )

    return response 