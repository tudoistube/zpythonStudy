name = input("이름이 뭐에요? ")
print("Hi, ", name)
print('===============')

"""
x = input("?")
a = int(x)

x= input("?")
b = int(x)

print("a * b = ", a*b)
print('===============')
"""

import time

input("엔터를 누르고 10초를 셉니다.")
start = time.time()

input("10초 후에 엔터를 다시 누릅니다.")
end = time.time()

et = end -start
print("실제시간 : ", et, "초")
print("차이 : ", abs(et - 10), "초")
