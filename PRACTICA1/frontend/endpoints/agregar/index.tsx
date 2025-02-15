import {url} from 'endpoints';

export const Agregar = (form) => {
    return fetch(url + 'agregar_producto',{
        method: "POST",
        body : form
    }).then(res => res.json());
}


