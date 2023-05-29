print("9-8.     20173087 노원진\n")

import re
s = 'Korea is awesome! I REALLY LOVE KOREA.'
s_list = re.findall('[kK][Oo][Rr][Ee][Aa]', s)
print('Korea의 출현 횟수 :', len(s_list))

# re.findall() 함수를 사용하여 문자열 s에서 정규식 패턴 [kK][Oo][Rr][Ee][Aa]과 일치하는 문자열을 모두 찾습니다. 
# 이 패턴은 "Korea" 또는 "korea"와 같은 대소문자 구분 없이 "Korea"를 찾습니다.
# s_list에는 re.findall() 함수의 결과로 찾은 모든 패턴이 리스트 형태로 저장됩니다.
# print() 함수를 사용하여 "Korea" 또는 "korea"가 출현하는 횟수를 출력합니다.
# s_list의 길이를 출력하여 해당 횟수를 확인합니다.
# 이 코드는 정규식을 사용하여 문자열에서 "Korea" 또는 "korea"와 같은 패턴을 찾고, 해당 패턴이 출현하는 횟수를 계산하여 출력합니다. 
# 대소문자를 구분하지 않고 "Korea"를 찾기 때문에 대소문자 구분 없이 해당 패턴이 출현하는 횟수를 셀 수 있습니다.