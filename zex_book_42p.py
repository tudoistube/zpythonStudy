for x in range(10) :
    print("Hi, it's Spring!")


import turtle as t

#삼각형그리기 47p.
n = int(100)
for x in range(3):
    t.forward(n)
    t.left(120)

#사각형그리기.
for x in range(4) :
    t.forward(n)
    t.left(90)

#원그리기.
for x in range(3) :
    t.circle(80)
    t.forward(n)
