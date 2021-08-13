import random

words = ("python", "hangman", "xylophone", "watch", "king", "dog", "animal", "anomaly", "hospital", "exit", "entrance", "jeep", "number", "airplane", "crossing", "tattoo")

lives = None
game_won = False

print("WELCOME TO HANGMAN!!!")
print("You have five lives!")
print("Choose wisely!")

play = input("would you like to play? (y/n) ")

def play_game(lives):
    
    mys_word = random.choice(words)
    mys_letters = list(mys_word)
    guess_letters = []
    game_won = False
    
    print(mys_word)
    
    while game_won == False:
        guess = input("what is your guess? ")
        
        if guess in mys_letters:
            print(f"Good job! {guess} is in the word!")
            guess_letters.append(guess)
            print(guess_letters)
        elif guess == mys_word:
            print(f"YOU WON! Congratulations!!! {mys_word} is the correct word!")
            game_won = True
        else:
            print(f"{guess} is not in the word! You lose a life.")
            lives -= 1
            
        if lives == 0:
            print("Game Over! You Lose!!")
            break
        
if play == "y":
    play_game(5)
else:
    print("Thanks for stopping by!")
    
play_again = input("Would you like to play again? (y/n) ")

if play_again == "y":
    play_game(5)
else:
    print("Thanks for playing!")