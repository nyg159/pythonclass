import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(6):
    t.circle(50)
    t.left(360/6)

t.penup()
t.forward(200)
t.pendown()

for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.forward(200)
t.pendown()
    
for i in range(4):
    t.forward(100)
    t.left(360/4)