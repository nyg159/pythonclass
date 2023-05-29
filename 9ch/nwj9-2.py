print("9-2.     20173087 노원진\n")

t = "It's Not The Right Time To Conduct Exams. MY DEMAND IN BOLD AND CAPITAL. NO EXAMS IN COVID!!!"
tcount = 0
count = 0

print('느낌표 개수 :', t.count('!'))
for ch in t:
    tcount+=1
    if ch.isupper():
        count += 1
print('총 문자 개수 :', tcount)
print('대문자 개수 :', count)

# t 변수에 주어진 문자열을 저장합니다.
# t.count('!')를 사용하여 문자열에서 느낌표의 개수를 세어 출력합니다.
# for 루프를 사용하여 문자열의 각 문자에 대해 반복합니다.
# tcount 변수를 사용하여 문자의 개수를 세는데 사용합니다.
# ch.isupper()를 사용하여 대문자인지 확인하고, 대문자인 경우 count 변수를 증가시킵니다.
# tcount 변수는 문자열의 총 문자 개수를 나타내고, count 변수는 대문자 개수를 나타냅니다.
# 총 문자 개수와 대문자 개수를 출력합니다.
# 이 코드는 주어진 문자열에서 느낌표의 개수와 대문자의 개수를 세는 기능을 수행합니다. 
# t.count('!')를 사용하여 문자열에서 느낌표의 개수를 세고, for 루프와 isupper() 함수를 사용하여 대문자인 경우 count 변수를 증가시킴으로써 대문자의 개수를 세어 출력합니다.
#    이를 통해 주어진 문자열에서 느낌표와 대문자의 개수를 확인할 수 있습니다.