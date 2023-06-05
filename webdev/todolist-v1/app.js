const express = require("express")
const path = require('path')
const bodyParser = require("body-parser")
const date = require(__dirname+"/date.js")

const app = express()
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({extended : true}))
app.use(express.static(__dirname + '/public'));

let newItems = []
let workItems = []
app.get("/", function(req,res){
    let day = date.getDate()
    res.render("list", {listTitle : day, newItems:newItems, route:"/"})
    
})

app.post("/", function(req,res){
    let newItem = req.body.toDoItem

    newItems.push(newItem)

    res.redirect("/")
})

app.get("/work", function(req,res){
    res.render("list", {listTitle : "Work List", newItems:workItems, route:"/work"})
})

app.post("/work", function(req,res){
    let workItem = req.body.toDoItem
    workItems.push(workItem)
    res.redirect("/work")
})
app.get("/about", function(req,res){
    res.render("about")
})



app.listen(3000, function(){
    console.log("App running on port 3000")
})