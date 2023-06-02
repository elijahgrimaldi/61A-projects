const express = require("express");
const bodyParser = require("body-parser");
const app = express();
app.use(bodyParser.urlencoded({extended : true}))

app.get("/", function(req,res){
    res.sendFile(__dirname + "/index.html")
})
app.post("/", function(req,res){
    let num1 = req.body.num1;
    let num2 = req.body.num2;
    let result = Number(num1)+Number(num2)
    res.send("The result of the calculation is " + result)
})
app.get("/bmicalculator", function(req,res){
    res.sendFile(__dirname + "/bmiCalculator.html")
})
app.post("/bmicalculator", function(req,res){
    let height = req.body.height;
    let weight = req.body.weight;
    let result = weight / Math.pow(height,2)
    res.send("The result of your BMI is " + result)
})
app.listen(3000, function(){
    console.log("server started on port 3000")
});