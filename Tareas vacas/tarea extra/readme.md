#  Tienda en Línea - Autenticación con Flask + React

Aplicación básica de autenticación para una tienda en línea, con backend en **Flask + MySQL** y frontend en **React + Material UI**.

---

## Características

- Registro de usuario con nombre, correo y contraseña.
- Inicio de sesión con validación y manejo de JWT.
- Recuperación de contraseña (mock).
- Interfaz moderna con Material UI.
- Conexión backend-frontend vía `fetch` y `FormData`.

---

##  Tecnologías

### Backend
- Python 3
- Flask (sin Blueprints)
- MySQL
- `mysql-connector-python`
- `hashlib` + JWT para autenticación

### Frontend
- React
- Material UI
- `fetch` + `FormData`
- React Hooks (`useState`)

---

##  Backend: configuración

1. Crear base de datos:
  ```
  CREATE DATABASE onlinestore;
  USE onlinestore;

  CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(64) NOT NULL
  );
  ```

- Instalar dependencias 

```
pip install flask mysql-connector-python pyjwt flask-cors
```

- ejecutar backend

```
python app.py
```

instalar dependencias de fronted
```
npm install
```
correr proyecto frontend
```
npm run dev
```


Notas
- No se usan Blueprints en Flask.

- No se usa Axios, solo fetch + FormData.

- Interfaz 100% responsive con Material UI.

