import { buildSchema } from "graphql";
import { agregarProducto } from "../src/controllers/productoController.js";

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
    _: String  # Query vacía para evitar el error
  }

  type Mutation {
    agregarProducto(nombre: String!, descripcion: String, precio: Float!, stock: Int!, categoria_id: Int): Producto
  }
`);

export const root = {
  agregarProducto
};
