from flask import request, jsonify
from config.db import get_connection
from main import app
from utils.utils import generar_token, requiere_token, verificar_token
from datetime import datetime
import jwt

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    usuario = data.get("usuario")
    password = data.get("password")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ambiente WHERE usuario = %s AND password_ci = %s", (usuario, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        return jsonify({"error": 1, "message": "Credenciales inválidas"}), 401

    token = generar_token({"id": user["idambiente"], "rol": user["rol"]})
    return jsonify({"error": 0, "token": token}), 200


@app.route('/ci', methods=['GET'])
def get_ci():
    user = requiere_token()
    if not user:
        return jsonify({"error": 1, "message": "Token inválido"}), 401

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT ci.*, a.usuario AS ambiente_usuario
        FROM ci
        LEFT JOIN ambiente a ON ci.idambiente = a.idambiente
    """)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify({"error": 0, "data": data}), 200

# crear ci

@app.route('/ci', methods=['POST'])
def crear_ci():
    user = requiere_token()
    if not user:
        return jsonify({"error": 1, "message": "Token inválido"}), 401

    data = request.form
    conn = get_connection()
    cursor = conn.cursor()

    nombre_ci = data.get('nombre_ci')
    tipo_ci = data.get('tipo')
    estado = data.get('estado')
    idambiente = data.get('ambiente')
    fecha_adquisicion = data.get('fecha_adquisicion')
    responsable = data.get('responsable')
    ubicacion = data.get('ubicacion')
    descripcion = data.get('descripcion')
    numero_serie = data.get('numero_serie')
    version = data.get('version')
    licencia = data.get('licencia')
    
    
    if not nombre_ci or not tipo_ci or not estado or not idambiente:
        return jsonify({"error": 1, "message": "Faltan campos obligatorios"}), 400


    cursor.execute("SELECT idambiente FROM ambiente WHERE idambiente = %s", (idambiente,))
    if not cursor.fetchone():
        return jsonify({"error": 1, "message": "Ambiente inválido"}), 400

    query = '''
        INSERT INTO ci (
            nombre_ci, tipo_ci, estado, idambiente, fecha_adquisicion,
            responsable, ubicacion, descripcion, numero_serie, version, licencia
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    values = (
        nombre_ci, tipo_ci, estado, idambiente,
        fecha_adquisicion or datetime.now(),
        responsable, ubicacion, descripcion,
        numero_serie, version, licencia
    )

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"error": 0, "message": "CI creado correctamente"}), 201

@app.route('/ci/<int:id>', methods=['GET'])
def obtener_ci(id):
    user = requiere_token()
    if not user:
        return jsonify({"error": 1, "message": "Token inválido"}), 401

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM ci WHERE id_ci = %s"
    cursor.execute(query, (id,))
    ci = cursor.fetchone()

    cursor.close()
    conn.close()

    if not ci:
        return jsonify({"error": 1, "message": "CI no encontrado"}), 404

    return jsonify({"error": 0, "data": ci}), 200


@app.route('/ci/<int:id>', methods=['DELETE'])
def eliminar_ci(id):
    user = requiere_token()
    if not user:
        return jsonify({"error": 1, "message": "Token inválido"}), 401

    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM ci WHERE id_ci = %s"
    cursor.execute(query, (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"error": 0, "message": "CI eliminado correctamente"}), 200


