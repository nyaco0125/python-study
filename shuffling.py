import random

text = input('텍스트 입력> ')
while True:
    splitted = list(text.split(" "))
    random.shuffle(splitted)
    print(splitted)
