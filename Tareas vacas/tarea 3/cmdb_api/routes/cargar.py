import pandas as pd
from config.db import get_connection
from main import app
from flask import request, jsonify


@app.route("/cargar_ci", methods=["POST"])
def cargar_ci_desde_excel():
    df = pd.read_excel('CMDB.xlsx', header=3)
    df.columns = [col.strip() for col in df.columns]

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        nombre_ci = row['Nombre del CI']
        tipo_ci = 1 if row['Tipo de CI'].strip().lower() == 'software' else 0
        descripcion = row['Descripción']
        numero_serie = row.get('Número de Serie')
        version = row.get('Versión')
        fecha_adquisicion = row.get('Fecha de Adquisición')
        estado = row['Estado Actual']
        responsable = row['Propietario/Responsable']
        ubicacion = row['Ubicación Física']
        licencia = row.get('N√∫mero de Licencia')
        doc_nombre = "doc_" + nombre_ci
        doc_ruta = row.get('Documentación relacionada')
        cambio_desc = row.get('Descripción del Cambio')
        fecha_cambio = row.get('Fecha de Cambio')
        idambiente = 1

        # Insert CI
        cursor.execute("""
            INSERT INTO ci (
                nombre_ci, tipo_ci, descripcion, numero_serie, version,
                fecha_adquisicion, estado, responsable, ubicacion, licencia, idambiente
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nombre_ci, tipo_ci, descripcion, numero_serie, version,
              fecha_adquisicion, estado, responsable, ubicacion, licencia, idambiente))
        id_ci = cursor.lastrowid

        #  Documento
        cursor.execute("INSERT INTO documento (nombre, ruta) VALUES (%s, %s)", (doc_nombre, doc_ruta))
        id_doc = cursor.lastrowid

        # Bitacora
        cursor.execute("INSERT INTO bitacora_cambio (descripcion, fec_actual, fec_anterior) VALUES (%s, %s, %s)",
                       (cambio_desc, fecha_cambio, None))
        id_bitacora = cursor.lastrowid

        #  Cambio
        cursor.execute("""
            INSERT INTO cambio (nombre_ci, descripcion, id_doc, id_ci, id_bitacora)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre_ci, cambio_desc, id_doc, id_ci, id_bitacora))

        # Insert Arbol 
        padre = row.get("Padres/Hijos")
        if pd.notna(padre) and padre.strip() != "":
            cursor.execute("SELECT id_ci FROM ci WHERE nombre_ci = %s", (padre.strip(),))
            padre_ci = cursor.fetchone()
            if padre_ci:
                cursor.execute("""
                    INSERT INTO arbol (padre, hijo, tipo, idci)
                    VALUES (%s, %s, %s, %s)
                """, (padre_ci['id_ci'], id_ci, "relacion", id_ci))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"error": 0, "message": "Carga completa"}), 200


@app.route("/reset_tablas", methods=["POST"])
def reset_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE cambio")
    cursor.execute("TRUNCATE TABLE documento")
    cursor.execute("TRUNCATE TABLE bitacora_cambio")
    cursor.execute("TRUNCATE TABLE arbol")
    cursor.execute("TRUNCATE TABLE ci")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"error": 0, "message": "Tablas limpiadas"}), 200
