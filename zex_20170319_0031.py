print('---------------')

class Person : 
    def __init__(self) : #초기자.
        self.nam = input('학생이름은?')
        self.kor = input('국어점수는?')
        self.eng = input('영어점수는?')
        self.mat = input('수학점수는?')
        self.tot = int(self.kor) + int(self.eng) + int(self.mat)
        self.avg = int(self.tot)/3

        print('학생이름:{0}, 국어:{1}, 영어:{2}, 수학:{3}, 총점:{4}, 평균 : {5}'.format(self.nam, self.kor, self.eng, self.mat, self.tot, round(self.avg,2)))
        
li = [] #리스트
for i in range(2):
    li.append(Person())

cnt = int()
kor = int()
eng = int()
mat = int()
avgK = int()
avgE = int()
avgM = int()
tot = int()
avg = int()
for i in li:
    cnt = cnt +1
    kor += int(i.kor)
    eng += int(i.eng)
    mat += int(i.mat)
    avgK = kor/cnt
    avgE = eng/cnt
    avgM = mat/cnt
    tot += kor + eng + mat
    avg = tot/cnt

    print(tot, avg)


print('===============')
