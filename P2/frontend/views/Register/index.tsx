"use client";
import { useState } from "react";
import { register } from "endpoints/register";
import { useRouter } from "next/navigation";
import { Typography, TextField, Button, Stack, Paper } from "@mui/material";

const Register = () => {
    const [form, setForm] = useState({ email: "", password: "", nombre: "" });
    const [message, setMessage] = useState("");
    const router = useRouter();

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        Object.keys(form).forEach((key) => formData.append(key, form[key]));

        const response = await register(formData);
        setMessage(response.message);
        
        if (!response.error) {
            setTimeout(() => router.push("/login"), 2000); // 🔹 Redirigir al login después de éxito
        }
    };

    return (
        <Stack alignItems="center" justifyContent="center" sx={{ height: "100vh" }}>
            <Paper elevation={3} sx={{ padding: 4, width: "60%" }}>
                <Typography variant="h4" textAlign="center" gutterBottom>
                    Registro
                </Typography>
                {message && <Typography color="success.main" textAlign="center">{message}</Typography>}
                <Stack component="form" onSubmit={handleSubmit} spacing={2}>
                    <TextField label="Nombre" name="nombre" fullWidth required onChange={handleChange} />
                    <TextField label="Correo electrónico" name="email" type="email" fullWidth required onChange={handleChange} />
                    <TextField label="Contraseña" name="password" type="password" fullWidth required onChange={handleChange} />
                    <Button type="submit" variant="contained" fullWidth>Registrar</Button>
                    <Button variant="outlined" fullWidth onClick={() => router.push("/login")} sx={{ mt: 1 }}>
                        Volver al Login
                    </Button>
                </Stack>
            </Paper>
        </Stack>
    );
};

export default Register;
