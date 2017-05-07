# ...117p.키보드로 거북이를 조종해서 그림 그리기
import turtle as t

def turn_right():                    # 오른쪽으로 이동하는 함수
    t.bgcolor("violet")
    t.color("pink")
    t.setheading(0)                  # t.seth(0)로 입력해도 됩니다.
    t.forward(15)                    # t.fd(10)로 입력해도 됩니다.

def turn_up():                       # 위로 이동하는 함수
    t.bgcolor("pink")
    t.color("yellow")    
    t.setheading(90)
    t.forward(15)

def turn_left():                     # 왼쪽으로 이동하는 함수
    t.bgcolor("yellow")
    t.color("green")    
    t.setheading(180)
    t.forward(15)

def turn_down():                    # 아래로 이동하는 함수
    t.bgcolor("green")
    t.color("lime")    
    t.setheading(270)
    t.forward(15)

def blank():                        # 화면을 지우는 함수
    t.bgcolor("lime")
    t.clear()

t.shape("turtle")                   # 거북이 모양을 사용합니다.
t.speed(0)                          # 거북이 속도를 가장 빠르게 지정합니다.

# t.onkeypress(FUNC_NAME, "KEY_NAME") : KEY_NAME 의 첫글자만 대문자임.
t.onkeypress(turn_right, "Right")   # [→]를 누르면 turn_right 함수를 실행합니다.
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")       # [Esc]를 누르면 blank 함수를 실행합니다.

t.listen()                          # 거북이 그래픽 창이 키보드 입력을 받습니다.

# 파이썬IDLE 프로그램이 아닌 파이참과 같은 다른 개발IDE 를 사용하면 실행하자마자
# 결과없이 바로 프로그램이 종료될 수 있음.
# 이때는 t.listen() 아래에 t.mainloop() 을 한줄 추가함.
# t.mainloop() 함수는 사용자가 거북이 그래픽 창을 종료할 때까지 프로그램을 실행하면서
# 마우스나 키보드 입력을 계속 처리하도록 하는 함수임.
t.mainloop()
