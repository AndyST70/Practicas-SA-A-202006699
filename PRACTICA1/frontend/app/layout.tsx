import { AppRouterCacheProvider } from '@mui/material-nextjs/v13-appRouter';
import { CssBaseline } from '@mui/material';

import MuiTheme from 'src/styles/MuiTheme';

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <AppRouterCacheProvider>
             <MuiTheme themeName="azul" >  {/* importacion de tema a trabajar*/}
              <CssBaseline/>
                  {children}
            </MuiTheme>            
        </AppRouterCacheProvider>
      </body>
    </html>
  );
}