from flask import request, jsonify
import os
from config.db import get_connection
from utils.security import verify_token
from main import app

@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    """Crear un nuevo pedido"""
    token_data = verify_token(request.headers)
    if not token_data:
        return jsonify({"error": 1, "message": "Token inválido o expirado"}), 401

    usuario_id = token_data["id"]
    productos = request.json.get("productos", [])
    total = sum(p["precio"] * p["cantidad"] for p in productos)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pedidos (usuario_id, total) VALUES (%s, %s)", (usuario_id, total))
    pedido_id = cursor.lastrowid

    for p in productos:
        cursor.execute("INSERT INTO detalles_pedido (pedido_id, producto_id, cantidad, precio_unitario) VALUES (%s, %s, %s, %s)",
                       (pedido_id, p["id"], p["cantidad"], p["precio"]))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Pedido creado con éxito", "pedido_id": pedido_id})

@app.route('/pedidos', methods=['GET'])
def obtener_pedidos():
    """Obtener todos los pedidos"""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(pedidos)
