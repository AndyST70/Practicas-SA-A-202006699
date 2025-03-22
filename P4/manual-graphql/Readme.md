# Manual Básico de GraphQL

## ¿Qué es GraphQL?
Un lenguaje de consulta para APIs que permite pedir solo lo que necesitas.

---

## Ejemplo de consulta
```graphql
query {
  productos {
    id
    nombre
    precio
  }
}
```
Ejemplo de mutación
```
mutation {
  agregarProducto(
    nombre: "Monitor", 
    descripcion: "Monitor LED", 
    precio: 200.00, 
    stock: 15, 
    categoria_id: 1
  ) {
    id
    nombre
  }
}

```

