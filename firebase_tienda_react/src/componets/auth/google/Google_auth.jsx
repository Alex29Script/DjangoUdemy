import React from "react";

// Apps googles for auth with firebase
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { GoogleAuthProvider } from "firebase/auth";
import { getAuth, signInWithPopup} from "firebase/auth";
import { redirect } from "react-router-dom";


const auth2Google=()=>{
    const firebaseConfig = {
        apiKey: "AIzaSyAVHa-C9WOlGD5e7uNJprsEosYAk6QvGGQ",
        authDomain: "djangoventasudemy.firebaseapp.com",
        projectId: "djangoventasudemy",
        storageBucket: "djangoventasudemy.appspot.com",
        messagingSenderId: "421752348920",
        appId: "1:421752348920:web:4226133eab23dbad0a9b0d",
        measurementId: "G-H1TXKX4B4Q"
    };
    const app = initializeApp(firebaseConfig);
    //const analytics = getAnalytics(app);
    const provider = new GoogleAuthProvider();



    const auth = getAuth();
    signInWithPopup(auth, provider)
    .then((result) => {
        // This gives you a Google Access Token. You can use it to access the Google API.
        const credential = GoogleAuthProvider.credentialFromResult(result);
        const token = credential.accessToken;
        // The signed-in user info.
        const user = result.user;
        console.log(user)
        // ...

        user.getIdToken().then(
            function(idToken){
              console.log("$$$$$$$$$$$$$ Token $$$$$$$$$$$")
              console.log(idToken)
              fetch("http://127.0.0.1:8000/api/google/login/",{
                headers:{"Content-Type":"application/json"},
                mode: 'cors',
                method:"POST",
                body: JSON.stringify({"token_id":idToken})
                }).then(res=>res.json())
                .then(res=>{
                  localStorage.setItem('email', res.user.email)
                  localStorage.setItem('full_name', res.user.full_name)
                  localStorage.setItem('token', res.token)
                  window.location.href='/productos/usuario/lista/'
                  
                })//.then(")
                .catch(error=>{console.log(error)})
            }
          ).catch(function(error){
            console.log(error)
        })



    }).catch((error) => {
        // Handle Errors here.
        const errorCode = error.code;
        const errorMessage = error.message;
        // The email of the user's account used.
        const email = error.customData.email;
        // The AuthCredential type that was used.
        const credential = GoogleAuthProvider.credentialFromError(error);
        // ...
  });
}

export const Google_auth=()=>{

  const login=()=>{
    auth2Google()
  }
  return (
    <>
    {/* 
    */}
    <div className="cocontainer">
      <div className="row">
        <div class="col-5">
          2 of 3 (wider)
          <div>
                <button type="button" class="btn btn-danger" onClick={login}>
                  Gmail
                </button>
          </div>
        </div>
        <div class="col-8">
          2 of 3 (wider)
          <div>
                <button onClick={login}>
                  Ingrese con Gmail
                </button>
          </div>
        </div>
      </div>
    </div>


    </>
  )
}