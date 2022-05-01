import React from "react";
import ReactDOM from 'react-dom/client';
import './App.css';
import Car from "./Sales/Car";
import Chicken from "./Sales/Chicken";
import Login from "./Sales/Login";

function sayHello() {
    alert('Yes!');
}

function App() {
    // return (

    //     <
    //     div >
    //     <
    //     button onClick = { sayHello } >
    //     Is Hailey gay ?
    //     <
    //     /button> < /
    //     div >

    // );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render( < Login / > );
export default App;
