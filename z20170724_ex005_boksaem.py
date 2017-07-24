"""
#...[파이썬 기초] pyton함수 다루기 가변인자 *, ** : http://blog.naver.com/nasu0210/220734447970
# 별(*) 1개 사용하면 가변인자는 튜플형.
# 별(*) 2개 사용하면 가변인자는 딕셔너리형.
"""
"""
def msg(*t):
    #print(type(t)) #<class 'tuple'>
    sum=0
    for i in t:
        sum+=i
    print('sum : ', sum)

msg(1,2,3,4,5)
"""

"""
def msg(*t):
    #print(type(t)) #<class 'tuple'>
    result = str() #...스트링 초기화, result = '' 와 같음.
    for i in t:
        result += i
    #...result :  abcde type :  <class 'str'>
    print('result : ', result, 'type : ', type(result))

msg('a', 'b', 'c', 'd', 'e')
"""

"""
def msg(**t):
    sum=0
    #print(type(t)) #<class 'dict'>
    for i in t.items():
        print(i)    # ('kor', 90) ('eng', 80) ('mat', 70)

    for i,j in t.items():
        print(i, j)    # kor 90  eng 80  mat 70

    for i in t.values():
        sum+=i
        print(i)    # 90 80 70
    print('sum : ', sum)


#...딕셔너리형을 사용함.
msg(kor=90, eng=80, mat=70)
"""

"""
def msg(kor=90):
    print(kor)

msg() #...매개변수가 없어도 함수선언에 기본값이 있음. 90
msg(kor=100) #...호출하는 매개변수가 기본값보다 우선함. 100
"""

def msg2(kor=90, a=77):
    print(kor, a)

msg2(80) #80 77
msg2 (a=88) #90 88