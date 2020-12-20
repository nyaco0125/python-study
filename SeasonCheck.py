import datetime

now = datetime.datetime.now()

print(str(now.month) + "월" + str(now.day) + "일")
month = now.month


want = input("계절을 알고싶으신가요?> ")

if want == '예':
    if 3 <= month <= 5:
        print('봄이군요!')  
    elif 6 <= month <= 8:
        print('여름이군요!')
    elif 9 <= month <= 11:
        print('가을이군요!')
    else:
        print('겨울이군요!')
else:
    pass