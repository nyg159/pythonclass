height = int(input("키를 입력하세요(cm) : "))
weight = float(input("몸무게를 입력하세요(kg) : "))
bmi = weight / (height/100) **2
print("당신의 BMI는", round(bmi,2), "입니다.")