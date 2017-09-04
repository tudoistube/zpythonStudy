"""
ztxt = '100%'
try:
    znum = int(ztxt)
except ValueError:
    print('{}는 숫자가 아니에요'.format(ztxt))
#100%는 숫자가 아니에요
"""

"""
def safe_pop_print(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{} index의 값을 가져올 수 없네요.'.format(index))

safe_pop_print([1, 2, 3], 5) #5 index의 값을 가져올 수 없네요.
"""

"""
try:
    import my_module
except ImportError:
    print('모듈이 없어요ㅠㅠ') #모듈이 없어요ㅠㅠ
"""

"""
#...모든 예외를 한번에 처리하고 싶을 때:
try:
    list = []
    print(list[0])

    txt = 'abc'
    num = int(txt)
except Exception as ex:
    print('오류가 발생했어요.', ex)
#오류가 발생했어요. list index out of range
"""

"""
def rsp(mine, yours):
    allowed = ['가위', '바위', '보']
    msg = "'가위','바위','보' 가운데 하나만 입력하세요."
    #...allowed 안에 없는 잘못된 값이라면 :
    if mine not in allowed:
        raise ValueError(msg)
    if yours not in allowed:
        raise ValueError(msg)

rsp('가위', '바보')
'''
  File "D:/JoyWins/WS_Python/ztryHello/ztemp.py", line 49, in <module>
    rsp('가위', '바보')
  File "D:/JoyWins/WS_Python/ztryHello/ztemp.py", line 47, in rsp
    raise ValueError(msg)
ValueError: '가위','바위','보' 가운데 하나만 입력하세요.
'''
"""

"""
#...키가 190이 넘는 학생이 있는 반을 찾으면, 그 반 이름을 출력하고 
#   즉시 전체 for 문을 종료함.
classrooms = {'1반':[162, 175, 198, 137, 145, 199],
              '2반':[165, 177, 157, 160, 191]}
for class_id, heights in classrooms.items():
    for height in heights:
        if height> 190:
            print(class_id, '에 190이 넘는 학생이 있네요^^!')
            #break #...다음반으로 for문이 실행됨.
            raise StopIteration
'''
Traceback (most recent call last):
1반 에 190이 넘는 학생이 있네요^^!
  File "D:/JoyWins/WS_Python/ztryHello/ztemp.py", line 68, in <module>
    raise StopIteration
StopIteration
'''
"""

"""
#...키가 190이 넘는 학생이 있는 반을 찾으면, 그 반 이름을 출력하고
#   즉시 전체 for 문을 종료함.
classrooms = {'1반':[162, 175, 198, 137, 145, 199],
              '2반':[165, 177, 157, 160, 191]}
try:
    for class_id, heights in classrooms.items():
        for height in heights:
            if height > 190:
                print(class_id, '에 190이 넘는 학생이 있네요^^!')
                # break #...다음반으로 for문이 실행됨.
                raise StopIteration

except StopIteration:
    print('정상 종료')
'''
1반 에 190이 넘는 학생이 있네요^^!
정상 종료
'''
"""