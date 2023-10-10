# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
# then draw a circle
painter.pencolor("blue")
painter.fillcolor("red")
painter.begin_fill()
painter.circle(100)
painter.end_fill()

# move the turtle to another part of the screen
painter.penup()
painter.goto(200, -100)
painter.pendown()

# change both the pen and fill colors
painter.pencolor("green")
painter.fillcolor("yellow")
painter.begin_fill()
painter.circle(100, 360, steps=9)
painter.end_fill()
# then draw a polygon of your choice

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()