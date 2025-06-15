import jwt
import os
from datetime import datetime, timedelta
from flask import request
import hashlib

SECRET = os.getenv("JWT_SECRET", "dev-secret")

def generar_token(payload, exp_minutes=60):
    payload["exp"] = datetime.utcnow() + timedelta(minutes=exp_minutes)
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verificar_token(token):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def requiere_token():
    auth = request.headers.get("Authorization", "")
    token = auth.replace("Bearer ", "")
    user = verificar_token(token)
    return user

def encriptar_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()