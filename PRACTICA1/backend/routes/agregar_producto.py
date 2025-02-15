from flask import request, jsonify
from main import app, G_I
from models.producto import Producto

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    nombre = request.form["nombre"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]
    #Validaciones de los campos
    if not nombre or not cantidad or not precio:
        return jsonify({"error": 1, "message": "Todos los campos son obligatorios"}), 400

    if not cantidad.isdigit() or not precio.replace('.', '', 1).isdigit():
        return jsonify({"error": 1, "message": "Cantidad y precio deben ser numéricos"}), 400

    if any(p["nombre"].lower() == nombre.lower() for p in G_I.mostrar_productos()):
        return jsonify({"error": 1, "message": "Ya existe un producto con este nombre"}), 400

    #Creación del objeto producto
    producto = Producto(nombre, int(cantidad), float(precio))
    G_I.agregar_producto(producto)

    return jsonify({"error": 0, "message": "Producto agregado", "producto": producto.to_dict()})
