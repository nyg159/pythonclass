x1 = int(input("x1 의 좌표를 입력하시오. : "))
y1 = int(input("y1 의 좌표를 입력하시오. : "))
x2 = int(input("x2 의 좌표를 입력하시오. : "))
y2 = int(input("y2 의 좌표를 입력하시오. : "))

if x1 <= x2 and y1 <= y2 :
    x3 = x2 - x1
    y3 = y2 - y1
    z2 = x3**2 + y3**2
    z = z2**0.5
    print(f"두 점의 거리 : {z}")

elif x1 >= x2 and y1 <= y2 :
    x3 = x1 - x2
    y3 = y2 - y1
    z2 = x3**2 + y3**2
    z = z2**0.5
    print(f"두 점의 거리 : {z}")

elif x1 >= x2 and y1 >= y2 :
    x3 = x1 - x2
    y3 = y1 - y2
    z2 = x3**2 + y3**2
    z = z2**0.5
    print(f"두 점의 거리 : {z}")

elif x1 <= x2 and y1 >= y2 :
    x3 = x2 - x1
    y3 = y1 - y2
    z2 = x3**2 + y3**2
    z = z2**0.5
    print(f"두 점의 거리 : {z}")

else:
    print("조건이 일치 하지 않습니다.")