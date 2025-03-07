from decouple import config
import datetime
import jwt
import pytz

class Security:
    secret = config('JWT_KEY')  # Se obtiene de .env
    tz = pytz.timezone("America/Guatemala")

    @classmethod
    def generate_token(cls, authenticated_user):
        """Genera un JWT con duración de 10 minutos"""
        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=1),
            'email': authenticated_user.email,  # Identificador del usuario
            'nombre': authenticated_user.nombre,
            'roles': ['User']  # En el futuro podríamos agregar roles dinámicos
        }
        return jwt.encode(payload, cls.secret, algorithm="HS256")

    @classmethod
    def verify_token(cls, headers):
        """Verifica la validez del token en los headers"""
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            encoded_token = authorization.split(" ")[1]

            if len(encoded_token) > 0:
                try:
                    payload = jwt.decode(encoded_token, cls.secret, algorithms=["HS256"])
                    return payload  # Devuelve el payload decodificado si es válido
                except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                    return None
        return None
