import random

#Printing Rules
print("...rock...")
print("...paper...")
print("...scissors...")
print("...please enter it in lower case...")

#Game Choice of One Player or Two Player
game_choice = input("One Player or Two Player? ")

#Take Input and Computer Choice
p1_choice = input("(enter Player 1's choice): ")
if game_choice == "one player":
    com_choice = random.choice(["rock", "paper", "scissors"])
elif game_choice == "two player":
    p2_choice = input("(enter Player 2's choice): ")

if game_choice == "one player":
    print("(Computer's choice): " + com_choice)

print("SHOOT!")

if game_choice == "one player":
    #Rock Set
    if p1_choice == "rock" and com_choice == "rock":
        print("It's a Tie!")
    elif p1_choice == "rock" and com_choice == "scissors":
        print("Player 1 wins!")
    elif p1_choice == "rock" and com_choice == "paper":
        print("Computer wins!")
    #Scissors Set
    elif p1_choice == "scissors" and com_choice == "rock":
        print("Computer wins!")
    elif p1_choice == "scissors" and com_choice == "scissors":
        print("It's a Tie!")
    elif p1_choice == "scissors" and com_choice == "paper":
        print("Player 1 wins!")
    #Paper Set
    elif p1_choice == "paper" and com_choice == "rock":
        print("Player 1 wins!")
    elif p1_choice == "paper" and com_choice == "scissors":
        print("Computer wins!")
    elif p1_choice == "paper" and com_choice == "paper":
        print("It's a Tie!")
    #Else Statement
    else:
        print("Please enter a valid choice.")

if game_choice == "two player":
    #Rock Set
    if p1_choice == "rock" and p2_choice == "rock":
        print("It's a Tie!")
    elif p1_choice == "rock" and p2_choice == "scissors":
        print("Player 1 wins!")
    elif p1_choice == "rock" and p2_choice == "paper":
        print("Player 2 wins!")
    #Scissors Set
    elif p1_choice == "scissors" and p2_choice == "rock":
        print("Player 2 wins!")
    elif p1_choice == "scissors" and p2_choice == "scissors":
        print("It's a Tie!")
    elif p1_choice == "scissors" and p2_choice == "paper":
        print("Player 1 wins!")
    #Paper Set
    elif p1_choice == "paper" and p2_choice == "rock":
        print("Player 1 wins!")
    elif p1_choice == "paper" and p2_choice == "scissors":
        print("Player 2 wins!")
    elif p1_choice == "paper" and p2_choice == "paper":
        print("It's a Tie!")
    #Else Statement
    else:
        print("Please enter a valid choice.")
    