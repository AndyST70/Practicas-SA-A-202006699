import db from "../config/db.js";

export const agregarProducto = async ({ nombre, descripcion, precio, stock, categoria_id }) => {
  try {
    const [result] = await db.execute(
      "INSERT INTO productos (nombre, descripcion, precio, stock, categoria_id) VALUES (?, ?, ?, ?, ?)",
      [nombre, descripcion, precio, stock, categoria_id]
    );
    return { id: result.insertId, nombre, descripcion, precio, stock, categoria_id };
  } catch (error) {
    throw new Error("Error al agregar producto");
  }
};