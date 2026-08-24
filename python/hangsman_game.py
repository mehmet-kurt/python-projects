import random
words = ["apple","orange","peer","carrot","grape","banana","home","store","calculation",
         "observation","simulation","criticise","sandman","telephone",
         "table","brave","conscience","donkey","tiger","parrot"]

art_collc = {1:(" O ",
                " ",
                " "),
            2:(" O ",
               " | ",
               " "),
            3:(" O ",
               "/| ",
               " "),
            4:(" O ",
               "/|\\",
               " "),
            5:(" O ",
               "/|\\",
               "/ "),
            6:(" O ",
               "/|\\",
               "/ \\")  
                }

def main():
    print("*****************************")
    print("Welcome to the Hangsman Game!\n")
    print("*****************************")
    print("You have 6 guesses to find the word")
    word = random.choice(words).upper()
    is_running = True
    guesses = []
    wrong_guesses=0
    while is_running:
        print("-----------------------------")

        print()

        guess = input("Make a guess of a letter or the word:").upper()
        print()
        if not guess.isalpha():
            print("Invalid input")

        else:
            if len(guess)>1:
                if guess == word:
                    print(f"Well done!! You find the word:{word}")
                    is_running = False
                else:
                    wrong_guesses+=1
                    guesses.append(guess)
                    print("Wrong word guess")
                    print("***************\n")

                    for x in art_collc[wrong_guesses]:
                        print(x)
                    print()
                    print("***************")

                if is_running:
                    for i in word:
                        if i in guesses:
                            print(i,end=" ")
                        else:
                            print("__",end=" ")
            
            elif guess in word:
                print(f"You made a correct guess: {guess}")
                print()
                guesses.append(guess)
                for i in word:
                    if i in guesses:
                        print(i,end=" ")
                    else:
                        print("__",end=" ")
        
            else:
                guesses.append(guess)
                wrong_guesses+=1
                print(f"{guess} is a wrong guess! Try again.")
                print("***************\n")

                for x in art_collc[wrong_guesses]:
                    print(x)
                print()
                print("***************")

                for i in word:
                    if i in guesses:
                        print(i,end=" ")
                    else:
                        print("__",end=" ")

        if wrong_guesses == 6:
            print(f"You lost! Game is over! Word is {word}")
            is_running = False

        print("\n")

        print(f"Your guesses so far{guesses}")


if __name__ == "__main__":
    main()