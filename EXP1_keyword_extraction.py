import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

df = pd.read_csv('twitter_dataset.csv')
print(df)

tweet = df['Tweet']
print("\n", tweet)

#keyword extraction
vectorizer = CountVectorizer(stop_words='english', max_features=20)
X = vectorizer.fit_transform(tweet)
words = vectorizer.get_feature_names_out()
print("\nKeywords Extracted:", words)

#LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components=3, random_state=42)
lda.fit(X)

print("\nTopic Modeling:")
for i, topic in enumerate(lda.components_):
    print(f"Topic {i+1}:", [words[j] for j in np.argsort(topic)[-6:]])
