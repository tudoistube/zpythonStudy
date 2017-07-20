class Person : #클래스 첫글자는 대문자.
    name = '홍작가'
    age = 17

k = Person()
print(k.name)
print(k.age)
print('===============')

class Person : 
    def __init__(self, _name, _age) : #초기자.
        self.name = _name
        self.age = _age
        print(self.name)
        print(self.age)

p1 = Person('김구라', 48)
print('name : {0}, age : {1}'.format(p1.name, p1.age))

p2 = Person('유작가', 45)
print('name : {0}, age : {1}'.format(p2.name, p2.age))

p3 = Person('전변', 58)
print('name : {0}, age : {1}'.format(p3.name, p3.age))
print('===============')


class Person : 
    def __init__(self, _name, _tel) : #초기자.
        self.name = _name
        self.tel = _tel
        print(self.name)
        print(self.tel)

p1 = Person('김구라', '111-1111')
print('name : {0}, tel : {1}'.format(p1.name, p1.tel))

p2 = Person('유작가', '111-1111')
print('name : {0}, tel : {1}'.format(p2.name, p2.tel))

p3 = Person('전변', '111-1111')
print('name : {0}, tel : {1}'.format(p3.name, p3.tel))

li = [] #리스트
li.append(p1)
li.append(p2)
li.append(p3)
print(li)

for i in li:
    print('name : {0}, tel : {1}'.format(i.name, i.tel))
print('===============')


class Person : 
    def __init__(self, _name, _tel) : #초기자.
        self.name = _name
        self.tel = _tel
        print(self.name)
        print(self.tel)
        
li = [] #리스트
for i in range(4):
    name = input('이름은?')
    tel = input('전화번호는?')

    li.append(Person(name, tel))

for i in li:
    print('name : {0}, tel : {1}'.format(i.name, i.tel))
print('===============')


class Person : 
    def __init__(self) : #초기자.
        self.name = input('별명은?')
        self.tel = input('핸펀번호는?')
        print(self.name)
        print(self.tel)
        
li = [] #리스트
for i in range(4):
    li.append(Person())

for i in li:
    print('name : {0}, tel : {1}'.format(i.name, i.tel))
print('===============')

