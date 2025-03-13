import { buildSchema } from "graphql";
import { obtenerProductos } from "../src/controllers/productoController.js";

export const schema = buildSchema(`
  type Producto {
    id: ID!
    nombre: String!
    descripcion: String
    precio: Float!
    stock: Int!
    categoria_id: Int
  }

  type Query {
    productos: [Producto]
  }
`);

export const root = {
  productos: obtenerProductos
};
