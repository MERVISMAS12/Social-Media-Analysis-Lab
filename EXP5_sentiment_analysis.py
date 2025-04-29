import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from wordcloud import WordCloud

df = pd.read_csv('twitter_dataset.csv')
df = df.dropna(subset=['Tweet', 'Sentiment'])

sns.countplot(data=df, x='Sentiment')
plt.title("Sentiment Distribution")
plt.show()

#sample tweets

print(f"\n\nPositive Sentiments: \n {df[df['Sentiment'] == 'positive']['Tweet'].head(5)}")
print(f"\n\nNeutral Sentiments: \n {df[df['Sentiment'] == 'neutral']['Tweet'].head(5)}")
print(f"\n\nNegative Sentiments: \n {df[df['Sentiment'] == 'negative']['Tweet'].head(5)}")

#word cloud
sentiments = ['positive', 'negative', 'neutral']

for s in sentiments:
    text = " ".join(df[df['Sentiment'] == s]['Tweet'])
    wc = WordCloud(height=400, width= 800, background_color='white', stopwords='english').generate(text)
    plt.imshow(wc)
    plt.title(f'Word Cloud for {s} sentiment')
    plt.axis('off')
    plt.show()