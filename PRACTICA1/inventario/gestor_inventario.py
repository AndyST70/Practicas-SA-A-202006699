from .producto import Producto
class GestorInventario:
    def __init__(self):
        self.inventario = []
        
        
        
    def validarnombre (self, nombre:str):
        if nombre == "":
            print("Datos no validos")
            return
        for producto in self.inventario:
            if producto.nombre == nombre:
                print("Producto ya existe")
                return 
            
        
    def agregar_producto(self, nombre:str, cantidad:int, precio:float):
        if nombre == "" or cantidad <= 0 or precio <= 0:
            print("Datos no validos")
            return
        
        self.validarnombre(nombre)
        
        producto = Producto(nombre, cantidad, precio)
        self.inventario.append(producto)

           
    def mostrar_productos(self):
        producto = Producto
        
        print("\n" + "*" * 50)
        print(f"{'ID':<5} | {'Nombre':<15} | {'Cantidad':^10} | {'Precio':>8}")
        print("-" * 50)
        
        for producto in self.inventario:
            print(producto)
        
        print("\n" + "*" * 50)
        
        
    
    #metodo de busqueda 
    def buscar_producto(self, nombre:str):
        if nombre == "":
            print("Datos no validos")
            return
        for producto in self.inventario:
            if producto.nombre == nombre:
                print("Producto encontrado")
                print(producto)
                return
            
    def eliminar_producto(self, nombre:str):
        if nombre == "":
            print("Datos no validos")
            return
        for producto in self.inventario:
            if producto.nombre == nombre:
                self.inventario.remove(producto)
                print("Producto {nombre} eliminado")
                return
        print("Producto no encontrado")
    
    def ordenar_productos_precio(self):
        if len(self.inventario) == 0:
            print("No hay productos")
            return
        self.inventario.sort(key=lambda producto: producto.precio)
        print("Productos ordenados por precio")
        self.mostrar_productos()
        
    def ordenar_productos_cantidad(self):
        self.inventario.sort(key=lambda producto: producto.cantidad)
        print("Productos ordenados por cantidad")
        self.mostrar_productos()