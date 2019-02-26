# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:35:36 2019

@author: Daniel Chong
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph() 

G.add_edge('a', 'b',  weight=0.2)
G.add_edge('b',   'c',  weight=0.7)  
G.add_edge('c',   'd',weight=0.7)
G.add_edge('d', 'e',weight=0.7)
G.add_edge('e', 'f',weight=0.9)
G.add_edge('f', 'g', weight=0.7)
G.add_edge('g',  'h',   weight=0.7)
G.add_edge('h',   'i',  weight=0.7)

initialpos = {'a':(0,0), 'b':(0,3), 'c':(0,-1), 'd':(2,5), 'e':(5,5), 'f':(4,4), 'g':(4,9), 'h':(6,1),'i':(7,2),  }
pos = nx.spring_layout(G, k=10, pos = initialpos, fixed=None,  iterations=100,dim=2, weight='weight',scale=0.5)  

#pos = nx.spring_layout(G)  
size = [700, 700, 700, 700, 700, 700,700,700,700] 
color=[ "#2da05f" , "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#2da05f" ]

nx.draw_networkx_nodes(G, pos, node_color=color,node_size=size,)#node_size=700,s
nx.draw_networkx_edges(G, pos, width=6)
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.savefig("GSNDA Layout1.eps") 
plt.show()