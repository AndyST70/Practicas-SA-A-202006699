import db from "../config/db.js";
// import { Producto } from "../models/producto.js";

export const obtenerProductos = async (req, res) => {
  const [rows] = await db.execute("SELECT * FROM productos");
  // res.json(rows.map(row => new Producto(row.id, row.nombre, row.precio)));
  return rows;
};
