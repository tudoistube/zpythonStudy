jumsu = int(input('점수를 입력하세요'))
while jumsu<0 or jumsu>100:
    jumsu = int(input('점수를 입력하세요'))
print('===============')

for i in range(10) :
    print('*', end='') #가로로 출력할때, end=' 구분할공백또는 기타입력 '
print('===============')

print('*'*10)
print('===============')

for i in range(1, 11, 2) : #0부터 시작하므로 1부터 10까지 홀수번째만 출력.
    print(i) 
print('===============')
"""
구구단
"""
for i in range(1, 10) :
    print(3, ' * ', i, ' = ', 3*i) 
print('===============')

for i in range(1, 10) : #9번
    for j in range(1, 5) : #4번
        print(i, ' * ', j, ' = ', i*j) #36
print('===============')

for i in range(1, 10) : 
    for j in range(1, 10) : 
        print(i, ' * ', j, ' = ', i*j) 
print('===============')

for i in range(1, 6) :
    for j in range(1, i+1) : 
        print(' * ', end='')
    print(' ')
print('===============')

for i in range(1, 6) :
    print(' ★ '*i)
print('===============')

for i in range(5, 0, -1) :
    print(' * ' * i)
print('===============')

for i in range(5, 0, -1) :
    for j in range(i, i+1):
        print(' * ' , end='')
    print()
print('===============')

for i in range(1, 7) :
    print( i * i )
print('===============')



















