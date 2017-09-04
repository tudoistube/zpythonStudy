"""
selected = None
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요>')

print('선택된 값은 : ', selected)
"""

"""
selected = None
if selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에 선택하세요>')

print('선택된 값은 : ', selected)
"""

"""
patterns=['가위','바위','보']
for i in range(len(patterns)):
    print(patterns[i])
"""

"""
patterns=['가위','바위','보']
length=len(patterns)
i=0
while i<length:
    print(patterns[i])
    i = i + 1
"""

"""
numbers = [1,2,3]
length = len(numbers)
print('length : ', length)
i = 0
while i < length :
	print('{} : {}'.format(i, numbers[i]))
	i = i + 1
"""

"""
zlist = [1, 2, 3, 5, 7, 2, 5, 237, 55]
for val in zlist:
    if val % 3 == 0:
        print(val)
        break
"""

"""
#...1부터 10까지 숫자 중 홀수를 두번씩 출력함.
#   중요한 코드를 깊게 배치하지 않고 간결하게 함
for val in range(10):
    if val % 2 == 0:
        continue
    print(val)
"""

znum = [(1, 2), (10, 0)]

for a, b in znum:
    if b == 0:
        print("0으로 나눌 수 없네요...")
    else:
        #print("{}를 {}로 나누면 {}".format(a, b, a/b))
        continue