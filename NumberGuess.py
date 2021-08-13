import random

random_number = random.randint(1,10)
guess = int(input("What is your guess?"))

while random_number > 0:
    if guess != random_number:
        print("Guess again!")
        guess = int(input("What is your guess?"))
    else:
        print("Great guess! You got it")
        break

play_again = input("Would you like to play again? y or n")

if play_again == "y":
    random_number = random.randint(1,10)
    guess = int(input("What is your guess?"))
    
    while guess != random_number:
        guess = int(input("What is your guess?"))
        
        if guess < random_number:
            print("Too Low!")
        elif guess > random_number:
            print("Too High!")
        else:
            print("Great guess! You got it")
            break
        
    play_again = input("Would you like to play again? y or n ")
    
elif play_again == "n":
    print("Thanks for playing!")