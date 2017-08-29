#...함수선언.
def a():
    pass

#...클래스선언.
class Person:
    a = 10
    def __init__(self):
        print("init")
    def printHi(self):
        return "Hi"
    def fn1(self, a):
        return a


p = Person() #...인스턴스화.

p.a = 50
print(p.a)
p1 = p.printHi()
print(p1)

p2 = Person()
p2.a = 20
print(p2.a)

p3 = Person()
p3.a = 25
print(p3.a)
p31 = p3.fn1(8)
print(p31)