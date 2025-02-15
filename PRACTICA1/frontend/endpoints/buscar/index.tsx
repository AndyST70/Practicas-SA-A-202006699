import {url} from 'endpoints';

export const Buscar = (form) => {
    return fetch(url + 'buscarproducto',{
        method: "POST",
        body : form
    }).then(res => res.json());

}