
from inventario.gestor_inventario import GestorInventario

G_I = GestorInventario()

def Menu():
    print ("1. Agregar Productos")
    print ("2. Mostrar Productos")
    print ("3. Buscar Productos")
    print ("4. Eliminar Productos")
    print ("5. Ordenar Productos x Precio")
    print ("6. Ordenar Productos x cantidad")
    print ("7. Salir")
    
def iniciar ():
    print ("Bienvenido al sistema de inventario")
    
    while True:    
        Menu()
        opcion = int(input("Digita la opcion deseada: "))
        
        if opcion == 1:
            nombre = input("Nombre del producto:")
            cantidad = int(input("Cantidad del producto:"))
            precio = float(input("Precio del producto:"))
            G_I.agregar_producto(nombre, cantidad, precio)
        elif opcion == 2:
            G_I.mostrar_productos()
        elif opcion == 3:
            nombre = input("Nombre del producto a buscar:")
            G_I.buscar_producto
        elif opcion == 4:
            nombre = input("Nombre del producto a eliminar:")
            G_I.eliminar_producto(nombre)
        elif opcion == 5:
            G_I.ordenar_productos_precio()
        elif opcion == 6:
            G_I.ordenar_productos_cantidad()
        elif opcion == 7:
            print ("Salir")
            break
        else:
            print ("Opcion no valida")
        