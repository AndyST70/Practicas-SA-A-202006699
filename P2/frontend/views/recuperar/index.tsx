"use client";
import { useState } from "react";
import { recuperar } from "endpoints/recuperar";
import { useRouter } from "next/navigation";
import { Typography, TextField, Button, Stack, Paper } from "@mui/material";

const Recuperar = () => {
    const [form, setForm] = useState({ email: "", new_password: "" });
    const [message, setMessage] = useState("");
    const router = useRouter();

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        Object.keys(form).forEach((key) => formData.append(key, form[key]));

        const response = await recuperar(formData);
        setMessage(response.message);

        if (!response.error) {
            setForm({ email: "", new_password: "" }); // 🔹 Limpia el formulario después de éxito
            setTimeout(() => router.push("/login"), 2000); // 🔹 Redirigir al login después de éxito
        }
    };

    return (
        <Stack alignItems="center" justifyContent="center" sx={{ height: "100vh" }}>
            <Paper elevation={3} sx={{ padding: 4, width: "100%" }}>
                <Typography variant="h4" textAlign="center" gutterBottom>
                    Recuperar Contraseña
                </Typography>
                {message && <Typography color={message.includes("Error") ? "error" : "success.main"} textAlign="center">{message}</Typography>}
                <Stack component="form" onSubmit={handleSubmit} spacing={2}>
                    <TextField 
                        label="Correo electrónico" 
                        name="email" 
                        type="email" 
                        fullWidth 
                        required 
                        value={form.email} 
                        onChange={handleChange} 
                    />
                    <TextField 
                        label="Nueva Contraseña" 
                        name="new_password" 
                        type="password" 
                        fullWidth 
                        required 
                        value={form.new_password} 
                        onChange={handleChange} 
                    />
                    <Button type="submit" variant="contained" fullWidth>
                        Actualizar Contraseña
                    </Button>
                    <Button variant="outlined" fullWidth onClick={() => router.push("/login")} sx={{ mt: 1 }}>
                        Volver al Login
                    </Button>
                </Stack>
            </Paper>
        </Stack>
    );
};

export default Recuperar;
