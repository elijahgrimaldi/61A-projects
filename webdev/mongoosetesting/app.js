
const url = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.9.1";
// getting-started.js
const mongoose = require('mongoose');

main().catch(err => console.log(err));

async function main() {
  await mongoose.connect(url+'/test');
//   const kittySchema = new mongoose.Schema({
//     name: String
//   });
// // NOTE: methods must be added to the schema before compiling it with mongoose.model()
//     kittySchema.methods.speak = function speak() {
//         const greeting = this.name
//         ? 'Meow name is ' + this.name
//         : 'I don\'t have a name';
//         console.log(greeting);
//     }; 
//     const Kitten = mongoose.model('Kitten', kittySchema);
//     const fluffy = new Kitten({name : "fluffy"})
//     const kittens = await Kitten.find();
//     console.log(kittens);

const personSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
      },
    age: Number,
    rating: {
        type: Number,
        min: 1,
        max: 10
    }
});
const Person = mongoose.model('Person', personSchema);
const richard = new Person({name : "Richard", age : 23})
const josh = new Person({name : "Josh", age : 23})
const stanley = new Person({name : "Stanley", age : 23})
const mason = new Person({name : "Mason", age : 23})
const anthony = new Person({name : "Anthony", age : 20, rating : 10})
const manthony = new Person({name : "Manthony" , age : 4, rating : 2})
await Person.deleteOne({name:"Manthony"})
// Person.insertMany([josh,stanley,mason])
const people = await Person.find({})
people.forEach(function(person){
    console.log(person.name)
})
await mongoose.connection.close()
}