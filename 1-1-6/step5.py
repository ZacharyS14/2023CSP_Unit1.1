#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used


# Create a spider body
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

# Configures spider legs
legs = 8
lengthoflegs = 70
spacing = 360 / legs - 20
spider.pensize(5)

# Draw Legs
n = 0
while (n < legs):
  spider.goto(0, 20)
  if(n < 4):
    spider.setheading(spacing * n-45)
    spider.forward(lengthoflegs)

  else:
    spider.setheading(spacing * n+45)
    spider.forward(lengthoflegs)
  n += 1

#create eyes
spider.penup()
spider.goto(-15, 40)
spider.pendown()
spider.color("white")
spider.pensize(4)
spider.circle(5)
spider.penup()
spider.goto(10, 40)
spider.pendown()
spider.color("white")
spider.pensize(4)
spider.circle(5)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()