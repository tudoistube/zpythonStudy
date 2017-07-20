dic = {'경상도': {'부산', '대구', '울산', '공통'},
         '전라도':{'광주','전주', '공통'}}

print(type(dic['경상도']))
print(dic['경상도'])
print(dic.items())
print('===============')
#열거형으로 바꿈.
li = list(dic.items())
print(li[1][1])
print('===============')
#dic > 열거형, 키와 값으로 출력함.
for name, contents in dic.items():
    print(name)
    print(contents)
    print('---------------------')
    if '광주' in contents:
        print(name)
        print('---------------------')
    if '공통' in contents and not ('대구' in contents):
        print(name)
        print('---------------------')

