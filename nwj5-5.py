import turtle


t = turtle.Turtle()
t.speed(0)
t.width(2)
i = -250
t.penup()
t.goto(-250, 0)
t.pendown()

while True:
    a = int(input("각도를 입력하시오. : "))
    i = i + 250
    if a <=  0:
        print("프로그램을 종료합니다.")
        break
    
    length = 10
    while length < 200:
        t.forward(length)
        t.right(a)
        length += 5
    t.penup()
    t.goto(i,0)
    t.pendown()