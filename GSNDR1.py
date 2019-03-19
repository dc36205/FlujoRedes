# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:41:30 2019

@author: Daniel Chong
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as m
import statistics as stats
data = pd.read_csv("VaLLoress.csv")
color_names = ["black", "green", "red", "blue", "yellow"]
#calculo = np.diff(data["media"]) / data["media"][:-1]
betweenness_centrality = data[(data["Alg1"] == "betweenness_centrality")]
minimun_spanning_tree= data[(data["Alg1"] == "minimum_spanning_tree")]
greedy_color = data[(data["Alg1"] == "greedy_color")]
max_clique = data[(data["Alg1"] == "max_clique")]
maximal_matching = data[(data["Alg1"] == "maximal_matching")]
size = (5 * data["arcos"][:5] / data["nodos"][:5])
figure, axis = plt.subplots(figsize=(10, 10))
axis.scatter(betweenness_centrality["media"], betweenness_centrality["arcos"],
            s=size, c=color_names, marker="+",
            label="Algoritmo Betweenness centrality", alpha=0.8, edgecolors='none')
axis.scatter(minimun_spanning_tree["media"], minimun_spanning_tree["arcos"],
            s=size, c=color_names, marker="*",
            label="Algoritmo Minimun Spanning Tree", alpha=0.8, edgecolors='none')
axis.scatter(greedy_color["media"], greedy_color["arcos"],
            s=size, c=color_names, marker="D",
            label="Algoritmo Greedy color", alpha=0.8, edgecolors='none')
axis.scatter(max_clique["media"], max_clique["arcos"],
            s=size, c=color_names, marker="o",
            label="Algoritmo Max Clique", alpha=0.8, edgecolors='none')
axis.scatter(maximal_matching ["media"], maximal_matching ["arcos"],
            s=size, c=color_names, marker="o",
            label="Algoritmo maximal_matching ", alpha=1, edgecolors='none')
axis.set_ylabel("Cantidad de arcos del grafo", fontsize=10)
axis.set_xlabel("Tiempo de ejecucion", fontsize=10)
plt.ylim((min(greedy_color["arcos"])-5, max(greedy_color["arcos"]) + 5))
plt.legend(loc="center right")
plt.axis('on')
plt.savefig("SPlOOTTTT.eps")
plt.show()
