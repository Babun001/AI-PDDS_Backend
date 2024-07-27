const express = require("express");
const request = require('request');
const port = 8080;
const App = express()

App.get("/api/boom",(req,res) =>{
    res.send("This is the first api you visit!");
});

App.get("/api/diabetes",(req,res) => {
    request('http://localhost:5000/diabetes', (err,response) => {
        console.error("error: ", err);
        console.log("response: ", response);
    })
})

App.listen(port, () =>{
    console.log(`Backend Server is running on port ${port}`);
});