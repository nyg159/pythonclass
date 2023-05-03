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