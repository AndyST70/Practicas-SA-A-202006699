from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Servicio funcionando '

from routes.ci_routes import *
from routes.cargar import *
from routes.cambios import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
