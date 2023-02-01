import React from 'react';
import { useState } from 'react';
import {Google_auth} from './componets/auth/google/Google_auth'


export const Inicio=()=> {
  
  const[ElegirBInicio, setElegirBInicio]=useState("ninguno")
  

  
  return (
    <>
      <div className="container text-center">
      <div className="row">
        <div className="col-12">
          <span className="badge text-bg-primary">Pagina inicio</span>
          <div className="d-flex align-items-start">
              <div className="nav flex-column nav-pills me-3" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                <button className="nav-link active" id="v-pills-home-tab" data-bs-toggle="pill" data-bs-target="#v-pills-home" type="button" role="tab" aria-controls="v-pills-home" aria-selected="true">Login</button>
                <button className="nav-link" id="v-pills-profile-tab" data-bs-toggle="pill" data-bs-target="#v-pills-profile" type="button" role="tab" aria-controls="v-pills-profile" aria-selected="false">Productos</button>
                <button className="nav-link" id="v-pills-disabled-tab" data-bs-toggle="pill" data-bs-target="#v-pills-disabled" type="button" role="tab" aria-controls="v-pills-disabled" aria-selected="false">Venta</button>
              </div>
              <div className="tab-content" id="v-pills-tabContent">
                <div className="tab-pane fade show active" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab" tabindex="0"><Google_auth/></div>
                <div className="tab-pane fade" id="v-pills-profile" role="tabpanel" aria-labelledby="v-pills-profile-tab" tabindex="0"> <p>segunda</p></div>
                <div className="tab-pane fade" id="v-pills-disabled" role="tabpanel" aria-labelledby="v-pills-disabled-tab" tabindex="0"><p>tercera</p></div>
              </div>
            </div>

        </div>
        <div className="col-8">
        <span className="badge text-bg-primary">Segunda</span>
        </div>
      </div>

        
      </div>
    </>
  );
}