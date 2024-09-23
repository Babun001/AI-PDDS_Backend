const express = require("express");
const cors = require("cors");
const request = require('request');
const port = 8080;
const App = express()

App.use(cors({ origin: '*' }))


App.get("/api/db", (req, res) => {
    const queryParams = req.query;
    console.log(queryParams);

    const URL = (`http://127.0.0.1:5000/diabetes?${new URLSearchParams(queryParams).toString()}`);
    console.log(`The URL you get =>>>`,URL);
    request(URL, (err, response, body) => {
        if (err) {
            console.error("Error: ", err);
            res.status(500).send("Error occurred while fetching data from flask API.");
        } else {
            console.log("Body: ", body);
            res.send(body);
        }
    });
})

App.get("/api/lv", (req, res) =>{
    const lvQuaryParams = req.query;
    // console.log(lvQuaryParams);
    const URLlv = (`http://127.0.0.1:5000/liver?${new URLSearchParams(lvQuaryParams).toString()}`);

    request(URLlv, (err, response, body) =>{
        if(err){
            console.error("Error: ", err);
            res.status(500).send("Error occurred while fetching data from flask API.");
        }
        console.log("data fetching succesful!");
        console.log("Body: ", body);
        res.send(body);
    })
})  

App.listen(port, () => {
    console.log(`Backend Server is running on port http://127.0.0.1:${port}`);
});