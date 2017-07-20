class Zoo :
    def __init__(self,name): #num 은 외부에서 입력받으므로 초기자에 설정함.
        self.name = name
    def say(self):
        print('Welcome, ' + self.name + ' zoo!')

s_z = Zoo('봄')
#s_z.name = '봄'
s_z.say()
