import {url} from 'endpoints'
export const register = async(form)=>{
    return fetch(url + "/register", {
        method: "POST",
        body : form
    }) .then((response) => response.json()) 
}