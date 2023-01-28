import React from "react";
import { Google_auth } from "./auth/google/google_auth";
import { ListaProductosUSer } from "./productos/lista_producto_user";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

export const Inicio2=()=>{
    
    
    
    return(
        <>
            <h1> Pagina de inicio para Firebase </h1>
            <h3>Front para la Autenticación</h3>
            <div>
                <h2> Ingrese con su cuenta de </h2>
                <Google_auth/>
                
            </div>
            <br />
            <Stack direction="row" spacing={2}>
                <Button color="secondary">Secondary</Button>
                <Button variant="contained" color="success">
                    Success
                </Button>
                <Button variant="outlined" color="error">
                    Error
                </Button>
            </Stack>

        </>
    )
}