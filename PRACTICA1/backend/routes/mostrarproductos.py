
from main import G_I 
from flask import Flask, request, jsonify
from main import app



@app.route('/mostrarproductos', methods=['GET'])
def mostrarproductos():
    #* Mostrar productos
    productos = G_I.mostrar_productos()
    return jsonify({"error":"0","messsage":"Productos", "productos":productos})

