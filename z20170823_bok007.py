#...http://blog.naver.com/nasu0210/220999573729
#...파이썬 GUI 환경 프로그래밍하기.
"""
import tkinter

w=tkinter.Tk()
label=tkinter.Label(w,text='환영합니다.')
button=tkinter.Button(w,text='확인')
label.pack()
button.pack()
w.mainloop()
"""


"""
from tkinter import *

w=Tk()
label=Label(w,text='환영합니다.')
button=Button(w,text='확인')
label.pack()
button.pack()
w.mainloop()
"""

"""
from tkinter import *

def procOk():
     print('ok')

def procCancel():
     print('cancel')

w=Tk()
btOk=Button(w,text='ok',command=procOk,fg='yellow',bg='green')
btCancel=Button(w,text='cancel',command=procCancel,fg='yellow',bg='green')
btOk.pack()
btCancel.pack()
w.mainloop()
"""

"""
#...클래스 사용.
from tkinter import *

class ProButton:
     def __init__(self):
          w=Tk()
          btok=Button(w,text='ok', fg='red',command=self.ok)
          btcancel=Button(w,text='cancel',fg='blue',command=self.cancel)
          btok.pack()
          btcancel.pack()
          w.mainloop()
     def ok(self):
          print('ok')
     def cancel(self):
          print('cancel')

ProButton()
"""

"""
from tkinter import *

class ProButton:
    def __init__(self):
        w = Tk()
        btok = Button(w)
        btok['text'] = 'ok'
        btok['fg'] = 'red'
        btok['bg'] = '#336699'
        btok['command'] = self.ok
        btok['cursor'] = 'circle'  # plus,cross,circle
        btok['justify'] = LEFT
        btok.pack()

        w.mainloop()

    def ok(self):
        print('ok')


ProButton()
"""

"""
from tkinter import *

class Wiget:
     def __init__(self):
          w=Tk()
          w.title('위젯')
          f=Frame(w)
          f.pack()
          self.v1=IntVar()
          cb=Checkbutton(f,text='진하게', variable=self.v1,command=self.cb)
          cb.grid(row=1,column=1)
          self.v2=IntVar()
          rb1=Radiobutton(f,text='남', variable=self.v2,value=1,command=self.rb)
          rb2=Radiobutton(f,text='여', variable=self.v2,value=2,command=self.rb)
          rb1.grid(row=2,column=1)
          rb2.grid(row=2,column=2)
          w.mainloop()
     def cb(self):
          print(self.v1.get())
     def rb(self):
          print(self.v2.get())
Wiget()
"""

from tkinter import *


class Wiget:
    def __init__(self):
        w = Tk()
        w.title('위젯')
        f = Frame(w)
        f.pack()
        self.v1 = IntVar()
        cb = Checkbutton(f, text='진하게', variable=self.v1, command=self.cb)
        cb.grid(row=1, column=1)
        self.v2 = IntVar()
        rb1 = Radiobutton(f, text='남', variable=self.v2, value=1, command=self.rb)
        rb2 = Radiobutton(f, text='여', variable=self.v2, value=2, command=self.rb)
        rb1.grid(row=2, column=1)
        rb2.grid(row=2, column=2)
        f2 = Frame(w)
        f2.pack()
        label = Label(f2, text='이름:')
        label.grid(row=1, column=1)
        self.name = StringVar()
        entry = Entry(f2, textvariable=self.name)
        entry.grid(row=1, column=2)
        button = Button(f2, text='확인', command=self.ok)
        button.grid(row=1, column=3)
        message = Message(f2, text='메세지')
        message.grid(row=1, column=4)
        t = Text(w)
        t.pack()
        t.insert(END, '1234\n')
        t.insert(END, '5678\n')
        t.insert(END, '910')
        w.mainloop()

    def cb(self):
        print(self.v1.get())

    def rb(self):
        print(self.v2.get())

    def ok(self):
        print(self.name.get())
        self.name.set('')

Wiget()

"""
#...http://blog.naver.com/nasu0210/220578596986
#...http://blog.naver.com/nasu0210/220578931184
#...http://blog.naver.com/nasu0210/220579874094
#...http://blog.naver.com/nasu0210/220580738666
#...http://blog.naver.com/nasu0210/220583032062
#...http://blog.naver.com/nasu0210/220584085137
이전 버전인데 대문자를 소문자로 바꿔서 실행해 볼 것.
"""