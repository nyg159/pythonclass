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