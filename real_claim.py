import networkx as nx
import matplotlib.pyplot as plt
import community
import collections
import numpy as np
import scipy as sp
from collections import Counter
from operator import itemgetter
import scipy.special

# יבוא דאטא ראשוני
Data = open('ClaimRealCOVID-19_tweets_replies_5.csv', "r")
next(Data, None)  # skip the first line in the input file
Graphtype = nx.DiGraph()
G = nx.parse_edgelist(Data, delimiter=',', create_using=Graphtype, nodetype=int, data=(('weight', float),))
original_nodes = list(G.nodes)
original_edges = list(G.edges)
print("number of nodes ", len(original_nodes))
print("number of edges ", len(original_edges))
print("original_nodes", original_nodes)
print("original_edges", original_edges)

# ציור גרף מקורי
color_map = []
for node in G:
    if node < 1000:
        color_map.append('blue')  # news
    elif node < 1000000:
        color_map.append('red')  # articles
    else:
        color_map.append('green')  # users
# nx.draw(G, node_color=color_map, with_labels=False)
# pos = nx.spring_layout(G)

# רכיבי קשירות
print("num of strongly cc ", nx.number_strongly_connected_components(G))
print("num of weakly cc ", nx.number_weakly_connected_components(G))
# print("all the components")
b = sorted(nx.weakly_connected_components(G), key=len, reverse=True)
print("b", len(b))

# ציור רכיב הקשירות הגדול ביותר
largest = len(b[0])
print("largest connected components ", largest)
NH = G.subgraph(b[0])
nodes=list(NH.nodes)
edges=list(NH.edges)
print("largest connected components nodes",len(nodes))
print("largest connected components edges",len(edges))
color_map = []
for node in NH:
    if node < 1000:
        color_map.append('blue')  # news
    elif node < 1000000:
        color_map.append('red')  # articles
    else:
        color_map.append('green')  # users
nx.draw(NH, node_color=color_map, with_labels=False)
plt.show()

