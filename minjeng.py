# 주민등록번호를 입력해주세요
number = '08012532874'


first = {
    '99','98','97','96','95','94','93','92','91','90','99','98','97','96','95','94','93','92','91','90'
}

second = {
    '00','01','02','03','04','05','08','09','10','11','12','13','14','15','16','17','18','19','20'
}

if number[0:2] in first:
    if number[6] == '1':
        print('성별: 남자')
        print('생일: ' + '19'+number[0:2] + '년 ' + number[2:4]+ '월 ' + number[4:6]+ ' 일')
    if number[6] == '2':
        print('성별: 여자')
        print('생일: ' + '19'+number[0:2] + '년 ' + number[2:4]+ '월 ' + number[4:6]+ ' 일')
elif number[0:2] in second:
    if number[6] == '3':
        print('성별: 남자')
        print('생일: ' + '20'+number[0:2] + '년 ' + number[2:4]+ '월 ' + number[4:6]+ ' 일')
    if number[6] == '4':
        print('성별: 여자')
        print('생일: ' + '20'+number[0:2] + '년 ' + number[2:4]+ '월 ' + number[4:6]+ ' 일')
else:
    print('잘못된 주민등록번호이거나 1959년 이상 생인 주민등록번호입니다.')