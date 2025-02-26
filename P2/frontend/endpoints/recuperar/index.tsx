import {url} from 'endpoints'
export const recuperar = async(form)=>{
    return fetch(url + "/recuperar", {
        method: "POST",
        body : form
    }) .then((response) => response.json()) 
}