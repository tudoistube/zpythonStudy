#...http://cafe.naver.com/gubass/4655
#...위젯 만들기.

from tkinter import *

class Proc:
    def __init__(self):
        w = Tk()
        f = Frame(w)
        f.pack()

        label = Label(f, text='이름')
        label.grid(row=1, column=1)

        button1 = Button(f, text='확인', fg='blue', command=self.btok)
        button2 = Button(f, text='취소', bg='red', command=self.btcancel)
        button1.grid(row=1, column=3)
        button2.grid(row=1, column=4)

        self.name = StringVar()
        self.e = Entry(f, textvariable=self.name)  #...Entry : TextBox.
        self.e.grid(row=1, column=2)

        self.t = Text(w)
        self.t.pack()

        w.mainloop()


    def btok(self):
        #...self.name.get() : Entry 의 값.
        self.t.insert(END, self.name.get() + '\n')
        # ...self.name.set('') : Entry 의 값이 지워짐.
        self.name.set('')

    def btcancel(self):
        self.name.set('')


Proc()