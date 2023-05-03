print("9-5.     20173087 노원진\n")

import re
text = '''101 COM PythonProgramming1
102 MAT LinearAlgebra
103 ENG ComputerEnglish'''
# 3개의 대문자로 이루어진 단어를 추출하는 정규식
s = re.findall('[A-Z][A-Z][A-Z]', text) # cf. ('[A-Z]{3}', text)
print(s)