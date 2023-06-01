var buttonColours = ["red", "blue", "green", "yellow"];
var gamePattern = [];
var userClickedPattern = [];
var level = 0;
var started = false;

function playSound(name){
    var audio = new Audio("sounds/" + name + ".mp3");
    audio.play();
}
function nextSequence(){
    var randomNumber = Math.floor((Math.random()*4));
    var randomChosenColour = buttonColours[randomNumber];
    gamePattern.push(randomChosenColour);
    $("#" + randomChosenColour).fadeIn(100).fadeOut(100).fadeIn(100);
    playSound(randomChosenColour);
    level++;
    $("h1").text("Level "+level);
}
 $(".btn").click(function(){
    userChoseColour = $(this).attr("id");
    animatePress(userChoseColour)
    userClickedPattern.push(userChoseColour)
    playSound(userChoseColour)
    if (userClickedPattern.length === gamePattern.length){
        var check = checkAnswer(level);
        if (check === true){
            userClickedPattern = [];
            setTimeout(function(){
                nextSequence()
            }, 500);
        } else{
            gameOver()
        }
    }

})
function animatePress(currentColour){
    $("#" + currentColour).addClass("pressed")
    setTimeout(function(){
        $("#" + currentColour).removeClass("pressed")
    }, 100);
}
    

if (started === false){
    $(document).keydown(function(){
        $("h1").text("Level "+level);
        nextSequence();
        started = true;
    })
}

function gameOver(){
    $("h1").text("Game Over");
    $("body").addClass("game-over")
    setTimeout(function(){
        $("body").removeClass("game-over")
        resetGame();
    }, 500);
}


function resetGame(){
    level = 0;
    userClickedPattern = [];
    gamePattern = [];
    $("h1").text("Press A Key to Start");
    started = false;
}

function checkAnswer(currentLevel){
    for (var i=0;i<currentLevel;i++){
        if (userClickedPattern[i] === gamePattern[i]){
            continue
        } else{
            return false
        }
    }
    return true
}
