from flask import request, jsonify
from main import app, G_I

@app.route('/eliminar', methods=['DELETE'])
def eliminarproducto():
    nombre = request.form['nombre']
    if not nombre:
        return jsonify({"error": 1, "message": "Nombre del producto es requerido"}), 400
    
    if G_I.eliminar_producto(nombre):
        return jsonify({"error": 0, "message": "Producto eliminado"})

    return jsonify({"error": 1, "message": "Producto no encontrado"}), 404



