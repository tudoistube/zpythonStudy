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
        pass

p1 = Score()
p2 = Score()
p3 = Score()

p1.kor=90
p1.eng=88
p1.mat=95
p1.tot=p1.kor+p1.eng+p1.mat
p1.avg=p1.tot/3

p2.kor=86
p2.eng=65
p2.mat=100
p2.tot=p2.kor+p2.eng+p2.mat
p2.avg=p2.tot/3

p3.kor=91
p3.eng=81
p3.mat=71
p3.tot=p3.kor+p3.eng+p3.mat
p3.avg=p3.tot/3

print(p1.tot, p1.avg)
print(p2.tot, p2.avg)
print(p3.tot, p3.avg)

