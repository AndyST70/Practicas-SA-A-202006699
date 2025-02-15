class Producto:
    contador_id = 1
    
    def __init__ (self, nombre:str, cantidad:int, precio:float):
        self.id = Producto.contador_id
        Producto.contador_id += 1
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }
    