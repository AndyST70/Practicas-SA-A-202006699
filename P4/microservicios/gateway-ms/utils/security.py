import datetime
import jwt
import pytz
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_KEY")
tz = pytz.timezone("America/Guatemala")

def generate_token(user):
    """Genera un JWT con duración de 1 minuto"""
    payload = {
        'iat': datetime.datetime.now(tz=tz),
        'exp': datetime.datetime.now(tz=tz) + datetime.timedelta(minutes=1),
        'email': user["email"],
        'nombre': user["nombre"],
        'roles': ['User']
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(headers):
    """Verifica la validez del token en los headers"""
    if 'Authorization' in headers:
        encoded_token = headers['Authorization'].split(" ")[1]
        if encoded_token:
            try:
                return jwt.decode(encoded_token, SECRET_KEY, algorithms=["HS256"])
            except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                return None
    return None
