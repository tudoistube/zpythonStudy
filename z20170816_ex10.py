#from foler import module
from tkinter import *

w = Tk() #...창.
label = Label(w, text='안녕하세요')
label.pack() #...pack() : 알아서 배치.

bt = Button(w, text='확인')
bt.pack()

lb = Label(w, text='라벨입니다')
lb.pack()

w.mainloop() #...이벤트를 받을때 까지 기다리기.사라지지 않음.