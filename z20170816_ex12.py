from tkinter import *

class Form :
    def __init__(self): #...초기자.
        w = Tk()
        bt1 = Button(w, text='Okay', command=self.prOk, bg='green', fg='yellow')
        bt2 = Button(w, text='Cancel', command=self.prCancel, bg='green', fg='yellow')
        bt3 = Button(w, text='Show', bg='white')
        bt3['text']='ShowMore...' #...버튼 속성 변경.
        bt3['bg']='blue'
        bt3['fg']='#AB84F9' #...#RGB
        bt3['cursor']='plus' #...커서가 '+' 로 바뀜.
        bt3['justify']=RIGHT

        bt1.pack()
        bt2.pack()
        bt3.pack()
        w.mainloop()

    def prOk(self): #...self 는 클래스소속의 함수임을 명시함.
        print('Okay 버튼이 클릭되었습니다.')

    def prCancel(self): #...self 는 클래스소속의 함수임을 명시함.
        print('Cancel 버튼이 클릭되었습니다.')

Form() #...객체를 호출함.
