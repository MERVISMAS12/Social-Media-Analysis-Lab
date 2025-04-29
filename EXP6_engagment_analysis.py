import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv('twitter_dataset.csv')

df['Sentiment'] = df['Sentiment'].str.lower()
df['Engagement'] = df['Like_count'] + df['Retweet_count']
df['text_length'] = df['Tweet'].str.len()

engagement_length = df.groupby(pd.cut(df['text_length'], bins=5), observed=False)['Engagement'].mean()
sns.barplot(x=engagement_length.values, y=engagement_length.index)
plt.title('Enagement of Tweet by Length')
plt.xlabel('Engagement')
plt.ylabel('Length')
plt.show()

top_user = df.groupby('Username')['Engagement'].sum().nlargest(10).reset_index()
sns.barplot(x='Username', y='Engagement', data=top_user)
plt.title('Top 10 Users with Highest Engagemwnt')
plt.xlabel('Username')
plt.ylabel('Engagement')
plt.show()

top_tweet = df.nlargest(10, 'Engagement')[['Username', 'Tweet', 'Engagement']].reset_index()
print(f"Top 10 most Engaging Tweet \n {top_tweet}")