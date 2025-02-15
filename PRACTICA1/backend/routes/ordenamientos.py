from flask import jsonify
from main import app, G_I

@app.route('/ordenarxprecio', methods=['GET'])
def ordenarxprecio():
    if not G_I.mostrar_productos():
        return jsonify({"error": 1, "message": "No hay productos para ordenar"}), 400

    G_I.ordenar_por_precio()
    return jsonify({"error": 0, "message": "Ordenado correctamente por precio", "productos": G_I.mostrar_productos()})

@app.route('/ordenarxcantidad', methods=['GET'])
def ordenarxcantidad():
    if not G_I.mostrar_productos():
        return jsonify({"error": 1, "message": "No hay productos para ordenar"}), 400

    G_I.ordenar_por_cantidad()
    return jsonify({"error": 0, "message": "Ordenado correctamente por cantidad", "productos": G_I.mostrar_productos()})
