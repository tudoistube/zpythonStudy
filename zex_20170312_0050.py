squares = [] #리스트.
for x in range(10) :
    squares.append(x**2)
print(squares)
print('===============')

#컴프리핸션 사용하기.
squares2=[x**2 for x in range(10)]
print(squares2)
print('-------------------------')

squares3=[x*7 for x in range(51)]
print(squares3)
print('-------------------------')

squares4=[x for x in range(1, 16) if x % 3 != 0]
print(squares4) #1~15 중 3의 배수 제외.
print('-------------------------')

#A=[1,2,3]이고 B=[1,2,3]일 때 중복되지 않는 순서쌍을
#구하시오.
li2 = [(a,b) for a in range(1, 4) for b in range(1, 4) if a != b]
print(li2)
print('-------------------------')
