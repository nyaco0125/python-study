recipe = {
    'name': 'Kimchi',
    'price': "15000won",
    'ingredient': ['lettuce']
}

print(recipe)
permission = input('수정하시겠습니까?> ')
if permission == '예':
        what = input('재료를 추가하시겠습니까 지우시겠습니까?> ')
        if what == '추가':
                plus_ing = input('추가할 내용을 적어주세요> ')
                recipe['ingredient'] = ['lettuce',plus_ing]
                print('추가되었습니다')
                print(recipe)
        elif what == '삭제':
                recipe.clear()
                print('삭제되었습니다')
        else:
                print('지원하지 않는 명령어 입니다.')
elif permission == '아니요':
        print('장비를 정지합니다')
else:
        print('지원하지 않는 명령어입니다.')
        
        