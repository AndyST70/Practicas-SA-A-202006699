from flask import request, jsonify
import os
from config.db import get_connection
from main import app

@app.route('/realizar_pedidos', methods=['POST'])
def crear_pedido():
    data = request.form

    usuario_id = data['usuario_id']
    productos_id = data['producto_id']
    cantidad = data['cantidad']
    
    if not usuario_id or not productos_id or not cantidad:
        return jsonify({'error': 1, 'message': 'Faltan datos'}), 400
    
    con = get_connection()
    cursor = con.cursor()
    
    # obtener el precio de los productos
    query = '''
        SELECT precio FROM productos WHERE id = %s
    '''
    values = (productos_id,)
    cursor.execute(query, values)
    precios = cursor.fetchall()

    if not precios:
        return jsonify({'error': 1, 'message': 'Producto no encontrado'}), 404
    
    precio_unitario = float(precios[0][0])
    resultado = precio_unitario * float(cantidad)
    
    query = '''
        INSERT INTO 
        pedidos (usuario_id, total) 
        VALUES (%s, %s)
    '''
    values = (usuario_id, resultado)
    cursor.execute(query, values)
    pedido_id = cursor.lastrowid
    
    #insertar detalle de pedido
    
    query = '''
        INSERT INTO 
        detalles_pedido (pedido_id, producto_id, cantidad, precio_unitario)
        VALUES (%s, %s, %s, %s)
    '''
    values = (pedido_id, productos_id, cantidad, precio_unitario)
    cursor.execute(query, values)
    con.commit()
    con.close()
    cursor.close()
        
    return jsonify({'message': 'Pedido creado con éxito'})


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
