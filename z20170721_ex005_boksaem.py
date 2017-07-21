#...제어문.
"""
#...3의 배수만 출력하기.
for i in range(0, 10):
    if i%3 != 0:
        continue
    print(i)
"""

#...3의 배수만 제외하고 출력하기.
for i in range(0, 11):
    if i%3 == 0:
        continue
    print(i)