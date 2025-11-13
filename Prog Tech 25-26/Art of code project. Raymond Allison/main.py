from myfunctions import *
from random import randint
bob.speed(0)
turtle.colormode(255)

jump(0,-175)
bob.width(10)
c=(198,0,0)
c1=("black")
bob.begin_fill()
bob.circle(225)
bob.fillcolor(c)
bob.end_fill()


jump(0,0)
bob.begin_fill()
bob.circle(50)
bob.color("gray")
bob.fillcolor(c1)
bob.end_fill()
jump(0,-100)
r =(121)
g =(41)
b =(41)
color=(r,g,b)
bob.color(r,g,b)
bob.circle(150)
bob.color("black")
#tomoe 1
jump(100,-80)
comet(15,5,"black",15)
#tomoe 2
jump(125,190)
comet(1500,5,"black",15)
#tomoe 3
jump(-185,25)
comet(1500,5,"black",15)

