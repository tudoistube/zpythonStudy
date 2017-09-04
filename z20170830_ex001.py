class School():
    def __init__(self, zList = list()):
        self.inputDataList = zList
    def inputData(self):
        self.inputDataList.append(("이름", input('이름 : ')))#...튜플로 넣음.
        #...숫자로 입력받음.
        s = "학년은 숫자로 입력(1.대학생 2.고등학생 3.중학생 4.초등학생)"
        grade = int()
        isContinue = True
        while(isContinue):
            try:
                grade = int(input(s))
            except Exception as e:
                if type(e) == ValueError :
                    print("잘못된 입력입니다.")
            finally:
                if type(grade) == int and grade < 5:
                    isContinue = False
                    self.inputDataList.append(("학년", grade))
                else :
                    print('잘못된 입력입니다.')
        self.subjectCnt = int(input('과목수?'))
        for i in range(self.subjectCnt):
            subj = input('과목명'+str(i+1)+":")
            self.inputDataList.append(('과목명'+str(i+1)+":", subj))
        li = []
        for x, y in self.inputDataList:
            if(str(x).startswith("과목명")):
                li.append(y)
        #print(li)
        for i in li:
            self.inputDataList.append((i+"점수:", int(input(i+"점수:"))))
        return self.inputDataList

    def getTotalScore(self):
        self.tot = 0
        for x, y in self.inputDataList:
            if(str(x).endswith("점수:")):
                self.tot += y
        return self.tot

    def getSubjectCnt(self):
        return self.subjectCnt

    def getAvgScore(self):
        self.avg = self.getTotalScore()/self.subjectCnt
        return self.avg

class Daeding(School):
    pass

class Goding(School):
    pass

class Jungding(School):
    pass

class Choding(School):
    pass

'''
s = School()
zinputDataList = s.inputData()
for x, y in zinputDataList:
    print(x, y)
'''

'''
for i in zinputDataList:
    for j in i:
        print(j)

'''

'''
tu = (1, 2)
for x, y in enumerate(tu):
    print('enu: {}, {}'.format(x, y))
'''

student = School()
zinputDataList = student.inputData()
for x in zinputDataList:
    print(x)


for x, y in zinputDataList:
    if str(x) == "학년":
        if y == 1:
            student = Daeding(zinputDataList)
        elif y == 2:
            student = Goding(zinputDataList)
        elif y == 3:
            student = Jungding(zinputDataList)
        else:
            student = Choding(zinputDataList)

print("Total : ".format(student.getTotalScore()))
print("AVG : ".format(student.getAvgScore()))