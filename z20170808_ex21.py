f=open('C:/pytest/NEWS.txt', 'r') #...rt : text 를 읽기 모드. r 도 가능함.

"""
print(f.readline())
print(f.readline())
print(f.readline())
"""

"""
for i in range(5):
    print(f.readline())
"""


for i in f:
    print(i)
