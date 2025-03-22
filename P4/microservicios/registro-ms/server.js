import express from "express";
import cors from "cors";
import { graphqlHTTP } from "express-graphql";
import { schema, root } from "./graphql/schema.js";

// import registroRoutes from "./src/routes/registroRoutes.js";
const app = express();
app.use(cors());
// app.use(express.json());
app.use("/graphql", graphqlHTTP({ schema, rootValue: root, graphiql: true }));

// app.use("/registro", registroRoutes);

// app.listen(process.env.PORT, () => console.log(`Servidor en http://localhost:${process.env.PORT}`));

// const PORT = process.env.PORT || 4001; 
// app.listen(PORT, () => console.log(`Servidor en http://localhost:${PORT}`));
app.listen(4001, () => console.log("Registro GraphQL en http://localhost:4001/graphql"));
