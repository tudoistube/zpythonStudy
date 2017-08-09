x = 10
y = 12
z = x + y
#print(z)
r = x / y
#print(r)
'''
1. 숫자형.
숫자형 : int, float
불리언형 : bool(True, False)
복소수형 : complex (ex.5+2j) , http://blog.naver.com/smilewhj/220760979616
2. 문자열.
str "hi", str 'hi'

'''
c = 56 + True
#print(c) #57
#c = 56 + (4+3j)
print(c) #(60+3j)
#c=56+'뭐든지'
#print(c) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
c=str(56)+'뭐든지'
print(c)
