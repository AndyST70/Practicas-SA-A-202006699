import express from "express";
import cors from "cors";
import productoRoutes from "./src/routes/productoRoutes.js";
import { graphqlHTTP } from "express-graphql";
import { schema, root } from "./graphql/schema.js";

const app = express();
app.use(cors());
app.use("/graphql", graphqlHTTP({ schema, rootValue: root, graphiql: true }));
// app.use(express.json());

app.use("/productos", productoRoutes);

// app.listen(process.env.PORT, () => console.log(`Servidor en http://localhost:${process.env.PORT}`));


// const PORT = process.env.PORT || 4000; // Se ejecuta en 4000 por defecto
// app.listen(PORT, () => console.log(`Servidor en http://localhost:${PORT}`));
app.listen(4000, () => console.log("Catalogo GraphQL en http://localhost:4000/graphql"));

