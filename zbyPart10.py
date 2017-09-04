"""
#...딕셔너리형 :
#            ↓ 이름표는 문자열 또는 숫자를 주로 사용하지만
dict = { 	"이름표"	:	[1,2,3] }
#                           ↑ 값은 리스트를 포함해서 무엇이든 올 수 있습니다.

print( dict["이름표"] )
"""

"""
days_in_months = {"Jan":31, "Feb":28, "Mar":31, "-Jan":999}
del days_in_months['-Jan']
print(days_in_months) #{'Jan': 31, 'Feb': 28, 'Mar': 31}
"""

"""
#...사전형.pop('키') 는 삭제한 값을 반환함.
days_in_months = {"Jan":31, "Feb":28, "Mar":31, "-Jan":999}
print(days_in_months.pop('-Jan')) #999
print(days_in_months) #{'Jan': 31, 'Feb': 28, 'Mar': 31}
"""

agesDict = {"Tom":35, "Jane":23, "Mike":62}
for k in agesDict.keys():
    print(k, end=' ') #Tom Jane Mike
for v in agesDict.values():
    print(v, end=' ') #35 23 62
for k in agesDict.keys():
    print('{}의 나이는 {}입니다.'.format(k, agesDict[k]))
#...파이썬의 사전형은 for in 문에서 keys() 를 생략해도
#   사전형.keys() 값과 같음.
for k in agesDict:
    print('{}의 나이는 {}입니다.'.format(k, agesDict[k]))
for k, v in agesDict.items():
    print('{}의 나이는 {}입니다.'.format(k, v))
#Tom의 나이는 35입니다.
#Jane의 나이는 23입니다.
#Mike의 나이는 62입니다.

#...딕셔너리 타입의 box를 매개변수로 받고,
#   box 에 '불량품'이라는 이름표가 있으면
#   box 전체를 빈 딕셔너리로 만들고, 없으면 그대로 둠.
def check_and_clear(box):
    if('불량품' in box.keys()) :
        box.clear()
        print("불량품이 있으면 box를 clear합니다.")

#...튜플을 여러 변수에 나눠 담을 수 있음.
a, b = 1, 2
print('튜플은 여러 변수에 나눠 담음 : ', a, b)
# 튜플은 여러 변수에 나눠 담음 :  1 2

#...튜플을 이용하면 두 변수 사이의 값을 쉽게 맞바꿈 :
x = 5
y = 6
x, y = y, x
print(x, y) #6 5

#...패킹과 언패킹 :
c = (3, 4) #...변수 c 에 튜플 (3, 4)를 대입함.
print(c)   # (3, 4)
#...c 의 값을 언패킹해서 d 와 e 에 넣음 :
d, e = c
print('언패킹 : ', d, e) #언패킹 :  3 4
#...변수 d 와 e 를 f 에 패킹함 :
f = d, e
print('패킹 : ', f) #패킹 :  (3, 4) #튜플형.

#...튜플을 반환하는 함수는 여러 개의 값을 한 번에 반환할 수 있음.
def tuple_func():
    return 1, 2
q, w = tuple_func()
print(q, w) #1 2
r = tuple_func()
print(type(r)) #<class 'tuple'>

#...튜플로 값을 반환해 주면 한번에 하나의 변수로 받을 수 있음.
#...enumerate 를 쓰면 for문을 순회하는 동안 리스트의 인덱스와 값을
#   튜플로 묶어서 함께 반환함.
zlist = [1, 2, 3, 4, 5]
for a in enumerate(zlist):
    print('{}번값 : {}'.format(a[0], a[1]))

#...함수의 실행인자를 튜플이나 리스트에 담아 두었을 때는
#   변수 앞에 별표(*)를 붙이면, '튜플에 든 값을 쪼개서
#   여러개의 실행인자로 만들어라'는 의미가 됨.
zlist = [1, 2, 3, 4, 5]
for a in enumerate(zlist):
    print('{}번값 : {}'.format(*a))

agesDict = {"Tom":35, "Jane":23, "Mike":62}
#...하나의 변수로 받아도 실행 결과는 같음 :
for a in agesDict.items():
    print('{}의 나이는 : {}'.format(a[0], a[1]))
# Tom의 나이는 : 35
# Jane의 나이는 : 23
# Mike의 나이는 : 62

#...agesDict.items() 가 a 에 튜플형태로 값을 담는 것 같음.
#   함수의 실행인자를 튜플이나 리스트에 담아 두었을 때는 변수 앞에
#   별표(*)를 붙이면, 튜플에 든 값을 쪼개서 여러 개의 실행인자로
#   만들게 됨.
for a in agesDict.items():
    print('{}의 나이는 : {}'.format(*a))