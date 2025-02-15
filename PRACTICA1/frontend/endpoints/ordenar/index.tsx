import {url} from 'endpoints';

export const OrdenarPorCantidad = async () => {
    return fetch(url + 'ordenarxcantidad',{
        method: "GET"
    }).then(res => res.json());
}

export const OrdenarPorPrecio = async () => {
    return fetch(url + 'ordenarxprecio',{
        method: "GET"
    }).then(res => res.json());
}