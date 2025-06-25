import React, { useState } from 'react';
import { TextField, Button, Typography, Box } from '@mui/material';
import { login } from  'endpoints/login';

type Props = {
  onLogin?: (name: string) => void;
};

export default function LoginView({ onLogin }: Props) {
  const [form, setForm] = useState({ email: '', password: '' });
  const [msg, setMsg] = useState({ text: '', error: false });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    const { email, password } = form;
    if (!email || !password) {
      setMsg({ text: 'Todos los campos son obligatorios', error: true });
      return;
    }

    

    const res = await login({ email, password });

    if (res.token) {
      localStorage.setItem('token', res.token);
    onLogin?.(res.name);
      setMsg({ text: `Bienvenido ${res.name}`, error: false });
    } else {
      setMsg({ text: res.error || 'Error en login', error: true });
    }
  };

  return (
    <Box display="flex" flexDirection="column" alignItems="center"> {/* Box para centrar el contenido arreglos propios :D */}

      <Typography variant="h6">Iniciar Sesión</Typography>
      <TextField label="Correo" name="email" fullWidth margin="normal" sx={{ m: 1, width: '45ch' }} onChange={handleChange} />
      <TextField label="Contraseña" name="password" type="password" fullWidth margin="normal"  sx={{ m: 1, width: '45ch' }} onChange={handleChange} />
      <Button variant="contained" onClick={handleSubmit}>Entrar</Button>
      {msg.text && (
        <Typography mt={2} color={msg.error ? 'error.main' : 'success.main'}>
          {msg.text}
        </Typography>
      )}
      <Button onClick={() => window.location.href = '/registrar'} sx={{ mt: 2 }}>
                  ¿No tienes cuenta? Regístrate
    </Button>
    </Box>

  );
}
