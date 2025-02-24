from flask_jwt_extended import create_access_token
import datetime

def generate_jwt(user_id):
    """Genera un token de acceso JWT"""
    expires = datetime.timedelta(hours=1)
    return create_access_token(identity=user_id, expires_delta=expires)
