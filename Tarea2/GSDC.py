# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:48:00 2019

@author: Daniel Chong
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph() 

G.add_node( "a", size=10 )
G.add_node( "b" , size=10 ) 
G.add_node( "c", size=10 )
G.add_node( "d", size=10 ) 
G.add_node( "e", size=10 )
G.add_node( "f", size=10 )
G.add_node( "g", size=10 )
G.add_node( "h", size=10 )
G.add_node( "i", size=10 )
G.add_edge('a', 'b',  color='red',weight=8)
G.add_edge('b', 'c',  color='red',weight=8)
G.add_edge('c', 'd',  color='red',weight=8)
G.add_edge('d', 'e',  color='black',weight=3)
G.add_edge('e', 'f',  color='black',weight=3)
G.add_edge('f', 'g',  color='black',weight=3)
G.add_edge('g', 'h',  color='black',weight=3)
G.add_edge('h', 'i',  color='black',weight=3)
G.add_edge('i', 'a',  color='black',weight=3)
pos = nx.shell_layout(pos)
labels = {('a', 'b' ):'20', ('b','c'):'70',('c','d'):'10'}
color=["#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2", "#A0CBE2"]
nx.draw(G, pos=pos, with_labels = True, scale=1, align='horizontal',center=None,edge_color='black',node_color=color,font_size=20, width=2)
nx.draw_networkx_edge_labels(G,pos, labels, font_size=10, font_color='red')       
nx.draw_networkx_nodes( G, pos, node_size=400, node_color=color)
nx.draw_networkx_edges( G, pos,width=3, edge_color='blue')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.savefig("GDirigidoCiclicoLayout.eps") 
plt.show()