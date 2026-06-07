import random

print("=====  ROCK PAPER SCISSORS  =====")

choices = ["rock", "paper", "scissors"]


while True:

    user_choice = input("\nEnter rock, paper, scissors:- ")

    if user_choice.lower() not in choices:
        print("Invalid chocie")
        continue

    computer_choice = random.choice(choices)
    
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It is a tie!")

    elif(
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")

    else:
        print("Computer wins!")

    again = input("\nDo you want to play again? (yes/no): ")

    if again.lower() != "yes":
        print("\nGame Over")
        break


