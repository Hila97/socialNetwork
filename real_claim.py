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
# nx.draw(NH, node_color=color_map, with_labels=False)
# plt.show()

######## degree  histogram ###################33

# degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print("degree",degree_sequence)
# degreeCount = collections.Counter(degree_sequence)
# deg, cnt = zip(*degreeCount.items())
# fig, ax = plt.subplots()
# plt.bar(deg, cnt, width=0.80, color="b")
# plt.title("Degree Histogram")
# plt.ylabel("Count")
# plt.yscale('log')
# plt.xlabel("Degree")
# plt.xscale('log')
# plt.yscale('log')
# plt.show()

# התפלגות דרגות
# degree_sequence = sorted([d for n, d in NH.degree()], reverse=True)  # degree sequence
# print("degree", degree_sequence)
# degreeCount = collections.Counter(degree_sequence)
# deg, cnt = zip(*degreeCount.items())
# print("deg",deg)
# p = []
# for x in cnt:
#     p.append(x / len(nodes))
# print("cnt", cnt)
# print("probabily", p)
# fig, ax = plt.subplots()
# plt.bar(deg, p, width=1, color="b",edgecolor='black',)
# plt.title("Degree Histogram")
# plt.ylabel("probability")
# plt.xlabel("Degree")
# plt.xscale('log')
# plt.yscale('log')
# # plt.xlim([0, 4000])
# # plt.ylim([0, 1])
# plt.show()

# מדדי מרכזיות

# print("degree centrality", nx.degree_centrality(G))
# print(nx.in_degree_centrality(G))
# print(nx.out_degree_centrality(G))
# print("betweenness", nx.betweenness_centrality(G, k=100, normalized=True, weight=None, endpoints=False, seed=None))
# print("pagerank", nx.pagerank(G, alpha=0.8))
# print("closeness", nx.closeness_centrality(G))

# degree_centrality=nx.degree_centrality(G)
# a={k: v for k, v in sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True)}
# z=[]
# for i in a.values():
#     z.append(i)
#
# Count = collections.Counter(z)
# deg, cnt = zip(*Count.items())
# print("deg",deg)
# p = []
# for x in cnt:
#     p.append(x / len(nodes))
# # print("cnt", cnt)
# # print("probabily", p)
# fig, ax = plt.subplots()
# plt.bar(deg, cnt, width=1, color="b",edgecolor='black',)
# plt.title("Degree Histogram")
# plt.ylabel("cnt")
# plt.xlabel("Degree")
# plt.xlim([0,2])
# plt.show()



# plt.hist(deg, bins=np.logspace(np.log10(1), np.log10(1000), 100), density=True, edgecolor='black')
# plt.gca().set_xscale("log")
# plt.gca().set_yscale("log")
# plt.show()
# degree_centrality=nx.degree_centrality(G)
# node_sizes=[]
# for x in degree_centrality.values():
#     node_sizes.append(x*1000)
#
# in_degree=nx.in_degree_centrality(G)
# node_sizes=[]
# for x in in_degree.values():
#     node_sizes.append(x*1000)

# out_degree=nx.out_degree_centrality(G)
# node_sizes=[]
# for x in out_degree.values():
#     node_sizes.append(x*1000)

# betweenness=nx.betweenness_centrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None)
# node_sizes=[]
# for x in betweenness.values():
#     node_sizes.append(x*1000)

# page_rank= nx.pagerank(G, alpha=0.8)
# node_sizes=[]
# for x in page_rank.values():
#     node_sizes.append(x*1000)


# closeness=nx.closeness_centrality(G)
# node_sizes=[]
# for x in closeness.values():
#     node_sizes.append(x*1000)
#

# nx.draw(G, node_color=color_map,node_size=node_sizes, with_labels=False)
# plt.show()


#ניסוי יצירת גרף רק משתמשים 1
DG = nx.DiGraph()

only_users=[]
only_claims=[]
for node in NH:
    if node>1000 and node<1000000:
        only_claims.append(node)
    elif node >1000000:
        only_users.append(node)  # users

print(only_users)
print(only_claims)

DG.add_nodes_from(only_users)

for l in only_claims:
    claims_out = list(NH.successors(l))
    claims_in = list(NH.predecessors(l))
    #print("for ",l , claims_out,claims_in)
    for x in claims_in:
        for y in claims_out:
            DG.add_edge(x, y)

# nx.draw(DG, with_labels=False)
# plt.show()
print("nodes:",len(list(DG.nodes)), "edges:",len(list(DG.edges)))

# betweenness=nx.betweenness_centrality(DG, k=None, normalized=True, weight=None, endpoints=False, seed=None)
# print(betweenness)
# node_sizes=[]
# for x in betweenness.values():
#     node_sizes.append(x*1000)
# nx.draw(DG, node_color=color_map,node_size=node_sizes, with_labels=False)
# plt.show()
print(sorted([d for n, d in DG.out_degree()], reverse=True))
page_rank=nx.pagerank(DG, alpha=0.8)
a=dict(sorted(page_rank.items(), reverse=True, key=lambda item: item[1]))
print("page rank",a)

# closeness=nx.closeness_centrality(DG)
# a=dict(sorted(closeness.items(), reverse=True, key=lambda item: item[1]))
# print("closeness",a)
# key=list(a.keys())
# value=list(a.values())
# fig, ax = plt.subplots()
# # ax.fmt_ydata = millions
# plt.plot(key, value, 'o')
# plt.show()

#configuration
degrees = []
degree_list = DG.degree(original_nodes)
for d in degree_list:
    degrees.append(d[1])
print(degrees)
CM = nx.configuration_model(degrees, create_using=None, seed=None)
# nx.draw(CM, with_labels=False)
# plt.show()
print("nodes:",len(list(CM.nodes)))
print("edges:",len(list(CM.edges)))

#erdos
ERG = nx.erdos_renyi_graph(len(list(DG.nodes)), 0.0385, seed=None, directed=False)
# nx.draw(ERG, with_labels=False)
# plt.show()
print("nodes:",len(list(ERG.nodes)))
print("edges:",len(list(ERG.edges)))

clustering=nx.clustering(DG, nodes=None, weight=None)
a=dict(sorted(clustering.items(), reverse=True, key=lambda item: item[1]))
print("clustering",a)

print(nx.transitivity(DG))