# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 18:00:35 2019

@author: Daniel Chong
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.MultiGraph() 

G.add_node( "a", size=60 ,  pos=(1,60))  
G.add_node( "b" , size=60 , pos=(10,80))  
G.add_node( "c", size=60, pos=(80,20)) 
G.add_node( "d", size=60,  pos=(80,-50)) 
G.add_node( "e", size=60,  pos=(10,20))  
G.add_node( "f", size=60, pos=(40,1))  
G.add_node( "g", size=60, pos=(30,-50))
G.add_edge('a', 'e',  color='red',weight=8)
G.add_edge('b', 'e',  color='red',weight=8)
G.add_edge('c', 'f',  color='red',weight=8)
G.add_edge('d', 'a',  color='red',weight=8)
G.add_edge('e', 'g',  color='red',weight=8)
G.add_edge('a', 'b',  color='red',weight=8)
G.add_edge('c', 'd',  color='red',weight=8)
G.add_edge('g', 'd',  color='red',weight=8)
G.add_edge('g', 'c',  color='red',weight=8)
G.add_edge('b', 'f',  color='red',weight=8)
pos = nx.circular_layout(G, scale=0.5, dim=2)
size = [1000, 1000, 1000, 1000, 1000, 1000, 1000] 
color=["#FF0000", "#A0CBE2", "#A0CBE2", "#FF0000", "#FF0000", "#A0CBE2", "#FF0000"]
nx.draw(G, pos, with_labels=True, edge_color='black', node_size=size, node_color=color, font_size=20, width=8)
nx.draw_networkx_edges(G, pos,  edge_color='green', label="S", arrowstyle='-|>', arrows=True, width=3)  
nx.draw_networkx_nodes( G, pos, node_size=400, node_color=color)
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.savefig("MNDirigidoREflexivo.eps") 
plt.show()