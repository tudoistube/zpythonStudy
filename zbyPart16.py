"""
class Animal():
    '''동물'''
    def walk(self):
        print('걷는다.')

    def eat(self):
        print('먹는다.')

#...Human 클래스는 Animal 클래스를 상속받음.
class Human(Animal):
    '''인간'''
    def wave(self):
        print('손을 흔든다.')

class Dog():
    '''강아지'''
    def wag(self):
        print('꼬리를 흔든다.')

person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()

"""

"""
class Animal():
    '''동물'''
    def walk(self):
        print('걷는다.')

    def eat(self):
        print('먹는다.')

    def greet(self):
        print('인사한다.')

#...Human 클래스는 Animal 클래스를 상속받음.
class Human(Animal):
    '''인간'''
    def wave(self):
        print('손을 흔든다.')

    #...부모 메서드를 override함(덮어씀).
    def greet(self):
        self.wave()

class Dog(Animal):
    '''강아지'''
    def wag(self):
        print('꼬리를 흔든다.')

    #...부모 메서드를 override함(덮어씀).
    def greet(self):
        self.wag()

class Cow(Animal):
    '''소'''
    pass

person = Human()
person.greet() #손을 흔든다.

dog = Dog()
dog.greet() #꼬리를 흔든다.

cow = Cow()
cow.greet() #인사한다.
"""

"""
class Animal():
    '''동물'''
    def __init__(self, _name):
        self.name = _name

    def walk(self):
        print('걷는다.')

    def eat(self):
        print('먹는다.')

    def greet(self):
        print('{}이/가 인사한다.'.format(self.name))

#...Human 클래스는 Animal 클래스를 상속받음.
class Human(Animal):
    '''인간'''
    def __init__(self, _name, _hand):
        #..._name 은 부모에서 처리하고
        #   _hand 만 사람이 처리하면 간편함.
        super().__init__(_name)
        self.hand = _hand

    def wave(self):
        print('{}을 흔들면서'.format(self.hand))

    #...부모 메서드를 override함(덮어씀).
    def greet(self):
        self.wave()
        super().greet()

person = Human("사람", "왼손")
person.greet()
#손을 흔든다.

#손을 흔들면서
#인사한다.

#왼손을 흔들면서
#사람이/가 인사한다.
"""

"""
class Animal():
    '''동물'''
    def __init__(self, _name):
        self.name = _name

    def walk(self):
        print('걷는다.')

    def eat(self):
        print('먹는다.')

    def greet(self):
        print('{}이/가 인사한다.'.format(self.name))

#...Human 클래스는 Animal 클래스를 상속받음.
class Human(Animal):
    '''인간'''
    def __init__(self, _name, _hand):
        #..._name 은 부모에서 처리하고
        #   _hand 만 사람이 처리하면 간편함.
        super().__init__(_name)
        self.hand = _hand

    def wave(self):
        print('{}을 흔들면서'.format(self.hand))

    #...부모 메서드를 override함(덮어씀).
    def greet(self):
        self.wave()
        super().greet()

person = Human("사람", "왼손")
person.greet()
#손을 흔든다.

#손을 흔들면서
#인사한다.

#왼손을 흔들면서
#사람이/가 인사한다.
"""

"""
#...내 예외 만들기1 :
#...파일1 : 내 예외 처리 클래스가 있는 파일.
class MyExceptionErr(Exception):
    '''가위 바위 보 가운데 하나가 아닌 값인 경우에 발생하는 에러'''
    pass

#...파일2 : from 파일명 import 클래스 로 가져와서
#   예외 처리함.
#...from 파일 import 클래스
from 파일1 import MyExceptionErr

val = '가'
try:
    if val not in ['가위', '바위', '보']:
        raise MyExceptionErr("가위, 바위, 보 중 하나여야 합니다.")
except MyExceptionErr:
    print("에러가 발생했네요.")

def sign_up():
    '''회원가입 함수'''
"""

"""
#...내 예외 만들기2: 사용자가 정한 오류들을 나눠서 처리할 수 있음.
try:
    sign_up()

except BadUserName:
    print('이름으로 사용할 수 없는 입력이에요.')
except PasswordNotMatched:
    print('입력한 패스워드가 일치하지 않아요.')
"""


"""
#...내 예외 만들기3 :
#...문구점 3곳을 검사해서 '풀'이 있으면 해당 문구점의 이름을
#   출력하고, MyException 을 raise 해서 즉시 for in 문을
#   종료함.
class MyException(Exception):
    pass

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product == '풀':
                print("{}: {}원".format(shop, price))
                raise MyException
except MyException:
    print("풀을 찾았습니다.")
"""

import hashlib
#...아이디어와 암호를 저장하는 변수.
user_db={}

class SignUpErr(Exception):
    '''회원 가입 오류'''
    pass

class UsernameAlreadyExists(Exception):
    '''로그인 아이디 중복'''
    pass

class UnsafePw(Exception):
    '''안전하지 않은 암호'''
    pass

class PwNotMatches(Exception):
    '''암호 확인 불일치'''
    pass


def sign_up(uName, pw, pw_check):
    if uName in user_db.keys():
        raise UsernameAlreadyExists('이미 존재하는 아이디 {}'.format(uName))
    if len(pw) < 6 or uName == pw:
        raise UnsafePw('안전하지 않은 암호입니다.')
    if pw != pw_check:
        raise PwNotMatches('암호가 일치하지 않습니다.')
    #...암호화.
    user_db[uName] = hashlib.sha1('$G:{}:{}'.format(uName, pw).encode()).hexdigest()

try:
    sign_up('hiWorld', 'safe_pw', 'safe_pw')
    sign_up('hiWorld', 'safe_pw', 'safe_pw')
#except Exception as e:
#    print('가입 실패!')
except UsernameAlreadyExists as e:
    print('UsernameAlreadyExists!')
except UnsafePw as e:
    print('UnsafePw!')
except PwNotMatches as e:
    print('PwNotMatches!')