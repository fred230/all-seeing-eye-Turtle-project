import turtle as t
import colorsys

screen = t.Screen()
screen.bgcolor("black")


t.pensize(1)
t.speed(2)

n= 36
h=1

t.goto(-60,0)

for i in range(20):
    c= colorsys.hsv_to_rgb(h,1,0.9)
    t.pencolor(c)
    h += 1 / n
    t.circle(105,103)
    t.backward(98)
    t.right(60)
    t.circle(70,68)
    t.left(87)
    t.backward(108)
    t.forward(150)

r = 111
t.penup()
t.goto((0,-67))
t.pendown()
for i in range (100):
    c= colorsys.hsv_to_rgb(h,1,0.9)
    t.pencolor(c)
    h+=1/n
    t.circle(r+i,20)
t.done()