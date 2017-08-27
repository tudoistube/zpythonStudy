from tkinter import *

class Form :
    def __init__(self): #...초기자.
        w = Tk()
        w.title('색변경')
        fr = Frame(w) #...윈도우 안에 프레임을 생성함.
        fr.pack()
        self.v1 = IntVar()  # ...정수형자료형.
        self.vRb = IntVar()

        rb1 = Radiobutton(fr, text='빨강', bg='red', command=self.rb, variable=self.vRb, value=1)
        rb1.grid(row=1, column=1)
        rb2 = Radiobutton(fr, text='노랑', bg='yellow', command=self.rb, variable=self.vRb, value=2)
        rb2.grid(row=2, column=1)
        rb3 = Radiobutton(fr, text='녹색', bg='green', command=self.rb, variable=self.vRb, value=3)
        rb3.grid(row=3, column=1)
        rb4 = Radiobutton(fr, text='파랑', bg='blue', command=self.rb, variable=self.vRb, value=4)
        rb4.grid(row=4, column=1)
        self.lb = Label(fr, text='선택한색상', bg='black')
        self.lb.grid(row=5, column=1)

        w.mainloop()

    def rb(self):
        #print('라디오버튼'+str(self.vRb.get()))
        print('라디오버튼이 ' + ('파랑색이 선택되었습니다.'if self.vRb.get()==1 else "녹색이 선택되었습니다."))
        if self.vRb.get() == 1 :
            self.lb['bg'] = 'red'  # ...#RGB
        elif self.vRb.get() == 2 :
            self.lb['bg'] = 'yellow'  # ...#RGB
        elif self.vRb.get() == 3 :
            self.lb['bg'] = 'green'  # ...#RGB
        else:
            self.lb['bg'] = 'blue'  # ...#RGB

Form()