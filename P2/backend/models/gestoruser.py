from db import conectar_db
from models.user import User
from utils.encription import encriptar, verificar_password

class GestorUser:
    @staticmethod
    def register_user(email, password, nombre):
        conexion = conectar_db()
        cursor = conexion.cursor()
        hashed_password = encriptar(password)  # Asegura que la contraseña se almacene encriptada
        
        query = '''INSERT INTO 
        Usuarios (nombre, email, password_hash, created_at)
        VALUES (%s, %s, %s, NOW())
        '''
        values = (nombre, email, hashed_password)
        cursor.execute(query, values)
        conexion.commit()
        
        cursor.close()
        conexion.close()
        
    @staticmethod
    def search_user(email):
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)
        
        query = '''
            SELECT * FROM Usuarios
            WHERE email = %s
        '''
        values = (email,)
        cursor.execute(query, values)
        
        user = cursor.fetchall()
        
        cursor.close()
        conexion.close()
        
        if len(user) == 0:
            return None
        
        return User(email=user[0]["email"], password=user[0]["password_hash"], nombre=user[0]["nombre"])

    @staticmethod
    def update_user(email, password):
        usuario = GestorUser.search_user(email)
        if usuario is None:
            return
        
        hashed_password = encriptar(password)  # Encriptamos correctamente la nueva contraseña
        conexion = conectar_db()
        cursor = conexion.cursor()
        
        query = '''
            UPDATE Usuarios
            SET password_hash = %s
            WHERE email = %s
        '''
        values = (hashed_password, email)
        cursor.execute(query, values)
        conexion.commit()
        
        cursor.close()
        conexion.close()
