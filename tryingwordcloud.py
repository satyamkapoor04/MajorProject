from wordcloud import WordCloud
import matplotlib.pyplot as plt

stopwords = set()


words = ' hello world how are you I am good and I know this would be the last '

wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=stopwords, min_font_size=10).generate(words)

plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
