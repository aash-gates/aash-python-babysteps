import turtle
  
t = turtle.Turtle()
 
s = 100
t.color("Orange")
t.begin_fill()
for _ in range(4):
  t.forward(s) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree
t.end_fill()

t.color("Green")
t.begin_fill()
t.forward(100)
for _ in range(4):
  t.forward(s) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree
t.end_fill()
  
t.color("Yellow")
t.begin_fill()
t.left(270)
for _ in range(4):
  t.forward(s) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree
t.end_fill()

t.color("black")
t.begin_fill()
t.right(450)
for _ in range(4):
  t.forward(s) # Forward turtle by s units
  t.left(90) # Turn turtle by 90 degree
t.end_fill()