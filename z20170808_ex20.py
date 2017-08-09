f = open('C:/pytest/result.txt', 'w')
"""
open('파일경로', '옵션')
옵션 :
r : 읽기모드.
w : 쓰기모드.
a : 추가모드.
+ : 읽고쓰기모드.
"""
f.write('파이썬중급시작!!!/n Fighting!!!')
f.flush()
f.close()
if f.closed:
    print('파일을 닫았습니다.\n')

    