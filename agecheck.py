age = input("나이를 적어주세요>")


if float(age) > 18:
    print('당신은 출입가능입니다!')
elif float(age) < 18:
    print('당신은 출입금지! 미성년자는 안대요!')
else:
    print('1년만 기다리고 오세요~')    