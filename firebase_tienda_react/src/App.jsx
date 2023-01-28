import { useState } from 'react'
import reactLogo from './assets/react.svg'
//import './App.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { Inicio } from './Inicio'
import { ListaProductosUSer } from './componets/productos/lista_producto_user'

function App() {
  
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element= {<Inicio />}/>
          <Route path="/productos/usuario/lista/" element={<ListaProductosUSer/>}/>
        </Routes>
      </BrowserRouter>

    </>
    
  )
}

export default App
