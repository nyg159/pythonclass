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



