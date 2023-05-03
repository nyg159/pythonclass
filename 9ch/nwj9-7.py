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