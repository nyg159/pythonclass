import turtle

def n_polygon(n, length, position):
    for i in range(8):
        t.penup()
        t.goto(position, 0)
        t.pendown()

        for j in range(n):
            t.forward(length)
            t.left(360//n)
    
        position = position + 100
        n = n + 1

t = turtle.Turtle()
num = int(input("n-각형을 입력하시오. : "))
lengths = int(input("변의 길이를 입력하시오. : "))
positions = int(input("좌표를 입력하시오. : "))

n_polygon(num, lengths, positions)
