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
