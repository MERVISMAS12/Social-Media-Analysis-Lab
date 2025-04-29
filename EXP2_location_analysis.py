import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('twitter_dataset.csv')

#Top 10 Locations
loc_counts = df['Location'].value_counts().head(10)
sns.barplot(x=loc_counts.values, y=loc_counts.index)
plt.title("Top 10 Locations")
plt.show()

#Top Brands in Mumbai
mumbai_counts = df[df['Location']=='Mumbai, India']['Brand'].value_counts()
sns.barplot(x=mumbai_counts.values, y=mumbai_counts.index)
plt.title("Top Brands in Mumbai")
plt.show()

#Top 10 Locations with Negative Sentiments
neg_counts = df[df['Sentiment']=='negative']['Location'].value_counts().head(10)
sns.barplot(x=neg_counts.values, y=neg_counts.index)
plt.title("Top 10 Locations with Negative Sentiments")
plt.show()

#Top 10 Locations with Neutral Sentiments
neu_counts = df[df['Sentiment']=='neutral']['Location'].value_counts().head(10)
sns.barplot(x=neu_counts.values, y=neu_counts.index)
plt.title("Top 10 Locations with Neutral Sentiments")
plt.show()

#Top 10 Locations with Positive Sentiments
pos_counts = df[df['Sentiment']=='positive']['Location'].value_counts().head(10)
sns.barplot(x=pos_counts.values, y=pos_counts.index)
plt.title("Top 10 Locations with Positive Sentiments")
plt.show()
