"""
#...파이썬 클래스 활용 : http://blog.naver.com/nasu0210/220860260159
    클래스 : 사용자 정의 자료형.
"""
class Score:
    kor=0
    eng=0
    mat=0
    tot=0
    avg=0.0
    def calc(self):
        self.tot = self.kor + Score.eng + self.mat
        Score.avg = self.tot / 3
    def disp(self):
        print(self.tot, self.avg)


class Score2:
    def __init__(self):
        self.kor=0
        self.eng=0
        self.mat=0
        self.tot=0
        self.avg=0.0
    def calc(self):
        self.tot = self.kor + self.eng + self.mat
        self.avg = round(self.tot / 3, 2)
    def disp(self):
        print(self.tot, self.avg)


class Score3:
    def __init__(self):
        self.kor=int(input('국어점수를 입력하세요.'))
        self.eng=int(input('영어점수를 입력하세요.'))
        self.mat=int(input('수학점수를 입력하세요.'))
        self.tot=0
        self.avg=0.0
    def calc(self):
        self.tot = self.kor + self.eng + self.mat
        self.avg = round(self.tot / 3, 2)
    def disp(self):
        print(self.tot, self.avg)


p1 = Score3()
p2 = Score3()
p3 = Score3()
p1.calc()
p1.disp()
p2.calc()
p2.disp()
p3.calc()
p3.disp()

print(p1.tot, p1.avg)
print(p2.tot, p2.avg)
print(p3.tot, p3.avg)

