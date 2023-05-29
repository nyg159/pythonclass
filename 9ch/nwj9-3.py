print("9-3.     20173087 노원진\n")

import random
import string

src_str = string.ascii_letters + '0123456789'
print ('src_str=', src_str, '\n')
n_digits = int(input('몇 자리의 비밀번호를 원하십니까?'))
otp = ''
for i in range(n_digits) :
    idx = random.randrange(len(src_str)) # cf. random.randrange(0, 10)
    otp += src_str[idx]
print(otp)

# string.ascii_letters는 알파벳 대소문자를 나타내는 문자열입니다. 
# '0123456789'는 숫자를 나타내는 문자열입니다. src_str 변수에 알파벳 대소문자와 숫자를 조합하여 저장합니다.
# input() 함수를 사용하여 사용자로부터 비밀번호의 자릿수를 입력받습니다.
# otp 변수를 빈 문자열로 초기화합니다.
# range() 함수와 for 루프를 사용하여 비밀번호의 자릿수만큼 반복합니다.
# random.randrange() 함수를 사용하여 src_str 문자열의 인덱스를 랜덤하게 선택하여 idx 변수에 저장합니다.
# otp에 src_str의 선택된 인덱스의 문자를 추가합니다.
# 반복이 완료되면 생성된 비밀번호를 출력합니다.
# 이 코드는 사용자로부터 입력받은 자릿수에 맞게 알파벳 대소문자와 숫자를 조합하여 랜덤한 비밀번호를 생성하는 기능을 수행합니다. 
# random.randrange() 함수를 사용하여 src_str 문자열의 인덱스를 랜덤하게 선택하여 비밀번호를 구성합니다.
# 이를 통해 원하는 자릿수의 랜덤한 비밀번호를 생성할 수 있습니다.