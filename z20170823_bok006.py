#...http://blog.naver.com/nasu0210/221004873085
#...성적관리.
from tkinter import *


class SungjukForm:
    def __init__(self):
        w = Tk()
        w.title('성적계산')
        f = Frame(w)
        f.pack()

        lbname = Label(f, text='이름')
        lbname.grid(row=1, column=1)
        self.name = StringVar()
        enname = Entry(f, textvariable=self.name)
        enname.grid(row=1, column=2)

        lbkor = Label(f, text='국어')
        lbkor.grid(row=2, column=1)
        self.kor = IntVar()
        enkor = Entry(f, textvariable=self.kor)
        enkor.grid(row=2, column=2)

        lbeng = Label(f, text='영어')
        lbeng.grid(row=3, column=1)
        self.eng = IntVar()
        eneng = Entry(f, textvariable=self.eng)
        eneng.grid(row=3, column=2)

        lbmat = Label(f, text='수학')
        lbmat.grid(row=4, column=1)
        self.mat = IntVar()
        enmat = Entry(f, textvariable=self.mat)
        enmat.grid(row=4, column=2)

        bt1 = Button(f, text='확인', command=self.ok)
        bt1.grid(row=5, column=1)
        bt2 = Button(f, text='취소', command=self.cs)
        bt2.grid(row=5, column=2)

        self.tot = StringVar()
        self.message = Message(f, textvariable=self.tot)
        self.message.grid(row=6, column=1)
        w.mainloop()

    def ok(self):
        print('이름:' + self.name.get())
        print('총점:' + str(self.kor.get() + self.eng.get() + self.mat.get()))
        print('평균:' + str((self.kor.get() + self.eng.get() + self.mat.get()) / 3))
        self.message['textvariable'] = self.tot #...일반 자료형은 안들어감.

    def cs(self):
        self.name.set('')
        self.kor.set('')
        self.eng.set('')
        self.mat.set('')


SungjukForm()