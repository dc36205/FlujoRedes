# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 18:43:10 2019

@author: Daniel Chong
"""

import networkx as nx 
import matplotlib.pyplot as plt

G = nx.DiGraph() 
G.add_nodes_from([1,2,3,4], bipartite=0)
G.add_nodes_from(['a','b', 'c', 'd' ], bipartite=1)
G.add_edges_from([(1,'a'), (1,'b'), (2,'b'), (2,'c'), (3,'c'),  (4,'a'),(4,'d') ])
l, r = nx.bipartite.sets(G)
pos = {}
pos.update((node, (1, index)) for index, node in enumerate(l))
pos.update((node, (2, index)) for index, node in enumerate(r))
labels = {(1,'a'):'2', (2,'b'):'7'}
color=["#2da05f", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2"]
nx.draw(G, pos=pos, with_labels = True, scale=1, align='vertical',center=None,edge_color='black',node_color=color,font_size=20, width=2)
nx.draw_networkx_edge_labels(G,pos, labels, font_size=10, font_color='red')   
nx.draw_networkx_nodes(G, pos, node_size=700,  node_color=color, with_labels=True)
nx.draw_networkx_edges( G, pos,width=6, edge_color='blue')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.savefig("Prueba_Layout_2.eps") 
plt.show()