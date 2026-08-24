import random

options = ["rock","paper","scissors"]
your_score = 0
bot_score = 0
set_score = 3
print("Welcome to the Rock Paper Scissors Game!")
print(f"Try to reach {set_score} score to win")
while your_score<set_score and bot_score<set_score:
    option = random.choice(options)
    choice = input("Select one of the options 'rock,paper or scissors' :").lower()
    print()
    if choice == "rock" or choice == "paper" or choice == "scissors":
        
        if option == "rock" and choice == "paper":
            your_score+=1
            print("You won the round")
        
        elif option == choice:
            print("It's tie")
        
        elif option == "rock" and choice == "scissors":
            bot_score+=1
            print("Computer won the round")

        elif option == choice:
            print("It's tie")

        elif option == "paper" and choice == "rock":
            bot_score+=1
            print("Computer won the round")

        elif option == "paper" and choice == "scissors":
            your_score+=1
            print("You won the round")

        elif option == "scissors" and choice == "rock":
            your_score+=1
            print("You won the round")

        elif option == "scissors" and choice == "paper":
            bot_score+=1
            print("Computer won the round")

        elif option == choice:
            print("It's tie")
        
        print(f"Computer's choice:{option}")
        print(f"Your choice:{choice}")
        print("----------------------------------")
        print(f"Your score:{your_score}")
        print(f"Computer's score:{bot_score}")
        print("----------------------------------")

    else:
        print("Your choice is invalid")

if your_score == set_score:
    print("You won")

elif bot_score == set_score:
    print("Computer won")