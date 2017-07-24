"""
이름    |  금액  |  이자율  | 이자  | 총금액
홍길동  | 100000 |  0.02    | 2000  | 102000
"""
class Book:
    def __init__(self):
        self.name = input('이름은요?')
        self.amt  = int(input('금액은요?'))
        self.rate = 0.02
        self.interests = 0
        self.total = 0
    def calc(self):
        #self.rate = 0.02
        self.interests = self.amt * self.rate
        self.total = self.amt + self.interests
    def disp_title(self):
        print('이름    |   금액   |   이율   |   이자   |   총금액')
    def disp(self):
        print(self.name, ' | ', self.amt, ' | ', self.rate, ' | ', self.interests, ' | ', self.total)

class Book2:
    #...클래스변수 : 공통은 self 가 아닌 클래스명을 붙여서 사용함.
    rate = float(input('이율은요?'))
    def __init__(self):
        #...인스턴스변수 : self.
        self.name = input('이름은요?')
        self.amt  = int(input('금액은요?'))
    def calc(self):
        self.interests = self.amt * Book2.rate
        self.total = self.amt + self.interests
    def disp_title(self):
        print('이름    |   금액   |   이율   |   이자   |   총금액')
    def disp(self):
        # ...공통은 self 가 아닌 클래스명을 붙여서 사용함.
        print(self.name, ' | ', self.amt, ' | ', Book2.rate, ' | ', self.interests, ' | ', self.total)


"""
b = Book()
b.calc()
b.disp()
"""

li=[]
for i in range(3):
    li.append(Book())

for i in li:
    i.calc()

cnt = 0
for i in li:
    cnt = cnt + 1
    if(cnt == 1) : i.disp_title()
    i.disp()