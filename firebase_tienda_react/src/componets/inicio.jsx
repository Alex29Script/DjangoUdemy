import React from "react";
import { Google_auth } from "./auth/google/google_auth";


export const Inicio=()=>{
    return(
        <>
        <h1> Pagina de inicio para Firebase </h1>
        <h3>Front para la Autenticación</h3>
        <div>
            <h2> Ingrese con su cuenta de </h2>
            <Google_auth/>
        </div>  
        </>
    )
}