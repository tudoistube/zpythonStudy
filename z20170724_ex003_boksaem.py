"""
#...컴프리핸션 : http://blog.naver.com/nasu0210/220800214678
"""
squares=[x**2 for x in range(10)]
print(squares)
"""
#...1~50까지 숫자 중 7의 배수만 리스트에 출력.방법1.
times7=[x*7 for x in range(1, 50)]
for i in times7:
    if i<50 : print(i)
    
#...1~50까지 숫자 중 7의 배수만 리스트에 출력.방법2.
times7 = [x for x in range(0, 51, 7)]
print(times7)

#...1에서 15까지 중 3의 배수가 아닌것만 리스트에 담기.
squares=[x for x in range(1, 16) if x%3!=0]
print(squares)
"""

"""
#...A=[1,2,3]이고 B=[1,2,3]일 때 중복되지 않는 순서쌍을 구하기.
a=[1,2,3]
li=[a for a in range(1, 4)]
print(a)

#...이중for문 만들기.
b=[1,2,3]
li=[(a, b) for a in range(1, 4) for b in range(1, 4)]
#print('a', a, 'b', b)
print(li)

#...중복되지 않는 순서쌍 구하기.
li2=[(a, b) for a in range(1, 4) for b in range(1, 4) if a!=b]
#print('a', a, 'b', b)
print(li2)

"""

"""
#...구구단 리스트 만들기.
a=[str(x) + '*' + str(y) + '=' + str(x*y)
   for x in range(2, 10)
   for y in range(1, 10)]
print(type(a), a)

"""
a='abcdef'
b=list(a)
b[1]='k' #...1번째 값을 'k' 로 변경함.
print('1', b)
print('2', a)
a='-'.join(b)
print(a)

