import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

df = pd.read_csv("keyword_matches.csv", index_col=0)
keyword = df.value_counts('KEYWORD')

plt.figure(figsize=(15,10))
keyword.sort_values(ascending=False).plot.bar()
plt.xticks(rotation=90)
plt.xlabel("Keyword")
plt.ylabel("Count of Mentions")
plt.show()

text = " ".join(keyword for keyword in df.KEYWORD)

wordcloud = WordCloud(width=3200, height=1600, max_words=100, background_color="white", collocations = False).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
wordcloud.to_file("keyword.png")