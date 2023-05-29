print("9-4.     20173087 노원진\n")

import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wiki = wikipedia.page('pythonprogramming')
text = wiki.content

wordcloud = WordCloud(width = 400, height = 300, stopwords = STOPWORDS).generate(text)

plt.figure(figsize=(40, 30))
plt.imshow(wordcloud)
plt.show()

# wikipedia.page() 함수를 사용하여 'pythonprogramming' 페이지의 내용을 가져옵니다.
# text 변수에 가져온 페이지의 내용을 저장합니다.
# WordCloud 객체를 생성하여 워드클라우드를 설정합니다. width, height는 워드클라우드의 크기를 설정하고, stopwords는 불용어로 처리할 단어들을 설정합니다.
# generate() 함수를 사용하여 텍스트를 기반으로 워드클라우드를 생성합니다.
# plt.figure() 함수를 사용하여 출력할 그림의 크기를 설정합니다.
# plt.imshow() 함수를 사용하여 워드클라우드 이미지를 표시합니다.
# plt.show() 함수를 사용하여 워드클라우드를 출력합니다.
# 이 코드는 Wikipedia에서 가져온 텍스트를 기반으로 워드클라우드를 생성하여 출력하는 기능을 수행합니다. 
# wikipedia.page() 함수를 사용하여 페이지의 내용을 가져온 후, WordCloud 객체를 생성하여 워드클라우드를 설정합니다. 
# 텍스트를 기반으로 워드클라우드를 생성하고, plt.imshow() 함수를 사용하여 이미지를 표시하여 워드클라우드를 출력합니다. 
# 이를 통해 텍스트 데이터의 단어들을 시각화하여 시각적인 형태로 확인할 수 있습니다.