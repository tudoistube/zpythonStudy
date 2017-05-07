# ...059p.거북이 그래픽 명령어.
'''
t.forward(100)
t.fd(100)

t.backward(1)
t.back(1)

t.left(45)
t.lt(45)

t.right(45)
t.rt(45)

t.circle(50)

t.down()
t.pendown()

t.up()
t.penup()

t.shape("classic"), t.shape("turtle"), t.shape("triangle")

t.speed(1) : 가장느린속도.
t.speed(10) : 빠른속도.
t.speed(0) : 최고속도.

t.pensize(3)
t.color("green")
t.bgcolor("blue")
t.fillcolor("lime")
t.begin_fill() : 도형 내부를 색칠할 준비를 함.
t.end_fill()

t.showturtle(), t.st() : 거북이를 화면에 표시함.
t.hideturtle(), t.ht() : 거북이를 화면에서 가림.

t.clear() : 거북이를 그대로 두고 화면을 지움.
t.reset() : 화면을 지우고 거북이도 원래 자리와 상태로 되돌림.
'''
# 정오각형을 그리기 프로그램
import turtle as t

n = 12                 # 오각형을 그립니다(다른 값을 입력하면 다른 도형을 그립니다).
t.color("lime")
t.begin_fill()        # 색칠할 영역을 시작합니다.
for x in range(n):    # n번 반복합니다.
    t.forward(50)     # 거북이 50만큼 앞으로 이동합니다.
    t.left(360/n)     # 거북이 360/n 만큼 왼쪽으로 회전합니다.
t.end_fill()          # 색칠할 영역을 마무리합니다.
