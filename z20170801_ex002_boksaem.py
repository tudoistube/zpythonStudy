"""
    def __init__(self, name = '홍길동', age=99):
        if(len(name) > 0) :
            self.name = input("이름은요?")
        else :
            self.name = name
        if(age > 0) :
            self.age = input('나이는요?')
        else :
            self.age = age
"""
class Person0801_002_01:
    def __init__(self, name='홍길동', age=99):
        self.name = name
        self.age = age

    def disp(self):
        print("이름은 " + self.name + "님이고, 나이는 " + str(self.age) + "살입니다.\n")

p1 = Person0801_002_01("JoyWins", 38)
p1.disp()
