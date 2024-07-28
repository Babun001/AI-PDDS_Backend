const express = require("express");
const cors = require("cors");
const request = require('request');
const port = 8080;
const App = express()

App.use(cors({origin: '*'}))

App.get("/",(req,res) =>{
    res.send("This is the first api you visit!");
});

App.get("/api/diabetes",(req,res) => {
    request('http://localhost:5000/diabetes', (err,response,body) => {
        console.error("error: ", err);
        // console.log("Status code: ", response.statusCode);
        console.log("Body: ", body);
        res.send(body);
    })
    // res.send("diabetes api done!");
})

App.get("/api/db", (req, res) => {
    const queryParams = req.query;
    const url = `http://localhost:5000/diabetes?${new URLSearchParams(queryParams).toString()}`;
    
    // res.send(queryParams);

    request(url, (err, response, body) => {
        if (err) {
            console.error("Error: ", err);
            res.send(queryParams);
            res.status(500).send("Error occurred while fetching data from the diabetes API.");
        } else {
            console.log("Body: ", body);
            // res.send("Body: ", body);
            // res.send(body);
        }
    });

});

App.listen(port, () =>{
    console.log(`Backend Server is running on port http://127.0.0.1:${port}`);
});