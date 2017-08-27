from tkinter import *

class Form :
    def __init__(self): #...초기자.
        w = Tk()
        w.title('글제목')
        fr = Frame(w) #...윈도우 안에 프레임을 생성함.
        fr.pack()
        self.v1 = IntVar()  # ...정수형자료형.
        self.vRb = IntVar()
        #self.v1 = 0 #...AttributeError: 'int' object has no attribute 'get'
        cb1 = Checkbutton(fr, text='진하게', command=self.chk, variable=self.v1)
        cb1.grid(row=1, column=1)
        rb1 = Radiobutton(fr, text='파랑', bg='blue', command=self.rb, variable=self.vRb, value=1)
        rb1.grid(row=1, column=2)
        rb2 = Radiobutton(fr, text='녹색', bg='green', command=self.rb, variable=self.vRb, value=2)
        rb2.grid(row=1, column=3)

        fr2 = Frame(w) #...윈도우 안에 프레임을 생성함.
        fr2.pack()
        self.name=StringVar()
        lb = Label(fr2, text='이름을 입력하세요')
        lb.grid(row=1, column=1)
        et=Entry(fr2, textvariable=self.name) #...텍스트박스.
        et.grid(row=1, column=2)
        bt = Button(fr2, text='확인', command=self.btOkay)
        bt.grid(row=1, column=3)
        #...Label 은 고정이고, Message 는 유동적이어서 창사이즈를 줄이면 가려짐.
        msg=Message(fr2, text='메시지입니다.')
        msg.grid(row=1, column=4)

        tx=Text(w)
        tx.pack()
        tx.insert(END, '글자를 추가합니다.\n다음줄...\n')
        tx.insert(END, '글자를 추가합니다2.\n다음줄...\n')

        w.mainloop()

    def chk(self):
        #print('체크버튼'+str(self.v1.get()))
        """
        print('체크버튼이 ', end='')
        if self.v1.get() == 1:
            print('선택되었습니다.')
        else :
            print("해제되었습니다.")
        """
        print('체크버튼이 ' + ('선택되었습니다.'if self.v1.get()==1 else "해제되었습니다."))

    def rb(self):
        #print('라디오버튼'+str(self.vRb.get()))
        print('라디오버튼이 ' + ('파랑색이 선택되었습니다.'if self.vRb.get()==1 else "녹색이 선택되었습니다."))

    def btOkay(self):
        print('당신의 이름은 '+self.name.get()+' 입니다.')
        self.name.set('') #...이름 입력하고 텍스트박스 지움.

Form()