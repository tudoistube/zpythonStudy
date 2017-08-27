#from foler import module
from tkinter import *

def prOk() :
    print('Okay 버튼이 클릭되었습니다.')

def prCancel() :
    print('취소 되었습니다.')

w = Tk() #...창.
label = Label(w, text='안녕하세요')
label.pack() #...pack() : 알아서 배치.

#...버튼을 누를때마다 함수 prok() 를 호출해서 콘솔에 출력됨.
bt = Button(w, text='Okay', command=prOk, bg='green', fg='yellow')
bt.pack()
bt1 = Button(w, text='Cancel', command=prCancel, bg='green', fg='white')
bt1.pack()

lb = Label(w, text='라벨입니다', bg="cyan")
lb.pack()

w.mainloop() #...이벤트를 받을때 까지 기다리기.사라지지 않음.