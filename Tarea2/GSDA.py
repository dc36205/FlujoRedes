# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:45:42 2019

@author: Daniel Chong
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph() 
G.add_edge('I', 'a', weight=0.6)
G.add_edge('a', 'b', weight=0.6)
G.add_edge('b', 'c', weight=0.6)
G.add_edge('c', 'd', weight=0.6)
G.add_edge('d', 'e', weight=0.7)
G.add_edge('e', 'F', weight=0.7)
pos = nx.kamada_kawai_layout(G, weight='weight', scale=1, center=None,dim=2)
labels = {('I', 'a' ):'20', ('b','c'):'70',('c','d'):'10'}
size = [700, 700, 700, 700, 700, 700,700] 
color=[ "#2da05f" , "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2" ]
nx.draw(G, pos=pos, with_labels = True, scale=1, align='vertical',center=None,edge_color='black',node_color=color,font_size=20, width=2)
nx.draw_networkx_edge_labels(G,pos, labels, font_size=10, font_color='red')       
nx.draw_networkx_nodes( G, pos, node_size=700, node_color=color)
nx.draw_networkx_edges( G, pos,width=6, edge_color='blue')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.savefig("GrafoSimpleDAcicNew.eps") 
plt.show()