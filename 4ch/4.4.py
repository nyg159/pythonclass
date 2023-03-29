leapyears = 0

while leapyears >= 0:
    leapyears = int(input("연도를 입력하시오 : "))

    if (leapyears % 4 == 0 and leapyears % 100 != 0) or (leapyears % 400 ==0):
        print(f"{leapyears} 년은 윤년입니다.")

    elif leapyears < 0:
        print("프로그램을 종료합니다.")
    else:
        print(f"{leapyears} 년은 윤년이 아닙니다.")
     
