import turtle as trtl

ryan = trtl.Turtle()
jack = trtl.Turtle()
idk = trtl.Turtle()
james = trtl.Turtle()
josh = trtl.Turtle()
zach = trtl.Turtle()

turtleList = [jack, idk, james, josh, zach, ryan]

x = -100
y = 0

for turtle in turtleList:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x = x + 10

wn = trtl.Screen()
wn.mainloop()