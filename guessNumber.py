import random

number = random.randint(1, 11)

while True:
    userNumber = input("What's your number: ")
    if number == int(userNumber):
        print("OMG... You won! xD")
        break
    else:
        print("Try again!")
        continue