'use client'

import { useEffect, useState } from 'react';
import { MostrarProductos } from 'endpoints/mostrar';
import { eliminar } from 'endpoints/eliminar';
import { Agregar } from 'endpoints/agregar';
import { OrdenarPorPrecio, OrdenarPorCantidad } from 'endpoints/ordenar';
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

  useEffect(() => {
    cargarProductos();
  }, []);

  const cargarProductos = async () => {
    const data = await MostrarProductos();
    const prods = data.productos || [];
    setProductos(prods);
    setFilteredProductos(prods);
    setSearchMensaje("");
  };

  const handleEliminar = async (nombreProducto) => {
    const formData = new FormData();
    formData.append("nombre", nombreProducto);
    await eliminar(formData);
    cargarProductos();
  };

  const handleAgregar = async (e) => {
    e.preventDefault();

    if (!nombre || !cantidad || !precio) {
      setMensaje("Todos los campos son obligatorios.");
      return;
    }
    // Crear un objeto FormData
    const formData = new FormData();
    formData.append("nombre", nombre);
    formData.append("cantidad", cantidad);
    formData.append("precio", precio);

    const response = await Agregar(formData);

    if (response.error === 0) {
      setMensaje("Producto agregado exitosamente.");
      setNombre("");
      setCantidad("");
      setPrecio("");
      cargarProductos();
    } else {
      // Mostrar mensaje de error
      setMensaje(response.message);
    }
  };
  const handleBuscar = (e) => {
    e.preventDefault();
    const query = search.toLowerCase().trim();
    if (!query) {

      setFilteredProductos(productos);
      setSearchMensaje("");
      return;
    }
    const filtrados = productos.filter((prod) =>
      prod.nombre.toLowerCase().includes(query)
    );
    setFilteredProductos(filtrados);
    if (filtrados.length === 0) {
      setSearchMensaje("No se encontraron productos.");
    } else {
      setSearchMensaje("");
    }
  };


  const handleOrdenarPorPrecio = async () => {
    const response = await OrdenarPorPrecio();
    if (response.error === 0) {
      setProductos(response.productos || []);
      // Si había resultados de búsqueda, se limpian
      setSearchMensaje("");
    } else {
      setSearchMensaje(response.message || "Error al ordenar por precio.");
    }
  };

  const handleOrdenarPorCantidad = async () => {
    const response = await OrdenarPorCantidad();
    if (response.error === 0) {
      setProductos(response.productos || []);
      setSearchMensaje("");
    } else {
      setSearchMensaje(response.message || "Error al ordenar por cantidad.");
    }
  };
  // Paginación
  const paginatedProductos = filteredProductos.slice(
    page * rowsPerPage,
    page * rowsPerPage + rowsPerPage
  );

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  return (
    <Container sx={{ mt: 4 }}>
      <Stack spacing={4}>

        <Paper sx={{ p: 2 }}>
          <Stack spacing={2}>
            <Typography variant="h5">Agregar Producto</Typography>
            {mensaje && <Alert severity="info">{mensaje}</Alert>}
            <form onSubmit={handleAgregar}>
              <Stack direction="row" spacing={2} alignItems="center">
                <TextField
                  label="Nombre"
                  value={nombre}
                  onChange={(e) => setNombre(e.target.value)}
                  sx={{ flex: 1 }}
                />
                <TextField
                  label="Cantidad"
                  type="number"
                  value={cantidad}
                  onChange={(e) => setCantidad(e.target.value)}
                  sx={{ flex: 1 }}
                />
                <TextField
                  label="Precio"
                  type="number"
                  value={precio}
                  onChange={(e) => setPrecio(e.target.value)}
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
            <form onSubmit={handleBuscar}>
              <Stack direction="row" spacing={2} alignItems="center">
                <TextField
                  label="Buscar"
                  value={search}
                  onChange={(e) => {
                    setSearch(e.target.value);
                    setSearchMensaje("");
                  }}
                  sx={{ flex: 1 }}
                />
                <Button variant="contained" color="secondary" type="submit">
                  Buscar
                </Button>
               
                <Button variant="outlined" onClick={handleOrdenarPorPrecio}>
                  Ordenar por Precio
                </Button>
                <Button variant="outlined" onClick={handleOrdenarPorCantidad}>
                  Ordenar por Cantidad
                </Button>
              </Stack>
            </form>
            {searchMensaje && <Alert severity="warning">{searchMensaje}</Alert>}
          </Stack>
        </Paper>


        <Paper sx={{ p: 2 }}>
          <ProductTable productos={paginatedProductos} onProductoEliminado={handleEliminar} />
          <TablePagination
            rowsPerPageOptions={[5, 10, 100]}
            component="div"
            count={filteredProductos.length}
            rowsPerPage={rowsPerPage}
            page={page}
            onPageChange={handleChangePage}
            onRowsPerPageChange={handleChangeRowsPerPage}
          />
        </Paper>
      </Stack>
    </Container>
  );
}
