import {url} from 'endpoints';
{/* endpoint para ordenar productos por cantidad*/}
export const OrdenarPorCantidad = async () => {
    return fetch(url + 'ordenarxcantidad',{
        method: "GET"
    }).then(res => res.json());
}
{/* endpoint para ordenar productos por precio*/}
export const OrdenarPorPrecio = async () => {
    return fetch(url + 'ordenarxprecio',{
        method: "GET"
    }).then(res => res.json());
}