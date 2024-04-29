from wordcloud import WordCloud
import matplotlib.pyplot as plot


# open text file with bag-of-words
with open('cleaned.txt', 'r') as input_file:
    words = input_file.read()


# generate word cloud
wc = WordCloud().generate(words)
plot.imshow(wc)
plot.axis('off')
plot.show()
