
import turtle


t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.shapesize(3,3)
 
while True:
    n1 = input("명령(r,l,f)을 입력하시오 : ")
    if n1 == "l":
        t.left(90)
        t.forward(100)
    elif n1 == "r":
        t.right(90)
        t.forward(100)
    elif n1 == "f":
        t.forward(100)
    else:
        print("잘못입력하셨습니다.")
