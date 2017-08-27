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


Form()