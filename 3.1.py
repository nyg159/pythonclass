import turtle

t = turtle.Turtle()
t.shape('turtle')

while True:
    square = int(input("몇각형을 그리시겠어요? : "))
    angles = 360 // square
    notang = 360 % square

    if notang == 0 and 0 < angles : 
        i = 1

        while i <= square :
            i = i + 1
            t.forward(100)
            t.left(angles)
            
        t.penup()
        t.forward(200)
        t.pendown()

    else :
        print('각도가 정수만 가능합니다.')

        
        