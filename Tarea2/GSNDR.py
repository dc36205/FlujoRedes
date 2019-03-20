# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:41:30 2019

@author: Daniel Chong
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph() 
G.add_node( "a", size=10 ,pos=(1,60))  
G.add_node( "b" , size=10 , pos=(40,80))  
G.add_node( "c", size=10 , pos=(80,20)) 
G.add_node( "d", size=10, pos=(80,-50)) 
G.add_node( "e", size=10 ,pos=(10,20))  
G.add_node( "f", size=10 ,pos=(40,1))  
G.add_node( "g", size=10 ,pos=(30,-50))
G.add_edge('a', 'b',  color='red',weight=8)
G.add_edge('b', 'c',  color='red',weight=8)
G.add_edge('c', 'd',  color='red',weight=8)
G.add_edge('e', 'a',  color='red',weight=8)
G.add_edge('b', 'f',  color='black',weight=3)
G.add_edge('f', 'g',  color='black',weight=3)
G.add_edge('g', 'e',  color='black',weight=3)
pos=nx.spring_layout(G, k=10, iterations=100, dim=2,weight='weight',scale=0.5 )
labels = {('a','e'):'15', ('b','f'):'70',('d','c'):'10'}
size = [700, 700, 700, 700, 700, 700, 700] 
color=["#A0CBE2", "#FF0000", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2"]              
nx.draw(G,pos, with_labels=True, edge_color='black', node_size=size, node_color=color, font_size=20, width=3, node_shape='s')
nx.draw_networkx_nodes(G, pos, node_size=size, node_color=color)
nx.draw_networkx_edges(G, pos, width=6, edge_color='blue')
nx.draw_networkx_edge_labels(G,pos, labels, font_size=10, font_color='red',font_family='sans-serif')
plt.axis('off')
plt.savefig("GNDirigidoReflexivo.eps") 
plt.show()