"use client"
import {useContext} from 'react';
import {logout} from 'endpoints/login'

import {
	Stack, 
	Typography, 
	Paper,
	Divider,
	Card,
	CardActionArea
} from '@mui/material';
import LogoutIcon from '@mui/icons-material/Logout';
import { SesionContext } from 'context';

import { usePathname, useRouter } from "next/navigation";

const SideBar = ()=>{
	const {setSesion} = useContext(SesionContext);
	const pathname = usePathname();
	const router = useRouter();

	const handlecerrar = async () => {
		try {
			const response = await logout();
			if (response.error === 0) {
				setSesion(null);
				router.replace("/login");
				setTimeout(() => {
					window.location.reload(); // 🔹 Recarga la página después de redirigir
				}, 100); 
			} else {
				console.error("Error en logout:", response.message);
			}
		} catch (error) {
			console.error("Error al cerrar sesión:", error);
		}
	};
	



	return(
		<Paper elevation={4} square sx={{height: '100%'}}>
			<Stack sx={{height: '100%', width: '20vw'}}>
				<Card variant="outlined" sx={{border: 'none'}}>
					<CardActionArea href='/' >
						<Stack padding={2} direction="row" justifyContent='center' alignItems='center'>
							<Typography variant="h4" sx={{fontWeight: 500}}>Home</Typography>
						</Stack>
					</CardActionArea>
				</Card>

				<Divider/>

				<Stack justifyContent="space-between" sx={{flex: 1}}>
					<Card variant="outlined" sx={{border: 'none'}}>
						<CardActionArea onClick={handlecerrar}>
							<Divider/>
							<Stack direction="row" alignItems='center' padding={2} spacing={2}>
								<LogoutIcon sx={{color: '#f44336'}}/>
								<Typography variant="body1">Cerrar Sesión</Typography>
							</Stack>
						</CardActionArea>
					</Card>
				</Stack>
			</Stack>
		</Paper>
	)
}

export default SideBar;