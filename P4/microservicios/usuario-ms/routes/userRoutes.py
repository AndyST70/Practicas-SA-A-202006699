from flask import request,  jsonify
from config.db import get_connection
from utils.security import encriptar
from main import app

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.form
    nombre = data["nombre"]
    correo = data["correo"]
    password = data["password"]


    conn = get_connection()
    cursor = conn.cursor()

    query = '''
        SELECT id FROM usuarios WHERE
        correo = %s 
    '''
    cursor.execute(query, (correo,))
    user = cursor.fetchall()
    
    if user:
        return jsonify({"error": 1, "message": "El correo ya está registrado"}), 400
    
    hashed = encriptar(password)
    
    query = '''
        INSERT INTO
        usuarios (nombre, correo, contrasenia, logueado)
        VALUES (%s, %s, %s, 0)
    '''
    value = (nombre, correo, hashed)
    cursor.execute(query, value)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"error": 0, "message": "Usuario creado con éxito"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    correo = data["correo"]
    password = data["password"]

    hashed = encriptar(password)

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = '''
        SELECT * FROM usuarios WHERE
        correo = %s AND contrasenia = %s
    '''
    values = (correo, hashed)
    cursor.execute(query, values)
    user = cursor.fetchone() 

    if not user:
        return jsonify({"error": 1, "message": "Credenciales inválidas"}), 401

    query = '''
        UPDATE usuarios SET logueado = 1 WHERE id = %s
    '''
    cursor.execute(query, (user["id"],))  
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "error": 0,
        "message": f"Bienvenido {user['nombre']}",
        "usuario_id": user["id"]
    }), 200

    
@app.route('/logout', methods=['POST'])
def logout():
    data = request.form
    usuario_id = data["usuario_id"]

    conn = get_connection()
    cursor = conn.cursor()
    query = '''
        SELECT * FROM usuarios WHERE
        id = %s
    '''
    cursor.execute(query, (usuario_id,))
    user = cursor.fetchall()
    
    if not user:
        return jsonify({"error": 1, "message": "Usuario no encontrado"}), 404
    
    query = '''
        UPDATE usuarios SET logueado = 0 WHERE id = %s
    '''
    values = (usuario_id,)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"error": 0, "message": "Sesión cerrada"}), 200