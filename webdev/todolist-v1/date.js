module.exports.getDate = getDate

function getDate(){
    let date = new Date()
    const options = {weekday : "long", day : "numeric", month : "long"}
    return date.toLocaleDateString("en-US", options)
}
module.exports.getDay = getDay
function getDay(){
    let date = new Date()
    const options = {weekday : "long"}
    return  date.toLocaleDateString("en-US", options)
}
