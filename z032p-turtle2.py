#...028p.거북이 그래픽의 짧은 명령어.
#              forward → fd.
#              left → lt.
#              right → rt.

# ...032p.거북이 그래픽-도형그리기2
# ...033p.단축키 :: 실행 : F5.
import turtle as t
# 삼각형 그리기
print("삼각형 그리기.")
t.color("orange")      # <추가> 펜 색상을 빨간색으로 바꿉니다.
t.pensize(2)        # <추가> 펜 두께를 3으로 바꿉니다.
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

# 사각형 그리기
print("사각형 그리기.")
t.color("green")   # <추가> 펜 색상으로 녹색으로 바꿉니다.
t.pensize(3)        # <추가> 펜 두께를 3으로 바꿉니다.
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# 원
print("원 그리기.")
t.color("blue")     # <추가> 펜 색상을 파란색으로 바꿉니다.
t.pensize(5)        # <추가> 펜 두께를 5로 바꿉니다.
t.circle(50)
