print("9-9.     20173087 노원진\n")

import string
src_str = string.ascii_uppercase + string.ascii_lowercase # cf. sring.ascii_letters

def cipher(a): # 암호화 코드를 만드는 함수
    idx = src_str.index(a)
    return dst_str[idx]

src = input('문장을 입력하시오 : ')
size = int(input('이동시킬 칸 수를 입력하시오 : '))
dst_str = src_str[size:] + src_str[:size]

print('암호화된 문장 : ', end='')

for ch in src:
    if ch in src_str:
        print(cipher(ch), end='')
    else:
        print(ch, end='')

#         string.ascii_uppercase와 string.ascii_lowercase를 사용하여 대문자와 소문자를 포함한 알파벳 문자열 src_str을 생성합니다.
# cipher() 함수는 암호화를 수행하는 함수로, 입력된 문자 a의 인덱스를 src_str에서 찾고, 해당 인덱스에 해당하는 암호화된 문자를 반환합니다.
# 사용자로부터 문장과 이동시킬 칸 수를 입력받습니다.
# dst_str은 src_str을 이동시킬 칸 수에 따라 조정한 암호화 문자열입니다.
# print() 함수를 사용하여 암호화된 문장을 출력합니다.
# 입력된 문장의 각 문자에 대해 암호화 함수를 적용하여 암호화된 문자를 출력합니다. src_str에 속하지 않는 문자는 그대로 출력합니다.
# 이 코드는 암호화 함수를 통해 문자열을 암호화하는 기능을 수행합니다. 
# 알파벳 대문자와 소문자를 포함한 문자열을 사용하여 암호화에 필요한 문자열을 생성하고, 이를 이용하여 입력된 문장을 암호화하여 출력합니다. 
# 사용자가 입력한 칸 수에 따라 문자열을 이동시키는 방식으로 암호화가 이루어집니다.