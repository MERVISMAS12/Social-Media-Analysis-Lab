import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

df = pd.read_csv('twitter_dataset.csv')
hastags = df['Hashtags'].dropna().str.split(',').sum()
counter = Counter(hastags)
common = counter.most_common(10)
label, count = zip(*common)
plt.barh(label, count)
plt.title('Top Most Common Hastags')
plt.show()