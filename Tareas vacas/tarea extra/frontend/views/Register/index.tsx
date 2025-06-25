import React, { useState } from 'react';
import { TextField, Button, Typography, Box } from '@mui/material';
import { registrar } from 'endpoints/login';

export default function Register() {
  const [form, setForm] = useState({ name: '', email: '', password: '' });
  const [msg, setMsg] = useState({ text: '', error: false });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    const { name, email, password } = form;
    if (!name || !email || !password) {
      setMsg({ text: 'Todos los campos son obligatorios', error: true });
      return;
    }


     // correccion a codigo tipo JSON no form
    const res = await registrar({ name, email, password });
    setMsg({
      text: res.message || res.error || 'Error desconocido',
      error: !res.message,
    });
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center">
      <Typography variant="h6">Registro</Typography>
      <TextField label="Nombre" name="name" fullWidth margin="normal"  sx={{ m: 1, width: '45ch' }} onChange={handleChange} />
      <TextField label="Correo" name="email" fullWidth margin="normal" sx={{ m: 1, width: '45ch' }}  onChange={handleChange} />
      <TextField label="Contraseña" name="password" type="password" fullWidth margin="normal"  sx={{ m: 1, width: '45ch' }}onChange={handleChange} />
      <Button variant="contained" onClick={handleSubmit}>Registrarse</Button>
      {msg.text && (
        <Typography mt={2} color={msg.error ? 'error.main' : 'success.main'}>
          {msg.text}
        </Typography>
      )}
        <Typography mt={2} variant="body2" color="textSecondary">
            Ya tienes cuenta? <a href="/login">Inicia sesión</a>
        </Typography>

    </Box>
  );
}
