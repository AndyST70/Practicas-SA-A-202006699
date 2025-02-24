

class User:
    def __init__(self, email, password, nombre, apellido):
        self.email = email
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        
    def to_dict(self):
        """Convierte la instancia en un diccionario"""
        return {
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido
        }