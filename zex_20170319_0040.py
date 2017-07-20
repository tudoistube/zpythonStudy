#객관식 점수 채점 http://blog.naver.com/nasu0210/220906806727
class Stu:
    
    def __init__(self,num): #num 은 외부에서 입력받으므로 초기자에 설정함.
        self.number = 5
        self.num=num
        print(self.num,'.', end='') #end='' : 줄바꿈안함.

        self.name=input('이름을 입력하세요. ')
        while True:
            print(self.name, end='')
            self.dap=input(':: 답안을 입력해주세요.(' + str(self.number) + '개) ')
            if len(self.dap)== self.number :
                break


numProblem = 5
people = 2        

print('***정답입력***')
while True :
    dap = input('정답을 입력하세요.('+ str(numProblem) +'개)')
    if len(dap) == numProblem :
        break

print('***답안입력***')
li=[]
for i in range(people):
    li.append(Stu(i+1)) #학생번호를 1부터 시작하게 보이기 위함.
    
print(type(li))


print('***채점 결과***')
for i in li:
    tot=0
    print(i.num,end=' ')
    print(i.name,end=' ')
    for j in range(numProblem):
        if dap[j]==i.dap[j]:
            tot=tot+5
            print('o',end='')
        else:
            print('x',end='')
    print(' ',tot,'점')   




