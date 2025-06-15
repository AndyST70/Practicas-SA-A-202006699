version: '3.8'

services:
  productos-service:
    build:
      context: ./microservicios/productos-service
      args:
        - PORT=5001
    ports:
      - "5001:5001"
    environment:
      - SECRET_KEY=clave123
    depends_on:
      - productos-db

  compras-service:
    build:
      context: ./microservicios/compras-service
      args:
        - PORT=5002
    ports:
      - "5002:5002"
    environment:
      - SECRET_KEY=clave123
    depends_on:
      - compras-db

  usuarios-service:
    build:
      context: ./microservicios/usuarios-service
      args:
        - PORT=5003
    ports:
      - "5003:5003"
    environment:
      - SECRET_KEY=clave123
    depends_on:
      - usuarios-db

  pagos-service:
    build:
      context: ./microservicios/pagos-service
      args:
        - PORT=5004
    ports:
      - "5004:5004"
    environment:
      - SECRET_KEY=clave123
    depends_on:
      - pagos-db

  reportes-service:
    build:
      context: ./microservicios/reportes-service
      args:
        - PORT=5005
    ports:
      - "5005:5005"
    environment:
      - SECRET_KEY=clave123
    depends_on:
      - reportes-db

  # Bases de datos
  productos-db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: productos_db
    volumes:
      - productos_data:/var/lib/mysql

  compras-db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: compras_db
    volumes:
      - compras_data:/var/lib/mysql

  usuarios-db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: usuarios_db
    volumes:
      - usuarios_data:/var/lib/mysql

  pagos-db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: pagos_db
    volumes:
      - pagos_data:/var/lib/mysql

  reportes-db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: reportes_db
    volumes:
      - reportes_data:/var/lib/mysql


  redis:
    image: redis:7
    ports:
      - "6379:6379"

volumes:
  productos_data:
  compras_data:
  usuarios_data:
  pagos_data:
  reportes_data:
