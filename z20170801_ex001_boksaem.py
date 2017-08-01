"""
#...http://cafe.naver.com/gubass/5359
"""
class Stu:
    def input():
        print('***정답 입력***')
        #...self 가 없는 클래스의 변수(Static변수).
        Stu.count = int(input('몇 문항?'))
        while True:
            Stu.dap = input('정답을 입력해주세요.(' + str(Stu.count) + '개) ')
            if len(Stu.dap) == Stu.count:
                break

    def __init__(self, num):
        self.tot = 0
        self.num = num
        print(self.num, '.', end='')
        self.name = input('이름을 입력하세요. ')
        while True:
            print(self.name, end='')
            self.dap = input('답안을 입력해주세요.(' + str(Stu.count) + '개) ')
            if len(self.dap) == Stu.count:
                break

    def calc(self):
        print(self.num, end=' ')
        print(self.name, end=' ')
        for j in range(Stu.count):
            if Stu.dap[j] == self.dap[j]:
                self.tot = self.tot + (100 / Stu.count)
                print('o', end='')
            else:
                print('x', end='')
        print(' ', self.tot, '점')


        # 정답입력

"""
#...self 가 없는 것은 공용의 개념.
    클래스명으로 바로 호출해서 한번만 실행함. 
    마치 math.random 처럼 할 것.
    static 개념으로 이해할 것.
"""
Stu.input()
# 답안입력
print('***답안 입력***')
count = int(input('몇 명?'))

li = []
for i in range(count):
    li.append(Stu(i + 1))

print('***채점 결과***')
for i in li:
    i.calc()