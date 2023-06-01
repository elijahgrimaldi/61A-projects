const express = require("express");
const app = express();

app.get("/", function(req,res){
    res.send("<h1>Hello World!</h1>")
})
app.get("/contact", function(req,res){
    res.send("Contact me at: iadwind@gmail.coms")
})
app.get("/about", function(req,res){
    res.send("Software Developer")
})
app.get("/hobbies", function(req,res){
    res.send("<ul><li>Coding</li></ul>")
})
app.listen(3000, function(){
    console.log("server started on port 3000")
});