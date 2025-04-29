import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

df = pd.read_csv('twitter_dataset.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.dropna(subset='Tweet')
df['Month'] = df['Timestamp'].dt.to_period('M')

vectorizer = CountVectorizer(max_features=1000, stop_words="english")
X = vectorizer.fit_transform(df['Tweet'])
words = vectorizer.get_feature_names_out()

lda = LatentDirichletAllocation(random_state=42, n_components=3)
topics = lda.fit_transform(X)
df['Topics'] = topics.argmax(axis=1)

topic_keywords = []

for i, topic in enumerate(lda.components_):
    topic_word = [words[j] for j in np.argsort(topic)[-6:]]
    topic_keywords.append(' / '.join(topic_word))

monthly_topic = df.groupby(['Month', 'Topics']).size().unstack(fill_value=0)

monthly_topic.columns = topic_keywords

monthly_topic.plot(marker='o')
plt.title("Trending Topics over the time")
plt.legend(loc='upper left')
plt.xlabel("Months")
plt.ylabel("Number of Tweets")
plt.show()