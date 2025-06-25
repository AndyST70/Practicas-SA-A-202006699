"use client"
import { Montserrat } from 'next/font/google';
import { createTheme } from '@mui/material/styles';

const montserrat = Montserrat({
  weight: ["100", "200", "300", "400", "500", "600", "700", "800", "900"],
  subsets: ["latin"],
  display: "swap",
});

const theme = createTheme({
  palette: {
    background:{
      default: '#e8e8e8',
    },
  },
  typography: {
    fontFamily: montserrat.style.fontFamily,
  }
});

export default theme;