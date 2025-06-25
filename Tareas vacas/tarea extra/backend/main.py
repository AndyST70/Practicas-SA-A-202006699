from flask import Flask, request, jsonify, session
import mysql.connector
import hashlib
import jwt
import datetime
from flask_cors import CORS

from dotenv import load_dotenv
import os


app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Cambiar por uno seguro en producción
CORS(app, supports_credentials=True)

# Configuración DB
load_dotenv()

# PEQUEÑA CORRECCIÓN QUE SE LE HIZO AL CÓDIGO ORIGINAL para no exponer la conexión a la base de datos globalmente

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )

cursor = get_connection().cursor(dictionary=True)

# Función para hashear contraseñas
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    if not name or not email or not password:
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400
    
    # Corrección para tener conexión a la base de datos en cada solicitud
    conn = get_connection() 
    cursor = conn.cursor(dictionary=True)
    
    
    cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return jsonify({'error': 'El correo ya está registrado'}), 409

    hashed_password = hash_password(password)
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                   (name, email, hashed_password))
    get_connection()
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Usuario registrado exitosamente'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()

    if not email or not password:
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400
    
    # Corrección para tener conexión a la base de datos en cada solicitud
    conn = get_connection() 
    cursor = conn.cursor(dictionary=True)
    
    hashed_password = hash_password(password)
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, hashed_password))
    user = cursor.fetchone()

    if not user:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Credenciales incorrectas'}), 401

    token = jwt.encode({
        'user_id': user['id'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, app.secret_key, algorithm='HS256')

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'token': token, 'name': user['name']}), 200


@app.route('/profile', methods=['GET'])
def profile():
    auth_header = request.headers.get('Authorization')
       
    conn = get_connection() 
    cursor = conn.cursor(dictionary=True)
    if not auth_header:
        return jsonify({'error': 'Token requerido'}), 401

    try:
        token = auth_header.split(" ")[1]
        decoded = jwt.decode(token, app.secret_key, algorithms=['HS256'])
        cursor.execute("SELECT name FROM users WHERE id=%s", (decoded['user_id'],))
        user = cursor.fetchone()
        
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': f'Bienvenido, {user["name"]}'}), 200
    except Exception:
        return jsonify({'error': 'Token inválido o expirado'}), 401
    
# Corrección para tener conexion a la base de datos en cada solicitud


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
