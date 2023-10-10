#   Add your code here and add comments to your code
#   to describe what each section of code is doing
# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle


# move the turtle to another part of the screen
painter.penup()
painter.goto(200, -100)
painter.pendown()

painter.pencolor("black")
painter.fillcolor("green")
painter.begin_fill()
painter.circle(100)
painter.end_fill()

painter.penup()
painter.goto(170, 50)
painter.pendown()

painter.circle(10, 360)

painter.penup()
painter.goto(220, 50)
painter.pendown()

painter.circle(10, 360)


wn = trtl.Screen()
wn.mainloop()
