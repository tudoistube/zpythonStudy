class Person : 
    def __init__(self) : #초기자.
        #kor, eng, mat 는 지역변수이므로 self 가 필요없고
        #nam, tot 는 외부에서 참조하는 경우 클래스변수이고 self 가 필요함.
        self.nam = input('학생이름은?')
        kor = int(input('국어점수는?'))
        eng = int(input('영어점수는?'))
        mat = int(input('수학점수는?'))
        self.tot = kor + eng + mat
        avg = self.tot/3

    def disp(self):    #클래스 소속이고 다른 메서드에서 참조할 경우 변수에 self 가 있어야 함.
        print(self.nam)
        print(self.tot)
        print('학생이름:{0}, 국어:{1}, 영어:{2}, 수학:{3}, 총점:{4}, 평균 : {5}'.format(self.nam, self.kor, self.eng, self.mat, self.tot, round(self.avg,2)))


#res = Person()
#res.disp()
print('===============')

class Person : 
    def __init__(self) : #초기자.
        self.nam = input('학생이름은?')
        self.kor = int(input('국어점수는?'))
        self.eng = int(input('영어점수는?'))
        self.mat = int(input('수학점수는?'))
        self.tot = self.kor + self.eng + self.mat
        self.avg = round(self.tot/3, 2)

    def dispTitle(self):    #클래스 소속이고 다른 메서드에서 참조할 경우 변수에 self 가 있어야 함.
        print('학생이름 | 국어 | 영어 | 수학 | 총점 | 평균')
        
    def dispItem(self):    #클래스 소속이고 다른 메서드에서 참조할 경우 변수에 self 가 있어야 함.
        print('{0} | {1} | {2} | {3} | {4} | {5}'.
                  format(self.nam, self.kor, self.eng, self.mat, self.tot, self.avg,2))
        
    def disp(self) :
        self.dispTitle()
        self.dispItem()

#res = Person()
#res.disp()
