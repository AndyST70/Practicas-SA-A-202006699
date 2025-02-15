import {url} from 'endpoints';

export const eliminar = async (form) => {
    return fetch(url + 'eliminar',{
        method: "DELETE",
        body : form
    }).then(res => res.json());
} 