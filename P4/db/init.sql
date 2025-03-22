CREATE DATABASE IF NOT EXISTS catalogo_db;
USE catalogo_db;


CREATE SCHEMA IF NOT EXISTS `catalogo_db` DEFAULT CHARACTER SET utf8 ;

-- Tabla de Categorías
CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de Productos
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE SET NULL
);

-- Tabla de Usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) UNIQUE NOT NULL,
    contrasenia VARCHAR(255) NOT NULL,
    logueado TINYINT
);

-- Tabla de Pedidos
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

-- Tabla Intermedia: Detalles del Pedido
CREATE TABLE detalles_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE
);

-- Insertando Categorías de Ejemplo
INSERT INTO categorias (nombre) VALUES ('Electrónica'), ('Ropa'), ('Hogar');

-- Insertando Productos de Ejemplo
INSERT INTO productos (nombre, descripcion, precio, stock, categoria_id) 
VALUES 
    ('Laptop', 'Laptop de alta gama', 1200.00, 10, 1),
    ('Camiseta', 'Camiseta de algodón', 25.00, 50, 2),
    ('Silla', 'Silla ergonómica de oficina', 150.00, 20, 3);
