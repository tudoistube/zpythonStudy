def disp(title) :
    if (title == '') :
        title = '책제목'
    print(' * ' * 10)
    print(' * * '+title+' * * ')
    print(' * ' * 10)
    
disp('1')
disp('자바')
disp('파이썬')
disp('자바스크립트')
print('===============')

def add(a, b) :
    c = a + b
    print(c)

add(10, 20)
print('-------------------------')

n = int(10)
def aaa(a, b) :
    c = a + b + n #n : 전역변수.
    print(c)
    return c

def bbb(a, b) :
    c = a + b + n
    print(c)
    return c

k1 = aaa(20, 30)
k2 = bbb(30, 40)
print(k1)
print(k2)
print('-------------------------')

def ccc(start, end) :
    #pass
    tot = 0
    for i in range(start, end+1) :
        tot += i
    #print(tot)
    return tot

k1 = ccc(1, 100)
k2 =ccc(1, 50)
print(k1)
print(k2)
print('-------------------------')

def ddd(start, end) :
    #pass
    li = []
    c1 = start + end
    c2 = start - end
    li.append(c1)
    li.append(c2)
    return li

k1 = ddd(1, 100)
print(k1)
print(k1[0])
print(k1[1])
print('-------------------------')

def eee(start) :
    #pass
    tot = 0
    for i in start :
        tot += i
    #print(tot)
    return tot

li = [1, 2, 3, 4, 5]
k1 = eee(li)
print(k1)
print('-------------------------')

def fff(start) :
    #pass
    start.sort()
    print('start.sort() = ', start)
    return start

li = [1, 5, 8, 2, 6]
#k1 = fff(li)
#print(k1)
li.sort()
k=li.sort()
print(type(li))
print(type(li.sort))
#print(type(k))
#print(k)
k1 = fff(li)
print('k1 : ', k1)
print('-------------------------')







