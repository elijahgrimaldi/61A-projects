const url = "mongodb://127.0.0.1:27017/wikiDB"
const express = require("express")
const bodyParser = require("body-parser")
const mongoose = require("mongoose")
const app = express()
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({extended : true}))
app.use(express.static(__dirname + '/public'));


const articleSchema = mongoose.Schema({
    title:String,
    content:String
})
const Article = mongoose.model('Article', articleSchema)

main().catch(err => console.log(err));

async function main() {
await mongoose.connect(url);


app.route("/articles")
.get(function(req,res){
    Article.find({}).then((foundResults)=>{
        res.send(foundResults)
    }).catch((err)=>{
        res.send(err)
    })
})
.post(function(req,res){
    const userTitle = req.body.title
    const userContent = req.body.content
    const newArticle = new Article({
        title:userTitle,
        content:userContent
    })
    newArticle.save().then((message)=>{
        res.send("Successfully saved")
    }).catch((err)=>{
        res.send(err)
    })
})
.delete(function(req,res){
    Article.deleteMany({}).then((returnObject=>{
        res.send("Deleted "+returnObject.deletedCount+" documents.")
    })).catch((err)=>{
        res.send(err)
    })
})

app.route("/articles/:topic")
.get(function(req,res){
    Article.find({title:req.params.topic}).then((foundResults)=>{
        res.send(foundResults)
    }).catch((err)=>{
        res.send(err)
    })
})
.put(function(req,res){
    Article.replaceOne({title:req.params.topic},{title:req.body.title,content:req.body.content}).then((message)=>{
        res.send(message)
    }).catch((err)=>{
        res.send(err)
    })
})
.patch(function(req,res){
    Article.updateOne({title:req.params.topic},req.body).then((message)=>{
        res.send(message)
    }).catch((err)=>{
        res.send(err)
    })
})
.delete(function(req,res){
    Article.deleteOne({title:req.body.title}).then((message)=>{
        res.send(message)
    }).catch((err)=>{
        res.send(err)
    })
})



app.listen(3000,function(){
    console.log("Server started on port 3000")
})

}