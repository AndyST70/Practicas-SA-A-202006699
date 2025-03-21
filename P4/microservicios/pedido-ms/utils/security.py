import datetime
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_KEY", "supersecreto")

def generate_token(user):
    """Genera un JWT con duración de 1 minuto"""
    payload = {
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
        'id': user["id"],
        'email': user["correo"],
        'nombre': user["nombre"]
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(headers):
    """Verifica el JWT"""
    if 'Authorization' not in headers:
        return None
    try:
        token = headers['Authorization'].split(" ")[1]
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
        return None
