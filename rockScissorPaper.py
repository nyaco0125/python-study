import random

while True:
    myChoice = input("What's your choice: ")
    if myChoice == "rock":
        if random.randint(1,4) == 1:
            print("Scissor! OMG.. You won! :(")
        elif random.randint(1,4) == 2:
            print("Rock! Oh! Tie! xD")
        else:
            print("Paper! I won! LOL")
    if myChoice == 'scissor':
        if random.randint(1,4) == 1:
            print("Paper! OMG.. You won! :(")
        elif random.randint(1,4) == 2:
            print("Scissor! Oh! Tie! xD")
        else:
            print("Rock! I won! LOL")
    if myChoice == 'paper':
        if random.randint(1,4) == 1:
            print("Rock! OMG.. You won! :(")
        elif random.randint(1,4) == 2:
            print("Paper! Oh! Tie! xD")
        else:
            print("Scissor! I won! LOL")