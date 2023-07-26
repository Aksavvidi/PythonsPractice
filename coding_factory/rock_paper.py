import random

options = ["rock", "paper", "scissors"]

#Get input and normalized in order to compare
player_input = input("Enter your choice (rock/paper/scissors): ").lower()
if player_input in options:
     print("You chose: ", player_input)
else:
    print("Invalid choice. Please enter rock, paper, or scissors.")
    
computer_str = random.choice(options)

print("Computer chose: ", computer_str)

# Find the winner
if player_input == computer_str:
    print("It's a tie!")
elif player_input == "rock":
    if computer_str == "paper":
        print("Computer wins!")
    else:
        print("You win!")
elif player_input == "paper":
    if computer_str == "scissors":
        print("Computer wins!")
    else:
        print("You win!")
elif player_input == "scissors":
    if computer_str == "rock":
        print("Computer wins!")
    else:
        print("You win!")

