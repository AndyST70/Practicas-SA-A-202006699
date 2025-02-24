from app.db import conectar_db
from app.models.user import User
from app.utils.encription import encriptar_password, verificar_password

class GestorUser:
    @staticmethod
    def register_user(email, password, nombre):
        conexion = conectar_db()
        cursor = conexion.cursor()
        hashed_password = encriptar_password(password)
        
        query = '''INSERT INTO 
        usuarios(nombre, email, password_hash, created_at)
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
            SELECT * FROM usuarios
            WHERE email = %s
        '''
        values = (email,)
        cursor.execute(query, values)
        
        user = cursor.fetchall()
        
        cursor.close()
        conexion.close()
        
        if len(user) == 0:
            return None
        
        return User(**user[0])
    
    
        
        