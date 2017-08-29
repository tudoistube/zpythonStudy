#...http://cafe.naver.com/gubass/4705
#...파이썬 tkinker 라디오 버튼 다루기.

from tkinter import *


class Proc:
    def __init__(self):
        w = Tk()
        f = Frame(w)
        label = Label(f, text='색상을 선택하시오. ')
        self.v1 = IntVar()
        #...라디오버튼은 오직 1개만 선택하므로 variable=self.v1 으로 3개 모두 같음.
        #...함수도 각각 만들 수 있지만, self.rb1sel 에서 처리함.
        self.rb1 = Radiobutton(f, text='노랑', bg='yellow', variable=self.v1, value=1, command=self.rb1sel)
        self.rb2 = Radiobutton(f, text='파랑', bg='blue', variable=self.v1, value=2, command=self.rb1sel)
        self.rb3 = Radiobutton(f, text='빨강', bg='red', variable=self.v1, value=3, command=self.rb1sel)
        label.grid(row=1, column=1)
        self.rb1.grid(row=1, column=2)
        self.rb2.grid(row=1, column=3)
        self.rb3.grid(row=1, column=4)
        f.pack()

        self.name = StringVar()
        self.e = Entry(w, textvariable=self.name)
        self.e.pack()

        w.mainloop()

    def rb1sel(self):
        if self.v1.get() == 1:
            self.name.set('노랑')
        if self.v1.get() == 2:
            self.name.set('파랑')
        if self.v1.get() == 3:
            self.name.set('빨강')


Proc()