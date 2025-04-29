import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv('twitter_dataset.csv')
print(df.describe(include='all'))

sentiment_count = df['Sentiment'].value_counts()
plt.pie(labels=sentiment_count.index, x=sentiment_count.values)
plt.title('Distribution of Sentiments')
plt.show()

#Top 10 locations
location_count = df['Location'].value_counts().head()
sns.barplot(x=location_count.index, y=location_count.values)
plt.xlabel('Location')
plt.ylabel('Count')
plt.show()

#Top 10 most common used Hastags
hastags = df['Hashtags'].str.split(",").sum()
counter = Counter(hastags)
common = counter.most_common(10)
label, value = zip(*common)
sns.barplot(x=label, y=value)
plt.title('Top most common Hastags')
plt.show()

