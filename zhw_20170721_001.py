#...별찍기 : http://blog.naver.com/nasu0210/220769623225
"""
*
**
***
****
*****

#...방법1.
for i in range(1, 6):
    for j in range(1, i+1):
        print('*', end='') #...end='' 해줘야 줄바꿈 되지 않음.
    print() #...빼면 줄바꿈이 안됨.

#...방법2.
for i in range(1, 6):
    print('*'*i)
"""

"""
*****
****
***
**
*

for i in range(1, 6):
    for j in range(1, 7-i):
        print('*', end='') #...end='' 해줘야 줄바꿈 되지 않음.
    print() #...빼면 줄바꿈이 안됨.
"""

"""
    *
   **
  ***
 ****
*****

#...방법1.
for i in range(1, 6):
    for j in range(1, 6-i):
        print(' ', end='') #...한칸띄워줘야 빈칸임.
    for j in range(1, i+1):
        print('*', end='') #...end='' 해줘야 줄바꿈 되지 않음.
    print() #...빼면 줄바꿈이 안됨.

#...방법2.
for i in range(5, 0, -1):
    print('*'*i)
"""
"""
      *
     **
    ***
   ****
  *****

for i in range(5, 0, -1):
    print(' '*i, '*'*(6-i)) #2개이상의 내용을 하나의 print 로 출력함.
"""


"""
...for : https://docs.python.org/3.6/tutorial/controlflow.html#for-statements
cat 3
window 6
defenestrate 12

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))
print()
"""

"""
0 Mary
1 had
2 a
3 little
4 lamb

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
print()
"""

"""
   *
  ***
 *****
*******

#...방법1.
for i in range(1, 5):
    for j in range(1, 5-i):
        print(' ', end='')
    for j in range(1, i*2, 1): #...range(start, end, step)
        print('*', end='')
    print()

#...방법2.
for i in range(1, 5):
    print(' '*(5-i), '*'*(i*2-1))
"""


"""
1
12
123
1234
12345

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end='')
    print()
"""

"""
1
22
333
4444
55555

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end='')
    print()
"""

