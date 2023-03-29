import turtle

t = turtle.Turtle()
t.shape("turtle")

shapes = str(turtle.textinput("", "도형을 입력하세요.(사각형, 원, 정삼각형) : "))

if shapes == "사각형":
    s = int(turtle.textinput("", "가로: "))
    w = int(turtle.textinput("", "세로: "))
    i = 0

    while i < 2:
        t.forward(s)
        t.left(90)
        t.forward(w)
        t.left(90)
        i = i + 1
    
    
elif shapes == "원":
    r = int(turtle.textinput("", "반지름을 입력하시오. : "))
    t.circle(r)

elif shapes == "정삼각형":
    l = int(turtle.textinput("","변의 길이를 입력하시오. : " ))
    i = 0

    while i < 3 :
        t.forward(l)
        t.left(120)
        i = i + 1

else:
    print("존재하는 도형이 없습니다.")

