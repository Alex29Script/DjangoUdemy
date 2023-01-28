import React, { useEffect, useState } from "react";


export const ListaProductosUSer = () =>{
    const[Productos,setProductos]=useState([])
    let token, email, full_name
    
    if(localStorage.getItem('token')){
        token = localStorage.getItem('token')
        email= localStorage.getItem('email')
        full_name= localStorage.getItem('full_name')
    }else{
        token="indefinido"
    }

    useEffect(()=>{
        fetch('http://127.0.0.1:8000/productos/listar/todos',{
        headers:{"Content-Type":"application/json",'Authorization': `token ${token}`},
        mode: 'cors',
        method:"GET",
        
    }).then(res=>res.json())
    .then(res=>{
        console.log(res[0].name)
        setProductos(res)
    })
    },[])
    
    
    return(
        <>
        <h1>Datos de Usuario </h1>
        <h2>Nombre: {full_name}</h2>
        <h2>el email: {email} </h2>
        <h3> le pertenece el token: {token} </h3>
        <h2>le pertenece los siguientes Productos</h2>
        <table>
        <thead>
            <tr>
                <th> Nombre </th>
                <th>Descripcion </th>
            </tr>
        </thead>
        <tbody>
        {
            Productos.map(prod=>
                <tr key={prod.name}>
                <td>{prod.name}</td>
                <td>{prod.description}</td>
                </tr>

            )
        }
        </tbody>
        </table>       
        </>
    )   

}