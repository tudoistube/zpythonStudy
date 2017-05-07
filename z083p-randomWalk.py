# ...082p.range(start, end - 1) : end 가 포함되지 않음.
#               random(start, end) : end 가 포함됨.
# 마음대로 걷는 거북이1
import turtle as t
import random

t.shape("turtle")                   # ‘거북이’ 모양의 거북이 그래픽을 사용합니다.
t.pensize(3)
t.bgcolor("cyan")
t.color("blue")
t.speed(10)

for x in range(1500):                # 거북이를 500번 움직입니다.
    a = random.randint(1, 360)      # 1~360 사이의 아무 수나 골라 a에 저장합니다.
    t.setheading(a)                 # a 각도로 거북이의 방향을 돌립니다.
    b = random.randint(1, 20)
    t.forward(b)                   # 거북이를 10만큼 앞으로 이동합니다.
