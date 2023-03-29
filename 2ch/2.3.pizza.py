from cmath import pi

radius = float(input("피자의 반지름을 입력하세요(cm) : "))
PI = 3.14
surface = PI * (radius ** 2)
round = 2 * PI * radius
print(f"피자의 면적은 {surface} 이고, 피자의 둘레는 {round}이다.")
