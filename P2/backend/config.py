from decouple import config

class Config():
    SECRET_KEY = config('SECRET_KEY')
    JWT_KEY = config('JWT_KEY')  # Ahora también cargamos JWT_KEY

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}
