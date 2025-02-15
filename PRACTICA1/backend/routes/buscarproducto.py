from flask import request, jsonify
from main import app, G_I

@app.route('/buscarproducto', methods=['GET'])
def buscarproducto():
    nombre = request.form['nombre']
    #Validaciones de los campos
    if not nombre:
        return jsonify({"error": 1, "message": "Nombre del producto es requerido"}), 400
    #Busqueda del producto
    producto = G_I.buscar_producto(nombre)

    if producto:
        return jsonify({"error": 0, "message": "Producto encontrado", "producto": producto})

    
    return jsonify({"error": 1, "message": "Producto no encontrado"}), 404



