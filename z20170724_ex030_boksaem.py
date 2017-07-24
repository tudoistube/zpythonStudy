class Phone:
    def __init__(self):
        self.name = input('이름은요?')
        self.no = input('번호는요?')
    def disp(self):
        print(self.name, ' | ', self.no)

li=[]
for i in range(3):
    li.append(Phone())

for i in li:
    i.disp()