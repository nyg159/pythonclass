print("9-7.     20173087 노원진\n")

import re
text = input('문자열을 입력하시오 :')
upper = re.findall('[A-Z]', text)
lower = re.findall('[a-z]', text)
number = re.findall('[0-9]', text)
others = re.findall('[^A-Za-z0-9]', text)
print('대문자, 소문자, 숫자, 특수문자의 개수')
print('대문자 =', len(upper))
print('소문자 =', len(lower))
print('숫자 =', len(number))
print('특수문자 =', len(others)) # [^abc] : 문자 제외범위

# input() 함수를 사용하여 사용자로부터 문자열을 입력받습니다.
# re.findall() 함수와 정규식을 사용하여 대문자, 소문자, 숫자, 특수문자를 추출하여 각각 upper, lower, number, others 리스트에 저장합니다.
# [A-Z]: 대문자를 찾습니다.
# [a-z]: 소문자를 찾습니다.
# [0-9]: 숫자를 찾습니다.
# [^A-Za-z0-9]: 대소문자와 숫자를 제외한 특수문자를 찾습니다.
# print() 함수를 사용하여 대문자, 소문자, 숫자, 특수문자의 개수를 출력합니다. 
# 각 리스트의 길이를 출력하여 해당 개수를 확인합니다.
# 이 코드는 정규식을 사용하여 문자열에서 대문자, 소문자, 숫자, 특수문자를 추출하고, 각각의 개수를 계산하여 출력합니다.
# re.findall() 함수를 활용하여 정규식 패턴과 일치하는 문자열을 모두 추출하고, 추출된 문자열의 개수를 len() 함수를 통해 세어 출력합니다.
# 이를 통해 문자열에 포함된 대소문자, 숫자, 특수문자의 개수를 셀 수 있습니다.