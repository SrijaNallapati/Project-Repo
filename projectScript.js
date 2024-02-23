let compScore = 0;
let userScore = 0;

const choices = document.querySelectorAll(".choice");
const msg = document.querySelector("#msg");

const userScorePara = document.querySelector("#user-score");
const compScorePara = document.querySelector("#comp-score");
const selPara = document.querySelector("#sel")

const btn = document.querySelector("#btn");

const genCompChoice = () => {
    const options = ['rock','paper','scissors'];
    const randIdx = Math.floor(Math.random() * 3);
    return options[randIdx];
}

const playGame = (userChoice) => {
    console.log("User Choice is ",userChoice);
    const compChoice = genCompChoice();
    console.log("Computer Choice is ",compChoice);
    if(compChoice === userChoice){
        console.log("Game was Draw!");
        sel.innerText = `User Choice is ${userChoice}  and Computer Choice is ${compChoice}`;
        msg.innerText =  "Game was Draw! Play Again";
        msg.style.backgroundColor = "brown";
    }
    else if (userChoice === 'rock') {
        if(compChoice === 'scissors'){
            console.log("You Won! Rock beats Scissor");
            sel.innerText = `User Choice is ${userChoice}  and Computer Choice is ${compChoice}`;
            msg.innerText = "You Won! Rock beats Scissor";
            userScore++;
            userScorePara.innerText=userScore;
            msg.style.backgroundColor = "green";
        }
        else{
            console.log("You Lose! Paper beats Rock");
            sel.innerText = `User Choice is ${userChoice}  and Computer Choice is ${compChoice}`;
            msg.innerText = "You Lose! Paper beats Rock";
            compScore++;
            compScorePara.innerText = compScore;
            msg.style.backgroundColor = "red";
        }
    }
    else if (userChoice === 'paper') {
        if(compChoice === 'scissors'){
            console.log("You Lose! Scissor beats Paper");
            sel.innerText = `User Choice is ${userChoice}  and Computer Choice is ${compChoice}`;
            msg.innerText = "You Lose! Scissor beats Paper";
            compScore++;
            compScorePara.innerText = compScore;
            msg.style.backgroundColor = "red";
        }
        else{
            console.log("You Won! Paper beats Rock");
            sel.innerText = `User Choice is ${userChoice}  and Computer Choice is ${compChoice}`;
            msg.innerText = "You Won! Paper beats Rock";
            userScore++;
            userScorePara.innerText=userScore;
            msg.style.backgroundColor = "green";
        }
    }
    else if (userChoice === 'scissors') {
        if(compChoice === 'paper'){
            console.log("You Won! Scissor beats Paper");
            sel.innerText = `User Choice is ${userChoice}  and Computer Choice is ${compChoice}`;
            msg.innerText = "You Won! Scissor beats Paper";
            userScore++;
            userScorePara.innerText=userScore;
            msg.style.backgroundColor = "green";
        }
        else{
            console.log("You Lose! Rock beats Scissor");
            sel.innerText = `User Choice is ${userChoice}  and Computer Choice is ${compChoice}`;
            msg.innerText = "You Lose! Rock beats Scissors";
            compScore++;
            compScorePara.innerText = compScore;
            msg.style.backgroundColor = "red";
        }
    }
}

choices.forEach((choice) => {
    choice.addEventListener("click", () =>{
        const userChoice = choice.getAttribute("id")
        playGame(userChoice);
    })
})

btn.addEventListener("click", () => {
    userScore = 0;
    compScore = 0;
    userScorePara.innerText=userScore;
    compScorePara.innerText = compScore;
    msg.innerText = "Play Your Move"
    sel.innerText = "User's and Computer's choice :";
})