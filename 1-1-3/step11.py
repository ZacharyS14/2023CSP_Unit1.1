#   a113_flower.py
#   This code draws a flower.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# draw flower
painter.color("blue")
painter.goto(20, 190)

for petal in range(18):
    painter.right(20)
    painter.forward(30)
    painter.stamp()

painter.color("green")
painter.goto(20, 160)

for petal in range(12):
    painter.right(30)
    painter.forward(30)
    painter.stamp()

painter.color("yellow")
painter.goto(20, 130)
for petal in range(6):
    painter.right(60)
    painter.forward(30)
    painter.stamp()

wn = trtl.Screen()
wn.mainloop()