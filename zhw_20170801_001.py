"""
소스상에 한글표기를 위해서는
#coding: cp949 또는 euc-kr, utf-8 한글인코딩방식을 명시해야 함.
"""
#coding: cp949
import os
class People:
    def __init__(self, name='익명', kg=0.0, cm=0.0):
        self.name = input('이름은요?')
        self.kg = int(input('체중은요?'))
        self.cm = int(input('신장은요?'))
        '''
        if {(self.kg < 0) or (self.kg > 200)} :
            raise Exception('체중을 정확하게 입력하세요.')
        if {(self.cm < 0) or (self.cm > 300)} :
            raise Exception('신장을 정확하게 입력하세요.')
        '''
    def disp(self):
        print("이름 : " + self.name, "| 체중 : " + str(self.kg), "| 신장 : " + str(self.cm))

    def makeFile(self):
#...파일쓰기옵션 : http://blog.naver.com/kkrdiamond77/221061357051
        self.f = open('zhw_20170801_input.txt', 'a')
        self.f.write(self.name+'\t'+str(self.kg)+'\t'+str(self.cm) + '\n')
        self.f.close()

    def delFile(self):
#...파일삭제 : http://blog.naver.com/hehe5959/220895050722
        os.remove('zhw_20170801_input.txt')

    def openFile(self):
        self.f = open("zhw_20170801_input.txt", "r")
        return self.f

    def readFile(self, f):
        for line in self.f:
            print(line.strip())
        self.f.close()

    def calcAvgKg(self):
        self.openFile()
        self.zsize = 0
        self.Sumkg = 0.0
        for line in self.f:
            self.zsize += 1
            self.name1, self.kg1, self.cm1 = line.split('\t')
            print("이름1 : " + self.name1, "| 체중1 : " + str(self.kg1), "| 신장1 : " + str(self.cm1))
            self.Sumkg = self.Sumkg + float(self.kg1)
        self.AvgKg = self.Sumkg/self.zsize
        print("평균체중 : " + str(self.AvgKg))


"""
#...다음과제 : 객체상속과 한글처리.
class Doctor(People):
    def __init__(self):
        super(People, self).__init__()
    def makeList(self):
        pass

"""


me = People()
#me.disp()
me.makeFile()
#me.delFile()
f = me.openFile()
me.readFile(f)
me.calcAvgKg() #...평균체중.

#doc = Doctor()

