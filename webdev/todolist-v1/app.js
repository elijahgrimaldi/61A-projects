const url = "mongodb://127.0.0.1:27017/todolist"
const express = require("express")
const path = require('path')
const bodyParser = require("body-parser")
const mongoose = require("mongoose")
const app = express()
const _ = require("lodash")
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({extended : true}))
app.use(express.static(__dirname + '/public'));


main().catch(err => console.log(err));

async function main() {

await mongoose.connect(url);
// SCHEMAS
const itemsSchema = new mongoose.Schema({
    name: String})

//console.log(await Item.find({}))
const listSchema = new mongoose.Schema({
    name: String,
    items: [itemsSchema]
})
// CREATE COLLECTIONS
const Item = mongoose.model('Item', itemsSchema)
const List = mongoose.model("List", listSchema)



const item1 = new Item({name : "Welome to your to-do list"})
const item2 = new Item({name : "Press the + icon to add a new item"})
const item3 = new Item({name : "<-- Press this to delete an item"})
const defaultItems = [item1,item2,item3]
//await Item.insertMany(defaultItems)


app.get("/", function(req,res){
    Item.find({}).then((currentItems)=>{
       if (currentItems.length === 0){
        Item.insertMany(defaultItems).then(()=>{
        })
        res.redirect("/")
       }else{
        res.render("list", {listTitle : "Today", newItems:currentItems, route:"/"})
       }
    })
    
})

app.post("/", function(req,res){
    let itemName = req.body.toDoItem
    let listName = req.body.list
    const newItem = new Item({name : itemName})
    newItem.save()
    res.redirect("/")
    

})
app.post("/delete", function(req,res){
    const checkedItemID = req.body.checkbox
    const listName = req.body.listName
    if (listName==="Today"){
        Item.findByIdAndRemove(checkedItemID).then(()=>{})
        res.redirect("/")
    } else {
        List.findOneAndUpdate({name : listName},{$pull: {items: {_id:checkedItemID}}}).then((returnList)=>{
            res.redirect("/"+listName)
        })
    }

})

app.get("/:customListName", function(req,res){
    const customListName = _.capitalize(req.params.customListName)
    console.log(customListName)
    List.find({name : customListName}).then((response)=>{
        if (response.length===0){

            //Create new list
            const list = new List({
                name: customListName,
                items : defaultItems
            })
            list.save()
            res.redirect("/"+customListName)
        }else{
            //Show existing list
            res.render("list", {listTitle: response[0].name, newItems:response[0].items, route:"/"+customListName})
        }
    })
    // console.log(defaultItems)

})
app.post("/:customListName", function(req,res){
    let itemName = req.body.toDoItem
    let listName = _.capitalize(req.body.list)
    const newItem = new Item({name : itemName})
    List.findOne({name : listName}).then((returnList)=>{
        returnList.items.push(newItem)
        returnList.save()
        res.redirect("/"+listName)
    })
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


}