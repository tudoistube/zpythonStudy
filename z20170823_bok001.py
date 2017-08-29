#...http://cafe.naver.com/gubass/4628
#...위젯 만들기.

from tkinter import *

class Wegdis:
    def __init__(self): #...초기자.
        w = Tk() #...창.
        w.title('제목')

        f = Frame(w)
        f.pack()

        #...인스턴스 변수에는 self 가 붙음.
        self.v1 = IntVar() #...컴포넌트 안에 쓰는 변수에는 IntVar(), StringVar()

        chk = Checkbutton(f, text='진하게', variable=self.v1,
                          command=self.prochk)
        #...체크버튼 배치.1행1열.
        chk.grid(row=1, column=1)

        self.v2 = IntVar()
        rb1 = Radiobutton(f, text='남', bg='blue', variable=self.v2, value=3,
                          command=self.prorb1)
        rb2 = Radiobutton(f, text='여', bg='red', variable=self.v2, value=4,
                          command=self.prorb1)
        #...라디오버튼 배치.1행2열.1행3열.
        rb1.grid(row=1, column=2)
        rb2.grid(row=1, column=3)

        w.mainloop()


    def prochk(self):
        #...체크박스 체크할때 마다 1, 0 출력함.
        print(self.v1.get())

    def prorb1(self):
        print(self.v2.get())


Wegdis()