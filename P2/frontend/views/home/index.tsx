'use client'

import { useEffect, useState } from 'react';

import ProductTable from './components';
import {
  Container,
  Typography,
  TextField,
  Button,
  Stack,
  Alert,
  TablePagination,
  Paper
} from '@mui/material';

export default function HomeView() {
 //  para mostrar productos
  const [productos, setProductos] = useState([]);
  const [filteredProductos, setFilteredProductos] = useState([]);

 // para agregar productos
  const [nombre, setNombre] = useState("");
  const [cantidad, setCantidad] = useState("");
  const [precio, setPrecio] = useState("");
  const [mensaje, setMensaje] = useState("");

 // para buscar productos
  const [search, setSearch] = useState("");
  const [searchMensaje, setSearchMensaje] = useState("");

 // paginacion
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);



  return (
    <Container sx={{ mt: 4 }}>
      <Stack spacing={4}>

        <Paper sx={{ p: 2 }}>
          <Stack spacing={2}>
            
            <form >
              <Stack direction="row" spacing={2} alignItems="center">
                <TextField
                  label="Nombre"

                  sx={{ flex: 1 }}
                />
                <TextField
                  label="Cantidad"
                  type="number"
               
                  sx={{ flex: 1 }}
                />
                <TextField
                  label="Precio"
                  type="number"
                  
                  sx={{ flex: 1 }}
                />
                <Button variant="contained" color="primary" type="submit">
                  Agregar
                </Button>
              </Stack>
            </form>
          </Stack>
        </Paper>


        <Paper sx={{ p: 2 }}>
          <Stack spacing={2}>
            <Typography variant="h5">Buscar Producto</Typography>
            <form >
              <Stack direction="row" spacing={2} alignItems="center">
                <TextField
                  label="Buscar"
                 
                  onChange={(e) => {
                 
                  }}
                  sx={{ flex: 1 }}
                />
                <Button variant="contained" color="secondary" type="submit">
                  Buscar
                </Button>
               
                <Button variant="outlined" >
                  Ordenar por Precio
                </Button>
                <Button variant="outlined" >
                  Ordenar por Cantidad
                </Button>
              </Stack>
            </form>
           
          </Stack>
        </Paper>


        
      </Stack>
    </Container>
  );

}