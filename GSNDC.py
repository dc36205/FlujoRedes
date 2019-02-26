# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:38:17 2019

@author: Daniel Chong
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph() 
G.add_edge('A', 'B', weight=0.6)
G.add_edge('B', 'C', weight=0.7)
G.add_edge('C', 'D', weight=0.7)
G.add_edge('D', 'E', weight=0.7)
G.add_edge('E', 'F', weight=0.9)
G.add_edge('F', 'A', weight=0.7)
size = [700, 700, 700, 700, 700, 700] 
color=[ "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2" , "#A0CBE2" ,"#A0CBE2" ]
initialpos = {'a':(0,0), 'b':(0,3), 'c':(0,-1), 'd':(5,2), 'e':(3,1), 'f':(4,4)}
pos = nx.circular_layout(G, scale=0.5, dim=2)  
nx.draw_networkx_nodes(G, pos, node_size=size, node_color=color)
nx.draw_networkx_edges(G, pos, width=6)
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.savefig("GraSNoDiCiclicoTipoLayout.eps") 
plt.show()