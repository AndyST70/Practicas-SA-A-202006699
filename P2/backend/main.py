from flask import *
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Bienvenido a la API de la practica 1'

from routes.GestionUser.login import *
from routes.GestionUser.registrar import *
from routes.GestionUser.updateuser import *


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)

