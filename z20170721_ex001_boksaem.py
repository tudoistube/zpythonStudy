'''
...튜플의 특징 : 메모리 효율이 좋고, 항목이 손상될 염려가 없고,
                 딕셔너리의 키로 사용할 수 있고,
                 함수의 인자는 튜플로 전달됨.
...소괄호() 사용하여 생성함.
#생성방법1, 2
'''

'''
tu=() #방법1.
a = tuple() #방법2.
print(tu)

tu=('a', 'b', 'c')
print(type(tu)) #<class 'tuple'>
'''

'''
#...주의!
Tuple 은 인자가 1개이면 인자뒤에 콤마(,)가 있어야 함.
Tuple 은 괄호를 생략할 수 있음.

tu=('a') 
print(type(tu)) #<class 'str'>

tu=('a',)
print(type(tu)) #<class 'tuple'>

tu='a', 'b', 'c'
print(type(tu)) #<class 'tuple'>
'''

'''
Tuple 은 한번에 여러 변수에 할당할 수 있음.

tu='a', 'b', 'c'
tu1, tu2, tu3 = tu
print(tu1, tu2, tu3) #a b c
'''

'''
#...주의!
다음은 오류가 발생함.
tu='a','b','c','d'
tu1, tu2 = tu
'''

'''
#...값을 다음과 같이 대입할 수 있음.

a=5
b=7
a,b = b,a
print(a, b) # 7 5
'''

li=['a', 'b', 'c', 'd', 'e', 'f']
a = tuple(li)
print(a) # ('a', 'b', 'c', 'd', 'e', 'f')

