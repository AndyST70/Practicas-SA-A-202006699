from flask import request, jsonify
from datetime import datetime
from config.db import get_connection
from main import app
from utils.utils import requiere_token

@app.route('/cambio', methods=['POST'])
def crear_cambio():
    user = requiere_token()
    if not user:
        return jsonify({"error": 1, "message": "Token inválido"}), 401

    data = request.form
    nombre_ci = data.get("nombre_ci")
    descripcion = data.get("descripcion")
    id_ci = data.get("id_ci")
    nombre_doc = data.get("documento_nombre")
    ruta_doc = data.get("documento_ruta")

    if not nombre_ci or not descripcion or not id_ci:
        return jsonify({"error": 1, "message": "Faltan campos obligatorios"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO documento (nombre, ruta) VALUES (%s, %s)",
        (nombre_doc, ruta_doc)
    )
    id_doc = cursor.lastrowid

    fecha_actual = datetime.now()

    cursor.execute(
        "INSERT INTO bitacora_cambio (descripcion, fec_actual, fec_anterior) VALUES (%s, %s, %s)",
        ("Creación de cambio", fecha_actual, fecha_actual)
    )
    id_bitacora = cursor.lastrowid

    cursor.execute(
        "INSERT INTO cambio (nombre_ci, descripcion, id_doc, id_ci, id_bitacora) VALUES (%s, %s, %s, %s, %s)",
        (nombre_ci, descripcion, id_doc, id_ci, id_bitacora)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"error": 0, "message": "Cambio registrado correctamente"}), 201


@app.route('/cambio/<int:id_cambio>', methods=['PUT'])
def actualizar_cambio(id_cambio):
    user = requiere_token()
    if not user:
        return jsonify({"error": 1, "message": "Token inválido"}), 401

    data = request.form
    descripcion = data.get("descripcion")

    if not descripcion:
        return jsonify({"error": 1, "message": "Descripción requerida"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    fecha_actual = datetime.now()

    cursor.execute(
        "SELECT id_bitacora FROM cambio WHERE idcambio = %s", (id_cambio,)
    )
    row = cursor.fetchone()
    if not row:
        return jsonify({"error": 1, "message": "Cambio no encontrado"}), 404

    id_bitacora = row[0]

    cursor.execute(
        "UPDATE bitacora_cambio SET descripcion = %s, fec_actual = %s WHERE idbitacora = %s",
        ("Actualización de cambio", fecha_actual, id_bitacora)
    )

    cursor.execute(
        "UPDATE cambio SET descripcion = %s WHERE idcambio = %s",
        (descripcion, id_cambio)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"error": 0, "message": "Cambio actualizado correctamente"}), 200
