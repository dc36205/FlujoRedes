# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 23:10:18 2019

@author: Daniel Chong
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.MultiDiGraph() 

G.add_node( "a", size=10 ,  pos=(1,60))  
G.add_node( "b" , size=10 , pos=(40,80))  
G.add_node( "c", size=10, pos=(80,20)) 
G.add_node( "d", size=10,  pos=(80,-50)) 
G.add_node( "e", size=10,  pos=(10,20))  
G.add_node( "f", size=10, pos=(40,1))  
G.add_node( "g", size=10, pos=(30,-50))
G.add_node( "h", size=10, pos=(50,30))
G.add_node( "i", size=10, pos=(30,30))
G.add_node( "i", size=10, pos=(30,30))

G.add_edge('a', 'b',  color='red',weight=8)
G.add_edge('a', 'b',  color='black',weight=3)
G.add_edge('b', 'c',  color='red',weight=8)
G.add_edge('b', 'c',  color='black',weight=3)
G.add_edge('c', 'd',  color='red',weight=8)
G.add_edge('c', 'd',  color='black',weight=3)
G.add_edge('b', 'f',  color='black',weight=3)
G.add_edge('f', 'g',  color='black',weight=4)
G.add_edge('g', 'e',  color='black',weight=3)
G.add_edge('f', 'h',  color='black',weight=5)
G.add_edge('f', 'i',  color='black',weight=3)
pos=nx.circular_layout(G)
size = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000] 
color=["#A0CBE2", "#A0CBE2", "#A0CBE2", "#FF0000", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2"]

nx.draw(G,pos, with_labels=True, edge_color='black', node_size=size, node_color=color, font_size=20, width=8)
nx.draw_networkx_edges(G, pos,  edge_color='green', label="S", arrowstyle='-|>', arrows=True, width=3)

plt.axis('off')
plt.savefig("MDirigidoRefexivo.eps") 
plt.show()