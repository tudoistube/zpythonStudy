"""
s = 'Hi, JoyWins!'
print(type(s)) #<class 'str'>

f = 3.14
print(type(f)) #<class 'float'>
"""

"""
#...자료형은 달라도 값은 같음.
print(type(25)) #<class 'int'>
print(type(25.0)) #<class 'float'>
print(25 == 25.0) #True
"""

"""
#...isinstance(값, 자료형) : 자료형 검사함수.
print(isinstance(25, int)) #True
print(isinstance(25.0, int)) #False
"""

"""
my_list = [1, 2, 3]
my_dict = {"풀": 800, "색연필": 3000}
my_tuple = (1, )
number = 10
real_number = 3.141592
print(type(my_list)) #<class 'list'>
print(type(my_dict)) #<class 'dict'>
print(type(my_tuple)) #<class 'tuple'>
print(type(number)) #<class 'int'>
print(type(real_number)) #<class 'float'>
"""

"""
znum = []
print(type(znum)) #<class 'list'>
"""

"""
znum = list(range(10))
print(znum) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(znum)) #<class 'list'>
zchar = list('hi,joywins')
print(zchar) #['h', 'i', ',', 'j', 'o', 'y', 'w', 'i', 'n', 's']
print(type(zchar)) #<class 'list'>
"""

"""
#...is 연산자 vs == 연산자.
list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 == list2:
    print("list1과 list2의 값은 같습니다.")
    #list1과 list2의 값은 같습니다.
    if list1 is list2:
        print("그리고 list1과 list2는 같은 인스턴스입니다.")
    else:
        print("list1과 list2는 다른 인스턴스입니다.")
        #list1과 list2는 다른 인스턴스입니다.
"""

"""
class Human():
    pass

person1 = Human()
person2 = Human()

person1.lang = '한국어'
person2.lang = 'English'

print(person1.lang) #한국어
print(person2.lang) #English

person1.name = '대구시민'
person2.name = '인도인'

def speak(person):
    print("{} 이 {} 로 말을 합니다".format(person.name, person.lang))

speak(person1) #대구시민 이 한국어 로 말을 합니다
speak(person2) #인도인 이 English 로 말을 합니다
"""

"""
class Human():
    pass

per = Human()
per.name = '재니'
per.weight = 62.5

def create_human(_name, _weight):
    person = Human()
    person.name = _name
    person.weight = _weight
    return person

#...함수를 클래스에 넣음.
Human.create = create_human

#person = create_human('수지', 60.2)
person = Human.create('수지', 60.2)

def eat(person):
    person.weight += 0.1
    print("{} 가 먹어서 {}kg 이 되었습니다".format(person.name, person.weight))

def walk(person):
    person.weight -= 0.1
    print("{} 가 걸어서 {}kg 이 되었습니다".format(person.name, person.weight))

Human.eat = eat
Human.walk = walk

#...함수를 클래스에 넣음.
person.walk()
person.eat()
person.walk()
"""

"""
#...빈 클래스와 함수를 따로 만들고, 다시 함수를 클래스에 넣는 방식 대신,
#   클래스에 메서드를 선언함.
class Human():
    '''Human...'''
    def create(_name, _weight):
        person = Human()
        person.name = _name
        person.weight = _weight
        return person

    def eat(person):
        person.weight += 0.1
        print("{} 가 먹어서 {}kg 이 되었습니다".format(person.name, person.weight))

    def walk(person):
        person.weight -= 0.1
        print("{} 가 걸어서 {}kg 이 되었습니다".format(person.name, person.weight))

#...클래스에 따로 넣어 주지 않아도 바로 클래스에 있는 함수를 사용함.
person = Human.create("수지", 60.5)
person.walk()
person.eat()
person.walk()
"""

"""
#...메서드를 호출할 때 첫번째 인자를 생략하면 인스턴스 자신으로 채워준다.
#   파이썬에서는 자기 자신을 자동으로 넘겨주는 매개변수 self 를 사용함.
class Human():
    '''Human...'''
    def create(_name, _weight):
        self = Human()
        self.name = _name
        self.weight = _weight
        return self

    def eat(self):
        self.weight += 0.1
        print("{} 가 먹어서 {}kg 이 되었습니다".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{} 가 걸어서 {}kg 이 되었습니다".format(self.name, self.weight))

#...클래스에 따로 넣어 주지 않아도 바로 클래스에 있는 함수를 사용함.
person = Human.create("수지", 60.5)
"""

"""
#...메서드를 호출할 때 첫번째 인자를 생략하면 인스턴스 자신으로 채워준다.
#   파이썬에서는 자기 자신을 자동으로 넘겨주는 매개변수 self 를 사용함.
class Human():
    '''Human...'''
    def create(_name, _weight):
        self = Human()
        self.name = _name
        self.weight = _weight
        return self

    def eat(self):
        self.weight += 0.1
        print("메서드eat :: {} 가 먹어서 {}kg 이 되었습니다".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{} 가 걸어서 {}kg 이 되었습니다".format(self.name, self.weight))

#...함수의 매개변수로 self 를 넣음.
def eat(self):
    self.weight += 1.1
    print("함수eat :: {} 가 먹어서 {}kg 이 되었습니다".format(self.name, self.weight))

person = Human.create("수지", 60.5)

eat(person) #함수eat :: 수지 가 먹어서 61.6kg 이 되었습니다

#...메서드를 호출할 때는 자동으로 첫번째 매개변수인 self 에 person 변수가
#   실행인자로 전달됨.
person.eat() #메서드eat :: 수지 가 먹어서 61.7kg 이 되었습니다
"""

"""
class Human():
    '''Human...'''
    def create(_name, _weight):
        self = Human()
        self.name = _name
        self.weight = _weight
        return self

    def eat(self):
        self.weight += 0.1
        print("메서드eat :: {} 가 먹어서 {}kg 이 되었습니다".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{} 가 걸어서 {}kg 이 되었습니다".format(self.name, self.weight))

    #...speak 메서드에는 매개변수가 2개처럼 보이지만,
    #   person 인스턴스에서 메서드를 호출하면, self 에는 person 자신이 들어가서
    #   실제로는 실행인자에 msg 하나만 넘겨줌.
    def speak(self, msg):
        print("{} 라고 말해요^^...".format(msg))

person = Human.create("수지", 60.5)

person.speak("안녕, 나는 이수지야^^")
#안녕, 나는 이수지야^^ 라고 말해요^^...
"""

"""
class Car():
    '''자동차'''
    def run(self):
        print("{}가 달립니다.".format(self.name))

taxi = Car()
taxi.name = "택시"
taxi.run()
"""

class Human():
    '''Human...'''
    #def __init__(self):
    #...매개변수도 받을 수 있음.
    def __init__(self, _name, _weight):
        '''초기화 메서드'''
        self.name = _name
        self.weight = _weight
        print("__init__실행...")
        print("이름은 {}, 몸무게는 {}".format(_name, _weight))

    def __str__(self):
        '''문자열화 메서드'''
        return "{}(몸무게:{}kg)".format(self.name, self.weight)

    def eat(self):
        self.weight += 0.1
        print("메서드eat :: {} 가 먹어서 {}kg 이 되었습니다".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{} 가 걸어서 {}kg 이 되었습니다".format(self.name, self.weight))

    #...speak 메서드에는 매개변수가 2개처럼 보이지만,
    #   person 인스턴스에서 메서드를 호출하면, self 에는 person 자신이 들어가서
    #   실제로는 실행인자에 msg 하나만 넘겨줌.
    def speak(self, msg):
        print("{} 라고 말해요^^...".format(msg))

#...Human 클래스의 인스턴스를 person 에 저장함.
#person = Human()
person = Human("사람", 62.5)
#__init__실행...
#이름은 사람, 몸무게는 62.5
print(person.name)
print(person.weight)
#...__str__(self)가 실행됨, 다른 언어의 toString()과 같음.
print(person) #사람(몸무게:62.5kg)