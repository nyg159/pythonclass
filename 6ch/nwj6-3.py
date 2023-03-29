import turtle


def drawBar(height):
    if d < 100:
        t.fillcolor("blue")
    elif d > 100 and d < 300:
        t.fillcolor("yellow")
    elif d > 300:
        t.fillcolor("red")

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font= ('Time New Roman', 16, 'bold'))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


t = turtle.Turtle()
t.color("blue")
##t.fillcolor("red")
t.pensize(3)



data = [120, 56, 309, 220, 156, 23, 90]

for d in data:
    drawBar(d)

t.penup()
t.goto(-200, 100)
t.pendown()
t.write("20173087 노원진")

