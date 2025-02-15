import {url} from 'endpoints';
{/* endpoint para mostrar productos*/}
export const MostrarProductos = async () => {
    return fetch(url + 'mostrarproductos',{
        method: "GET"
    }).then(res => res.json());
}