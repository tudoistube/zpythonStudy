#...http://cafe.naver.com/gubass/4706
#...tkinter 체크박스 다루기.

from tkinter import *

class Proc:
    def __init__(self):
        w = Tk()
        f = Frame(w)
        label = Label(f, text='색상을 선택하시오. ')
        #...체크박스는 여러개를 선택할 수 있으므로, 변수도 각각 만듦.
        self.v1 = IntVar()
        self.v2 = IntVar()
        self.v3 = IntVar()
        self.ck1 = Checkbutton(f, text='노랑', bg='yellow', variable=self.v1, command=self.chk1sel)
        self.ck2 = Checkbutton(f, text='파랑', bg='blue', variable=self.v2, command=self.chk1sel)
        self.ck3 = Checkbutton(f, text='빨강', bg='red', variable=self.v3, command=self.chk1sel)

        label.grid(row=1, column=1)
        self.ck1.grid(row=1, column=2)
        self.ck2.grid(row=1, column=3)
        self.ck3.grid(row=1, column=4)
        f.pack()
        self.name = StringVar()
        self.e = Entry(w, textvariable=self.name)
        self.e.pack()
        w.mainloop()

    def chk1sel(self):
        result = ''
        if self.v1.get() == 1:
            result += '노랑 '
        if self.v2.get() == 1:
            result += '파랑 '
        if self.v3.get() == 1:
            result += '빨강 '
        self.name.set(result)


Proc()