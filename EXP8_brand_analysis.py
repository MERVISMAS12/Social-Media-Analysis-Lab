import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('twitter_dataset.csv')

brand_count = df['Brand'].value_counts().head(10)
sns.barplot(x=brand_count.values, y=brand_count.index)
plt.title('Top 10 Brand Mentions')
plt.xlabel('Count')
plt.ylabel('Brand')
plt.show()

brand_like_retweet = df.groupby('Brand')[['Like_count', 'Retweet_count']].mean().loc[brand_count.index]

sns.lineplot(x=brand_like_retweet['Like_count'], y=brand_count.index, color='green', markers='o')
plt.title('Average Like Count per Brand')
plt.xlabel('Average Likes')
plt.ylabel('Brand')
plt.show()

sns.lineplot(x=brand_like_retweet['Retweet_count'], y=brand_count.index, color='blue', markers='o')
plt.title('Average Retweet Count per Brand')
plt.xlabel('Average Retweet')
plt.ylabel('Brand')
plt.show()