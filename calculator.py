what = input("어느것을 실행할지 적어주세요> ")
first = input("첫번째 숫자를 적어주세요> ")
second = input("두번째 숫자를 적어주세요> ")

if what == "곱하기":
    print(float(first) * float(second))
    
elif what == '나누기':
    print(float(first) / float(second))
elif what == '더하기':
    print(float(first) + float(second))
elif what == '뺴기':
    print(float(first) - float(second))
elif what == '제곱':
    print(float(first) ** float(second))
