import { AppRouterCacheProvider } from '@mui/material-nextjs/v13-appRouter';
import { ThemeProvider } from '@mui/material/styles';
import { CssBaseline } from '@mui/material';
import { SesionProvider } from 'context';
import theme from 'theme';

import Layout from 'layout/mainLayout';



export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <SesionProvider>
        <AppRouterCacheProvider>
          <ThemeProvider theme={theme}>
            <CssBaseline/>
            <Layout>
            {children}
            </Layout>
          </ThemeProvider>
        </AppRouterCacheProvider>
        </SesionProvider>
      </body>
    </html>
  );
}
