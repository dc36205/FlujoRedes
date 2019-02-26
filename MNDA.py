# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:37:56 2019

@author: Daniel Chong
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiGraph() 
G.add_node( "a", size=60 ,  pos=(1,60))  
G.add_node( "b" , size=60 , pos=(40,80))  
G.add_node( "c", size=60, pos=(80,20)) 
G.add_node( "d", size=60,  pos=(80,-50)) 
G.add_node( "e", size=60,  pos=(10,20))  
G.add_node( "f", size=60, pos=(40,1))  
G.add_node( "g", size=60, pos=(30,-50)) 
G.add_edge('a', 'b',  color='red',weight=8)
G.add_edge('a', 'b',  color='black',weight=3)
G.add_edge('b', 'c',  color='red',weight=8)
G.add_edge('b', 'c',  color='black',weight=3)
G.add_edge('c', 'd',  color='red',weight=8)
G.add_edge('c', 'd',  color='black',weight=3)
G.add_edge('e', 'a',  color='red',weight=8)
G.add_edge('e', 'a',  color='black',weight=3)
G.add_edge('b', 'f',  color='black',weight=3)
G.add_edge('f', 'g',  color='black',weight=3)

pos=nx.spectral_layout(G)
size = [700, 700, 700, 700, 700, 700] 
color=["#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2"]
nx.draw(G,pos, with_labels=True, edge_color='black', node_size=size, node_color=color, font_size=20, width=8)
nx.draw_networkx_edges(G, pos,  edge_color='green', label="S", arrowstyle='-|>', arrows=True, width=3)  
plt.axis('off')
plt.savefig("MNDAciclicoTipoLayout.eps") 
plt.show()