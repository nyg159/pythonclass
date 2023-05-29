print("9-10.     20173087 노원진\n")

import re
s = 'Jian777 is very famous Data scientist. He is only 26 years old but published 19 papers.'
s = re.split(' |\.', s)

eng_word = []
numbers = []
mixed = []

for word in s:
    if word == '':
        continue
    elif re.search('^[A-Za-z]+$', word):  # ^ : 문자열의 시작을 의미
        eng_word.append(word)
    elif re.search('^\d+$', word):
        numbers.append(word)
    else:
        mixed.append(word)

print('영문 단어 :', ' '.join(eng_word))
print('숫자 :', ' '.join(numbers))
print('영문자+숫자 :', ' '.join(mixed))

# re.split() 함수를 사용하여 문자열 s를 공백과 마침표(.)를 기준으로 분할하여 리스트 s에 저장합니다.
# eng_word, numbers, mixed 리스트를 초기화합니다.
# for 루프를 사용하여 s 리스트의 각 단어에 대해 분류 작업을 수행합니다.
# 빈 문자열인 경우, 건너뜁니다.
# re.search() 함수와 정규식을 사용하여 단어가 영문자로만 이루어진 경우 eng_word 리스트에 추가합니다.
# re.search() 함수와 정규식을 사용하여 단어가 숫자로만 이루어진 경우 numbers 리스트에 추가합니다.
# 위 조건에 해당하지 않는 경우 mixed 리스트에 추가합니다.
# print() 함수를 사용하여 각 분류된 리스트들을 출력합니다. 각 리스트의 요소들을 문자열로 변환하여 출력합니다.
# 이 코드는 정규식을 활용하여 문자열을 분할하고, 분할된 단어들을 영문 단어, 숫자, 영문자+숫자로 분류하여 출력합니다. 
# 각 분류된 단어들을 리스트로 저장하여 출력하고, 각 리스트의 요소들을 공백을 포함하여 문자열로 변환하여 출력합니다. 
# 이를 통해 문자열에서 원하는 패턴의 단어들을 추출하여 활용할 수 있습니다.