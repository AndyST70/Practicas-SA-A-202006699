'use client'

import { ThemeProvider } from '@mui/material';
import { orange } from '@mui/material/colors';
import { createTheme } from '@mui/material/styles';
import { ReactNode } from 'react';

import { Montserrat } from 'next/font/google';
import { Pixelify_Sans } from 'next/font/google';

const montserrat = Montserrat({
  weight: ["100", "200", "300", "400", "500", "600", "700", "800", "900"],
  subsets: ["latin"],
  display: "swap",
});

const pixelifySans = Pixelify_Sans({
  weight: ["400", "700"], 
  subsets: ["latin"],
  display: "swap",
});



const themes = {
  verde: {
    primary: "#F8FE29", // Componentes
    secondary: "#5BAB3C", // extra
    background: "#091b11", //fondo
    text: "#C8F424" // texto
  },
  morado: {
    primary: "#f1d0ff", // Componentes
    secondary: "#15151e", // extra a593ba
    background: "#15151e", //fondo
    text: "#000000" // texto
    // 15151e negro
    // 383647 gris
    // 68607b gris más claro
    // a593ba morado pastel
    // f1d0ff morado claro
  },
  naranja: {
    primary: "#ff7d39", // Componentes 000000
    secondary: "#ffab2a", // extra
    background: "#fffbdd", //fondo
    text: "#000000" // texto
  },

  azul : {
    primary: "#3a86ff", // Componentes 000000
    secondary: "#adb5bd", // extra
    background: "#001123", //fondo
    text: "#000000" // texto
  },

  rojo : {
    primary: "#e63946", // Componentes
    secondary: "#1d3557", // extra
    background: "#000000", // fondo
    text: "#ffffff", // texto
  }
};


const createCustomTheme = (themeName: string) => {
  const currentTheme = themes[themeName] || themes.verde;

  return createTheme({
    palette: {
      primary: {
        main: currentTheme.primary,
      },
      secondary: {
        main: currentTheme.secondary,
      },
      background: {
        default: currentTheme.background,
      },
      text: {
        primary: currentTheme.text,
      },
      // danger: orange[500],
    },
    typography: {
      fontFamily: montserrat.style.fontFamily, 
    },
  });
};


interface MuiThemeProps {
  children: ReactNode;
  themeName: string; 
}


const MuiTheme = ({ children, themeName }: MuiThemeProps) => {
  const theme = createCustomTheme(themeName);

  return (
    <ThemeProvider theme={theme}>
      {children}
    </ThemeProvider>
  );
};

export default MuiTheme;