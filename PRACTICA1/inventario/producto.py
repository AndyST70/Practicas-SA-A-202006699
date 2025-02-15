class Producto:
    contador_id = 1
    
    def __init__ (self, nombre:str, cantidad:int, precio:float):
        self.id = Producto.contador_id
        Producto.contador_id += 1
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        
    def __str__(self):
         return f"{self.id:<5} | {self.nombre:<15} | {self.cantidad:^10} | Q{self.precio:>8.2f}"
    
    