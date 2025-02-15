import {url} from 'endpoints';

{/* endpoint para buscar productos*/}
export const Buscar = (form) => {
    return fetch(url + 'buscarproducto',{
        method: "POST",
        body : form
    }).then(res => res.json());

}