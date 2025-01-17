#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
#shape of turtle and color
tloc = 50
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.speed(0)
    ht.goto(-350, tloc)
    ht.speed(5)
    ht.setheading(0)
    #creates turtle
    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    ht.speed(0)
    vt.goto(-tloc, 350)
    vt.speed(5)
    vt.setheading(270)
    tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
"""
for step in range(50):
	# do something
"""
pixelSize = 30
distance = 3
collisionColor = "grey"
collisionShape = "circle"
for step in range(50):
    for ht in horiz_turtles:
        for vt in vert_turtles:
            ht.forward(distance)
            vt.forward(distance)
        #look for colision
        if  (abs(ht.xcor() - vt.xcor()) < pixelSize):
            if (abs(ht.ycor() - vt.ycor()) < pixelSize):
                horiz_turtles.remove(ht)
                ht.shape(collisionShape)
                ht.fillcolor(collisionColor)
                vert_turtles.remove(vt)
                vt.shape(collisionShape)
                vt.fillcolor(collisionColor)
wn = trtl.Screen()
wn.mainloop()
