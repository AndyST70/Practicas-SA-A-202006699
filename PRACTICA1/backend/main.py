from flask import *
from flask_cors import CORS
from models.gestor_inventario import GestorInventario


app = Flask(__name__)
CORS(app)

G_I = GestorInventario()
@app.route('/')
def index():
    return 'Bienvenido a la API de la practica 1'


from routes.agregar_producto import *
from routes.buscarproducto import *
from routes.eliminar import *
from routes.mostrarproductos import *
from routes.ordenamientos import *

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
