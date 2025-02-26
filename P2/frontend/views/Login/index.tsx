"use client";
import { useState, useEffect } from "react";
import { login, verify_session } from "endpoints/login";
import { useRouter } from "next/navigation";
import { Typography, Avatar, TextField, Button, Stack, Link} from "@mui/material";
import PetsOutlinedIcon from "@mui/icons-material/PetsOutlined";

const LoginView = () => {
    const [errorMessage, setErrorMessage] = useState("");
    const router = useRouter();

    //  Verificar si el usuario ya está autenticado al cargar la página
    useEffect(() => {
        async function checkAuth() {
            const response = await verify_session();
            
            if (response.error === 0) {
                router.push("/home");  
            }
        }
        checkAuth();
    }, []);

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData(event.currentTarget); // Captura el formulario completo
        try {
            const response = await login(formData); 
            if (response.error === 0) {
                router.push("/home");  
            } else {
                setErrorMessage(response.message); // Muestra el mensaje de error si `error === 1`
            }
        } catch (error) {
            console.error("Error en login:", error);
            setErrorMessage("Error de conexión con el servidor.");
        }
    };

    return (
        <Stack component="form" onSubmit={handleSubmit} sx={{ width: "60%", mt: 1 }} alignItems="center">
            <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
                <PetsOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5" sx={{ mb: 2, fontSize: "3rem" }}>
                Log in
            </Typography>
            {errorMessage && <Typography color="error">{errorMessage}</Typography>}
            <TextField required fullWidth label="Correo electrónico" name="email" type="email" autoFocus />
            <TextField required fullWidth label="Contraseña" name="password" type="password" />
            <Button type="submit" variant="contained" sx={{ width: "200px", m: 3 }}>
                Ingresar
            </Button>
            {/* 🔹 Botón de Registro */}
            <Link component="button" onClick={() => router.push("/registrar")} sx={{ mt: 2, cursor: "pointer" }}>
                ¿No tienes cuenta? Regístrate aquí
            </Link>
            {/* 🔹 Botón de Recuperar Contraseña */}
            <Link component="button" onClick={() => router.push("/recuperar")} sx={{ mt: 2, cursor: "pointer" }}>
                ¿Olvidaste tu contraseña? Recuperar aquí
            </Link>
        </Stack>
    );
};

export default LoginView;
