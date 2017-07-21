#...제어문.
"""
# ...pass문 : 나중에 구현할 부분으로, 오류만 나지않게 함.
for i in range(0, 11):
    if i % 3 == 0:
        pass
    print(i)


#...3의 배수만 출력하기.
for i in range(0, 10):
    if i%3 != 0:
        continue
    print(i)
"""


"""
#...3의 배수만 제외하고 출력하기.
for i in range(0, 11):
    if i%3 == 0:
        continue
    print(i)

# ...break문 : 자기자신을 제외한 바로 상위 처리흐름을 벗어남.
for i in range(0, 11):
    if i % 3 == 0:
        break
    print(i)

"""

#...http://blog.naver.com/nasu0210/220836927243
"""
li=[50000,10000,5000,1000,500,100,50,10,5,1]
na = int(input('금액입력 : '))
for i in li:
    m=na//i #몫
    na=na%i #나머지
    print(i, '---', m)
"""

li=[]
k=1
for i in range(5):
    print(k)
    li.append(k)
    k=k*10
print(li)

li=[5*10**i for i in range(5)]
print(li) #[5, 50, 500, 5000, 50000]