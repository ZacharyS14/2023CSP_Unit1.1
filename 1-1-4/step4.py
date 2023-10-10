#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

space = 50 # the radius of the circle
angle = 65 # experiment
seg = int(360/angle) # the length of a line

# Add a loop with a zero-iteration condition

start_loop = 'n'

while (start_loop == 'y'):
  painter.right(angle)
  painter.forward(space)
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()

# Add an infinite loop

startloop= input('y')

while (startloop == 'y'):
  painter.right(angle)
  painter.forward(space)
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()


wn = trtl.Screen()
wn.mainloop()