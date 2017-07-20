import turtle as t

n = 5
t.color("lightgreen")
t.pensize(5)
t.begin_fill()

for x in range(n) :
    t.forward(100)
    t.left(360/n)

t.end_fill()
