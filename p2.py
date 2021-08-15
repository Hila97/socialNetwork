import networkx as nx
import matplotlib.pyplot as plt
import community
import collections
import numpy as np
import scipy as sp

# יבוא דאטא ראשוני
Data = open('fake.csv', "r")
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
# plt.show()
#
# # רכיבי קשירות
print("num of strongly cc ", nx.number_strongly_connected_components(G))
print("num of weakly cc ", nx.number_weakly_connected_components(G))
# print("all the components")
b = sorted(nx.weakly_connected_components(G), key=len, reverse=True)
# print("b", b)
# a=[list(cc) for cc in nx.strongly_connected_components(G)]
# print("connected com", a)
#
largest = len(b[0])
print("largest connected components ", largest)

# max=0
# adam=0
# for n in original_nodes:
#     degree=G.degree(n)
#     if(degree>max):
#         max=degree
#         adam=n
# print("max",max)
# print("adam",adam)
# NH=nx.DiGraph()
# succ=list(G.successors(adam))
# pre= list(G.predecessors(adam))
# allNodes=succ+pre+[adam]
# #print("allNodes",allNodes)

# ציור רכיב הקשירות הגדול ביותר
NH = G.subgraph(b[0])
nodes=list(NH.nodes)
edges=list(NH.edges)
print("largest connected components nodes",nodes)
print("largest connected components edges",edges)
color_map = []
for node in NH:
    if node < 1000:
        color_map.append('blue')  # news
    elif node < 1000000:
        color_map.append('red')  # articles
    else:
        color_map.append('green')  # users
# nx.draw(NH, node_color=color_map, with_labels=False)
# plt.show()

# # דרגות בגרף
# # degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
# # degree sequence
# # print("degree",degree_sequence)
# # degreeCount = collections.Counter(degree_sequence)
# # s=dict(sorted(degreeCount.items(), key=lambda item: item[0]))
# # print(s)
# ######## degree  histogram ###################33
# #
# # degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# # degreeCount = collections.Counter(degree_sequence)
# # deg, cnt = zip(*degreeCount.items())
# #
# # fig, ax = plt.subplots()
# # plt.bar(deg, cnt, width=0.80, color="b")
# #
# # plt.title("Degree Histogram")
# # plt.ylabel("Count")
# # plt.xlabel("Degree")
# # ax.set_xticks([d + 0.4 for d in deg])
# # ax.set_xticklabels(deg)
# #
# # # draw graph in inset
# # plt.axes([0.4, 0.4, 0.5, 0.5])
# # Gcc = G.subgraph(sorted(nx.strongly_connected_components(G), key=len, reverse=True)[0])
# # pos = nx.spring_layout(G)
# # plt.axis("off")
# # # nx.draw_networkx_nodes(G, pos, node_size=20)
# # # nx.draw_networkx_edges(G, pos, alpha=0.4)
# # plt.show()
#
# # מדדי מרכזיות

print("degree centrality", nx.degree_centrality(G))
print(nx.in_degree_centrality(G))
print(nx.out_degree_centrality(G))
print("betweenness", nx.betweenness_centrality(G, k=100, normalized=True, weight=None, endpoints=False, seed=None))
print("pagerank", nx.pagerank(G, alpha=0.8))
print("closeness", nx.closeness_centrality(G))

degree_centrality=nx.degree_centrality(G)
node_sizes=[]
for x in degree_centrality.values():
    node_sizes.append(x*1000)


# betweenness=nx.betweenness_centrality(NH, k=None, normalized=True, weight=None, endpoints=False, seed=None)
# node_sizes=[]
# for x in betweenness.values():
#     node_sizes.append(x*1000)

# page_rank= nx.pagerank(NH, alpha=0.8)
# node_sizes=[]
# for x in page_rank.values():
#     node_sizes.append(x*1000)


# closeness=nx.closeness_centrality(NH)
# node_sizes=[]
# for x in closeness.values():
#     node_sizes.append(x*1000)
#

nx.draw(G, node_color=color_map,node_size=node_sizes, with_labels=False)
plt.show()