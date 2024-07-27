const express = require("express");
const port = 8080;
const App = express()

App.get("/api/boom",(req,res) =>{
    res.send("This is the first api you visit!");
});

App.listen(port, () =>{
    console.log(`Backend Server is running on port ${port}`);
});