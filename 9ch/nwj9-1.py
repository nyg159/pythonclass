print("9-1.     20173087 노원진\n")

t = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '

print('[원시 데이터]')
print(t, '\n\n')
low_t = t.lower()
t = ''
for word in low_t.split(' '):
    if word == 'kt' or word == 'samsung' or word == 'lg' or word == 'skt':
        t += '* '
    else:
        t += word + ' '
print('[처리된 결과]')
print(t)

# t 변수에 주어진 원시 데이터 문자열을 저장합니다.
# print('[원시 데이터]')를 사용하여 원시 데이터 문자열을 출력합니다.
# t.lower()를 사용하여 문자열을 소문자로 변환한 후, low_t 변수에 저장합니다.
# t 변수를 빈 문자열로 초기화합니다.
# low_t.split(' ')를 사용하여 소문자로 변환된 문자열을 공백을 기준으로 분할하여 단어들의 리스트로 만듭니다.
# for 루프를 사용하여 단어들을 반복합니다.
# 각 단어가 특정 단어인 경우 ('kt', 'samsung', 'lg', 'skt') 해당 단어를 *로 대체하고, 그렇지 않은 경우에는 그대로 유지합니다.
# t 변수에 변환된 단어를 추가하고, 공백을 추가하여 원래의 문장 형태를 유지합니다.
# print('[처리된 결과]')를 사용하여 처리된 결과를 출력합니다.
# 이 코드는 주어진 문자열에서 특정 단어들을 마스킹 처리하는 기능을 수행합니다. 
# 주어진 문자열을 소문자로 변환한 후, 단어들을 공백을 기준으로 분할하여 단어들의 리스트로 만듭니다. 
# 그리고 각 단어가 특정 단어인 경우 *로 대체하고, 그렇지 않은 경우에는 그대로 유지하여 처리된 결과를 출력합니다. 
# 이를 통해 원시 데이터에서 특정 단어들을 마스킹 처리한 결과를 확인할 수 있습니다.