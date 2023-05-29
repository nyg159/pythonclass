print("8-5.     20173087 노원진\n")

def process(w):
    output = ""
    for ch in w:
        if ch.isalpha() : 
            output += ch

    return output.lower()

words = set()
next_words = []
fname = input("입력 파일 이름 : ")
file = open(fname, "r")

for line in file:
    lineWords = line.split()
    for word in lineWords:
        words.add(process(word))
        next_words.append(process(word))

numb = len(next_words) - len(words)

print("사용된 단어의 개수 = {}".format(len(words)))
print("중복된 단어의 개수 = {}".format(numb))
print(words)

# process(w) 함수는 단어를 처리하여 알파벳 문자만 추출하고 소문자로 변환하는 역할을 합니다. 
# 이 함수는 입력된 단어에서 알파벳이 아닌 문자를 제거하고, 소문자로 변환한 결과를 반환합니다.
# words는 사용된 단어를 저장하기 위한 집합(set)입니다.
# next_words는 모든 단어를 저장하기 위한 리스트입니다.
# fname에 사용자로부터 입력 파일의 이름을 입력받습니다.
# file은 입력 파일을 읽기 모드로 열기 위한 파일 객체입니다.
# for 루프를 사용하여 파일의 각 줄에 대해 반복합니다.
# lineWords는 각 줄을 단어로 분리한 리스트입니다.
# for 루프를 사용하여 lineWords의 각 단어에 대해 반복합니다.
# process 함수를 사용하여 단어를 처리하고, 처리된 단어를 words에 추가합니다.
# process 함수를 사용하여 단어를 처리하고, 처리된 단어를 next_words에 추가합니다.
# numb 변수는 중복된 단어의 개수를 계산하기 위해 next_words 리스트의 길이에서 words 집합의 길이를 뺀 값을 저장합니다.
# "사용된 단어의 개수 = ..."를 출력하여 사용된 단어의 개수를 출력합니다.
# "중복된 단어의 개수 = ..."를 출력하여 중복된 단어의 개수를 출력합니다.
# words를 출력하여 사용된 단어를 확인할 수 있습니다.
# 이 코드는 입력 파일에서 단어를 처리하고, 사용된 단어의 개수와 중복된 단어의 개수를 출력합니다. 
# 또한, 사용된 단어들을 words 집합에 저장하여 확인할 수 있습니다.

