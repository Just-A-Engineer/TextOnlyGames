const words = ["javascript", "html", "hypertext", "banana", "orange", "apple", "mango", "kiwi", "xylophone", "markup", "jeep", "number", "pepper", "lion", "dog"];

const mysWordIndex = Math.floor(Math.random() * (words.length));
const mysWord = words[mysWordIndex];

console.log(mysWordIndex);
console.log(mysWord);

let play = window.prompt("Would you like to play a game of Hangman? (y/n)");

function correctGuess() {
  const correctG = window.prompt("You got it right! Take another guess!");
  
}

function playGame() {
  if(play === "y") {
    const playG = window.alert("You have 5 Lives! Play Wisely!");
    const guess = window.prompt("What is your guess? (Letter or Word)");
    
    while(mysWord != guess) {
      if(mysWord.includes(guess)) {
        correctGuess();
      } else if(mysWord === guess) {
        break;
        const youWin = window.prompt("You Won! Would you like to play again? (y/n) ");
      }
    }
    
  } else if(play === "n") {
    const denied = window.alert("Thanks for Stopping By!");
  }
}

playGame();
