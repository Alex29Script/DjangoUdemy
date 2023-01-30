import React from "react";

export const NavB=(EleccionB)=>{
    

    switch(EleccionB){
        case "ninguno":
            return(<><h1>Elija una Opcion</h1></>)
        case "userB":
            return(
            <>
                <h1>Usuario</h1>
            </>
            )
        case "productB":
            return(
                <>
                    <h1> Productos </h1>
                </>
            )
        case "ventasB":
            return(
                <>
                    <h1> Ventas </h1>
                </>
            )

    }


}
