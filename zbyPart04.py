"""
zid = 'JoyWins! '
zwhat = 'my dream!'

#print('Hi! I am ', ' JoyWins!', ' I have ', 'my ', 'dream!')
print('Hi! I am ', zid, 'I have ', zwhat)
"""

"""
#...power : a 의 b 승.
powA = 33
powB = 3
power = powA ** powB
print(power)
"""

"""
#...이차방정식의 근의 공식 : http://terms.naver.com/entry.nhn?docId=2073696&cid=47324&categoryId=47324
def print_root():
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) #...제곱근 : varX ** 0.5
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print('해는 {} or {}'.format(r1, r2)) #...문자열.format(a, b)

a = 2
b = -6
c = -8
print_root()
"""

#...여러개의 값을 한번에 반환할 수 있음 :
def print_root():
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) #...제곱근 : varX ** 0.5
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2 #...return 뒤에 쉼표로 여러개의 값을 반환할 수 있음.

a = 2
b = -6
c = -8
#...함수를 호출하고 여러개의 값을 한번에 받을 수 잇음 :
r1, r2 = print_root()
print('해는 {} or {}'.format(r1, r2)) #...문자열.format(a, b)