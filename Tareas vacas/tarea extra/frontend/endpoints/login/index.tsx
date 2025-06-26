import {url} from 'endpoints'

export const registrar = async ({ name, email, password }) => {
  return fetch(url + "/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name, email, password }),
    credentials: "include",
  }).then(res => res.json());
};

export const login = async ({ email, password }) => { //para soportar json error de la correccion
  return fetch(url + "/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
    credentials: "include",
  }).then(res => res.json());
};
// 