import {url} from 'endpoints';
{/* endpoint para eliminar productos*/}
export const eliminar = async (form) => {
    return fetch(url + 'eliminar',{
        method: "POST",
        body : form
    }).then(res => res.json());
} 