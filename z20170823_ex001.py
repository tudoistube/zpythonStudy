def a():
    print("a")

a()

def b(num):
    print(num)

b(2)

def c():
    return 10

c = c()

def d(num):
    return num

d = d(3)
print(d)


def a(li):
    n1 = li[0]
    n2 = li[1]
    n3 = li[2]

li = [1,2,3,4,5]
a(li)

def b():
    li = ['a', 'b', 'c', 'd']
    return li

listNum = b()