"use client";
import { createContext, useState, useEffect } from "react";
import { verify_session } from "endpoints/login";
import { useRouter, usePathname } from "next/navigation";

export const SesionContext = createContext(null);

export const SesionProvider = ({ children }) => {
    const [usuario, setUsuario] = useState(null);
    const [loading, setLoading] = useState(true);
    const router = useRouter();
    const path = usePathname(); // 🔹 Obtiene la ruta actual

    const paginasPublicas = ["/login", "/registrar", "/recuperar"]; // 🔹 Rutas que no requieren sesión

    useEffect(() => {
        async function verificarSesion() {
            const response = await verify_session();
            if (!response.error) {
                setUsuario(response.user);
            } else {
                setUsuario(null);
                if (!paginasPublicas.includes(path)) {
                    router.replace("/login"); // 🔹 Solo redirigir si NO está en una página pública
                }
            }
            setLoading(false);
        }
        verificarSesion();
    }, []);

    if (loading) return null; // 🔹 Evita renderizar contenido antes de verificar la sesión

    return (
        <SesionContext.Provider value={{ usuario, setUsuario }}>
            {children}
        </SesionContext.Provider>
    );
};
