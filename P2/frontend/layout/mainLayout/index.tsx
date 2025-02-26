"use client";
import { useContext, useEffect } from "react";
import { SesionContext } from "context";
import { useRouter, usePathname } from "next/navigation";
import { Stack, Paper, Box } from "@mui/material";
import SideBar from "./components/sideBar";

const MainLayout = ({ children }) => {
    const { usuario, loading } = useContext(SesionContext);
    const router = useRouter();
    const path = usePathname();
    const paginasPublicas = ["/login", "/register", "/recuperar"];

    useEffect(() => {
        if (!loading && usuario === null && !paginasPublicas.includes(path)) {
            router.replace("/login"); // 🔹 Solo redirigir si es una página privada
        }
    }, [usuario, loading]);

    if (loading) return null; // 🔹 No mostrar nada hasta que la sesión esté validada

    return (
        <Stack sx={{ height: "100vh", width: "100vw", justifyContent: "center", alignItems: "center" }}>
            {paginasPublicas.includes(path) ? (
                children // 🔹 Permite mostrar login, register y recuperar sin layout
            ) : (
                <Paper sx={{ width: "90%", height: "90%", borderRadius: 4, overflow: "hidden" }} elevation={4}>
                    <Stack direction="row" sx={{ height: "100%" }}>
                        <Box sx={{ height: "100%", bgcolor: "skyblue" }}>
                            <SideBar />
                        </Box>
                        <Box sx={{ height: "100%", flex: 1, overflow: "auto" }}>{children}</Box>
                    </Stack>
                </Paper>
            )}
        </Stack>
    );
};

export default MainLayout;
