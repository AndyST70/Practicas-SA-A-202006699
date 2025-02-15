
<h1 align="center"> Documentacion</h1>

<p align="center">
   <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
   </p>

*Universidad de San Carlos de Guatemala*  
*Escuela de Ingeniería en Ciencias y Sistemas, Facultad de Ingenieria*  
*Laboratorio Analisis y Diseño de sistemas 2, Vacaciones de Diciembre 2024.*  
*Seccion P - Grupo 1*  


# Principios SOLID - Ejemplo de Pizzería

Este archivo explica los principios SOLID aplicados en la programación orientada a objetos, usando como ejemplo una pizzería que gestiona pedidos, ingredientes y facturación.

### 1. Principio de Responsabilidad Única (SRP)

Cada clase debe tener una única responsabilidad, es decir, debe tener una razón para cambiar. Esto facilita el mantenimiento y la comprensión del código.

**Ejemplo:**

```python
class Pizza:
    def __init__(self, tipo, ingredientes):
        self.tipo = tipo
        self.ingredientes = ingredientes

    def preparar(self):
        # Lógica para preparar la pizza
        print(f"Preparando una pizza {self.tipo} con {', '.join(self.ingredientes)}")

class Pedido:
    def __init__(self, pizza):
        self.pizza = pizza

    def realizar_pedido(self):
        # Lógica para procesar el pedido
        self.pizza.preparar()
        print("Pedido realizado con éxito")
```

En este ejemplo, la clase Pizza se encarga de la preparación de la pizza y la clase Pedido de procesar el pedido. Cada clase tiene una responsabilidad específica.

### 2. Principio de Abierto/Cerrado (OCP)
Las clases deben estar abiertas para su extensión, pero cerradas para su modificación. Esto significa que podemos añadir nuevas funcionalidades sin modificar el código existente.

Ejemplo:

```python

class Pizza:
    def __init__(self, tipo, ingredientes):
        self.tipo = tipo
        self.ingredientes = ingredientes

    def preparar(self):
        # Lógica para preparar la pizza
        print(f"Preparando una pizza {self.tipo} con {', '.join(self.ingredientes)}")

class PizzaConExtra(Pizza):
    def __init__(self, tipo, ingredientes, extra):
        super().__init__(tipo, ingredientes)
        self.extra = extra

    def preparar(self):
        # Añadir extra en la preparación
        super().preparar()
        print(f"Añadiendo extra: {self.extra}")
```

En este caso, la clase PizzaConExtra extiende la clase Pizza, añadiendo la funcionalidad de agregar un ingrediente extra, sin modificar la clase base Pizza.

### 3. Principio de Sustitución de Liskov (LSP)
Las clases derivadas deben poder ser sustituidas por sus clases base sin alterar el comportamiento esperado del programa.

Ejemplo:

```python
class Bebida:
    def servir(self):
        # Lógica para servir la bebida
        pass

class Refresco(Bebida):
    def servir(self):
        print("Sirviendo refresco")

class Jugo(Bebida):
    def servir(self):
        print("Sirviendo jugo")

# Uso
def servir_bebida(bebida: Bebida):
    bebida.servir()

# Podemos pasar tanto refresco como jugo sin problemas
servir_bebida(Refresco())
servir_bebida(Jugo())
```

Aquí, tanto Refresco como Jugo pueden sustituir a Bebida sin causar ningún problema en el comportamiento del programa.

### 4. Principio de Segregación de Interfaces (ISP)
Los clientes no deben ser forzados a implementar interfaces que no usan. Esto implica que las interfaces deben ser más específicas y no contener métodos innecesarios.

Ejemplo:

```python

class PedidoPizza:
    def preparar_pizza(self):
        # Preparar pizza
        pass

class PedidoBebida:
    def preparar_bebida(self):
        # Preparar bebida
        pass

class Cliente:
    def realizar_pedido_pizza(self, pedido: PedidoPizza):
        pedido.preparar_pizza()

    def realizar_pedido_bebida(self, pedido: PedidoBebida):
        pedido.preparar_bebida()
```
Aquí, los métodos preparar_pizza y preparar_bebida están separados en interfaces específicas, evitando que el cliente tenga que implementar métodos que no le son útiles.

### 5. Principio de Inversión de Dependencias (DIP)
Las clases de alto nivel no deben depender de clases de bajo nivel, sino de abstracciones. Esto reduce el acoplamiento y facilita la reutilización del código.

Ejemplo:

```python
Copiar
Editar
class BaseDeDatos:
    def guardar(self, datos):
        pass

class MySQL(BaseDeDatos):
    def guardar(self, datos):
        print("Guardando en MySQL")

class PostgreSQL(BaseDeDatos):
    def guardar(self, datos):
        print("Guardando en PostgreSQL")

class Factura:
    def __init__(self, base_de_datos: BaseDeDatos):
        self.base_de_datos = base_de_datos

    def procesar_factura(self, datos):
        # Procesar factura
        self.base_de_datos.guardar(datos)

# Uso
mysql_db = MySQL()
factura = Factura(mysql_db)
factura.procesar_factura("Factura de pizza")
```


Estos principios SOLID ayudan a mantener el código modular, limpio y fácil de escalar. Al implementar estos principios, es más sencillo hacer modificaciones y añadir nuevas funcionalidades sin afectar el comportamiento del sistema existente.