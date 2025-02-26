import {url} from 'endpoints'


export const login = async(form)=>{
    return fetch(url + "/login", {
        method: "POST",
        body : form,
        credentials: "include",
    }) .then((response) => response.json()) 
}


export const verify_session = async () => {
    return fetch(url + "/verify_session", {
        method: "GET",
        credentials: "include",
    }) .then((response) => response.json()) 
}

export const logout = async () => {
    return fetch(url +"/logout", {
        method: "POST",
        credentials: "include",
    }).then((response) => response.json());
};
