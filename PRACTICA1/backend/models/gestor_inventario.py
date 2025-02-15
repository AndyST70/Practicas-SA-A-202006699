from .producto import Producto

class GestorInventario:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, producto: Producto):
        self.inventario.append(producto)

    def mostrar_productos(self):
        return [p.to_dict() for p in self.inventario]

    def buscar_producto(self, nombre: str):
        for producto in self.inventario:
            if producto.nombre.lower() == nombre.lower():
                return producto.to_dict()
        return None

    def eliminar_producto(self, nombre: str):
        for producto in self.inventario:
            if producto.nombre.lower() == nombre.lower():
                self.inventario.remove(producto)
                return True
        return False

    def ordenar_por_precio(self):
        self.inventario.sort(key=lambda p: p.precio)

    def ordenar_por_cantidad(self):
        self.inventario.sort(key=lambda p: p.cantidad)
