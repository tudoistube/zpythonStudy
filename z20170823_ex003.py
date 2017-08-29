"""
rx = 0
ry = 0
def robot1(x, y):
    global rx, ry
    rx = rx + x
    ry = ry + y


robot1(10, 5)
robot1(-5, 2)

"""

class Robots:
    rx = 0
    ry = 0
    def moveXY(self, x, y):
        self.rx = self.rx + x
        self.ry = self.ry + y
        print(self.rx, " || ", self.ry)

r1 = Robots()
r1.moveXY(1, 2)
r1.moveXY(2, 3)