import {url} from 'endpoints';

export const MostrarProductos = async () => {
    return fetch(url + 'mostrarproductos',{
        method: "GET"
    }).then(res => res.json());
}