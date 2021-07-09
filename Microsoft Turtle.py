import turtle
  
t = turtle.Turtle()
 
s = 100
t.screen.colormode(255)
t.color(243, 79, 28)
t.begin_fill()
for _ in range(4):
  t.forward(s) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree
t.end_fill()

t.screen.colormode(255)
t.color(127, 188, 0)
t.begin_fill()
t.forward(100)
for _ in range(4):
  t.forward(s) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree
t.end_fill()
  
t.screen.colormode(255)
t.color(243, 79, 28)
t.begin_fill()
t.left(270)
for _ in range(4):
  t.forward(s) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree
t.end_fill()

t.screen.colormode(255)
t.color(243, 79, 28)
t.begin_fill()
t.right(450)
for _ in range(4):
  t.forward(s) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree
t.end_fill()