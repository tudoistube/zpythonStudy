"""
class Robot:
    posX=0
    posY=0
    def move(self, x, y):
        self.posX =self.posX + x
        self.posY = self.posY + y
        return (self.posX, self.posY)

r = Robot()
print(r.move(1, 2))
print(r.move(1, 2))
"""

"""
#...보통은 객체를 외부에서 조작하도록 생성하지 않음.
class Car():
    color = "blue"
    size = 120

c = Car()
c.color = "green"
print(c.color) #green

c1 = Car()
c1.color = "white"
c1.size = 200
print(c.color, c1.color) #green white
"""

"""
class Car():
    # ...객체의 초기자를 이용하여 변수를 초기화함.
    def __init__(self, c="White", s=100):
        self.color = c
        self.size = s
        print("초기자...color:{}, size:{}".format(self.color, self.size))
    # ...getter, setter 를 이용하여 외부에서 값을 읽고 변경함.
    def getSize(self):
        return self.size
    def setSize(self, s):
        self.size = s
    def getColor(self):
        return self.color
    def setColor(self, c):
        self.color = c

c = Car() #초기자...color:White, size:100
c.setColor("Green")
c.setSize(180)
print(c.getColor(), c.getSize()) #Green 180
"""

"""
class Car():
    # ...객체의 초기자를 이용하여 변수를 초기화함.
    def __init__(self, c="White", s=100):
        self.color = c
        self.size = s
        print("초기자...color:{}, size:{}".format(self.color, self.size))
    # ...getter, setter 를 이용하여 외부에서 값을 읽고 변경함.
    def getSize(self):
        return self.size
    def setSize(self, s):
        self.size = s
    def getColor(self):
        return self.color
    def setColor(self, c):
        self.color = c

#...클래스 상속.
class smallCar(Car):
    pass

c = smallCar() #초기자...color:White, size:100
"""

class Car():
    # ...객체의 초기자를 이용하여 변수를 초기화함.
    def __init__(self, c="White", s=100):
        self.color = c
        self.size = s
        print("초기자...color:{}, size:{}".format(self.color, self.size))
    # ...getter, setter 를 이용하여 외부에서 값을 읽고 변경함.
    def getSize(self):
        return self.size
    def setSize(self, s):
        self.size = s
    def getColor(self):
        return self.color
    def setColor(self, c):
        self.color = c

#...클래스 상속.
class smallCar(Car):
    def __init__(self, c="Ivory", s=80):
        self.color = c
        self.size = s
        self.speedMax = 105
        print("초기자...color:{}, size:{}".format(self.color, self.size))
    def getSize(self):
        return 80
    def setSpeedUp(self):
        self.speedMax = self.speedMax + 10
    def getSpeedUp(self):
        return self.speedMax

c = smallCar() #초기자...color:Ivory, size:80 #...자식클래스의 초기자가 있으므로.
print(c.getSize()) #80
print(c.getSpeedUp()) #105
c.setSpeedUp()
print(c.getSpeedUp()) #115

c1 = smallCar("Navy") #초기자...color:Navy, size:80
c2 = smallCar("Navy", 120) #초기자...color:Navy, size:120