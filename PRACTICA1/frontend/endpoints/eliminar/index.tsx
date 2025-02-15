import {url} from 'endpoints';

export const eliminar = async (form) => {
    return fetch(url + 'eliminar',{
        method: "POST",
        body : form
    }).then(res => res.json());
} 