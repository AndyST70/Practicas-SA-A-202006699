import { Button, Container, Table, TableHead, TableRow, TableCell, TableBody, Typography } from '@mui/material';

export default function ProductTable({ productos, onProductoEliminado }) {
  return (
    <Container>
      <Typography variant="h5" sx={{ color: 'text.primary', mb: 2 }}>
        Lista de Productos
      </Typography>
      <Table>
        <TableHead sx={{ backgroundColor: 'primary.main' }}>
          <TableRow>
            <TableCell sx={{ color: 'text.primary' }}>ID</TableCell>
            <TableCell sx={{ color: 'text.primary' }}>Nombre</TableCell>
            <TableCell sx={{ color: 'text.primary' }}>Cantidad</TableCell>
            <TableCell sx={{ color: 'text.primary' }}>Precio</TableCell>
            <TableCell sx={{ color: 'text.primary' }}>Eliminar</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {productos.map((p) => (
            <TableRow key={p.id}>
              <TableCell>{p.id}</TableCell>
              <TableCell>{p.nombre}</TableCell>
              <TableCell>{p.cantidad}</TableCell>
              <TableCell>{p.precio}</TableCell>
              <TableCell>
                <Button variant="contained" color="error" onClick={() => onProductoEliminado(p.nombre)}>
                  Eliminar
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Container>
  );
}
