import express from "express";
import { agregarProducto } from "../controllers/productoController.js";

const router = express.Router();
router.post("/", agregarProducto);

export default router;
