import turtle

t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100,100)
t.write("두 수 모두 양수")
t.goto(100, -100)
t.write("두 번째 수만 음수")
t.goto(-100, -100)
t.write("두 수 모두 음수")
t.goto(-100, 100)
t.write("첫 번째 수만 양수")
t.goto(0,0)
t.pendown()

num1 = int(turtle.textinput("", "첫 번째 숫자를 입력하세요. : "))
num2 = int(turtle.textinput("", "두 번째 숫자를 입력하세요. : "))

if num1 > 0 and num2 > 0:
    t.goto(100,100)
    
elif num1 > 0 and num2 < 0:
    t.goto(100, -100)
    
elif num1 < 0 and num2 < 0:
    t.goto(-100, -100)
    
elif num1 < 0 and num2 > 0:
    t.goto(-100, 100)
     
else:
    t.goto(0,0)  
    turtle.done