import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community import girvan_newman

df = pd.read_csv('twitter_dataset.csv').head(50)
G = nx.Graph()

for brand in df['Brand'].dropna().unique():
    users = df[df['Brand'] == brand]['Username'].dropna().unique()
    for i in range(len(users)):
        for j in range(i+1, len(users)):
            G.add_edge(users[i], users[j], brand= brand)

comp = next(girvan_newman(G))
i=1
for comm in comp:
    print(f"Commmunity {i}: {comm}")
    i+=1

nx.draw(G, node_size = 10, font_size=9)
plt.title("User Graph Based on Common Brand Mentions ")
plt.show()
