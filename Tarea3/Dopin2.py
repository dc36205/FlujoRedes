# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:00:45 2019

@author: Daniel Chong
"""

#Libraries
import networkx as nx
import random as rnd
import datetime
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
#---------------------------------------------Deficiones Generales---------------------------------
tiempos = []
# -------------------------------------------Creando los grafos ----------------------------------

##Primero funcion para crear una lista con las 25 combinaciones  

def Generator(num, nameGraf): 
    G1 = nx.Graph()
    #for p in range(num):
    nodes = []
    edges = []
    for i in range(num):  # Creacion aleatoria de Grafo con 80 nodos
            nodes.append(i)                 
    for i in nodes:
         idx = nodes.index(i) + 1
         for j in nodes[idx:len(nodes)]:
             edg = rnd.randint(1,4) #Para crear un arco o no entre un par de vertices 
             if edg:
                 G1.add_edge(i,j, distance=rnd.randint(1,10) ) # Adicionar peso a los arcos del grafo aleatoria
                 G1.add_edge(j, i, distance=rnd.randint(1,10) ) 
        
    df = pd.DataFrame()
    df = nx.to_pandas_adjacency(G1, dtype=int, weight="distance")
    
    df.to_csv(nameGraf, index=None, header=None)

for i in range(1):
    A=Generator(rnd.randint(100,150),"grafos"+str(i)+".csv")# Se crean 5 grafos guardados en archivos csv
    
#--------------------- Grafo 1---------------------------------------------------------
def betweenness_centrality(nombre):
    df = pd.DataFrame()
    df = pd.read_csv(nombre, header=None) 
    a = nx.from_pandas_adjacency(df, create_using=nx.Graph())
    
    for i in range(30): # Numero de corridas
        inicio = datetime.datetime.now()
        for key in range(50):
            nx.betweenness_centrality(a)
        final = datetime.datetime.now()
        tiempos.append((final - inicio).total_seconds())
       
    media=np.mean(tiempos)
    desv=np.std(tiempos)
    mediana=np.median(tiempos)
    nodos=nx.number_of_nodes(a) 
    arcos=nx.number_of_edges(a) 
    salvar=[]
    salvar.append(media)
    salvar.append(desv)
    salvar.append(mediana)
    salvar.append(nodos)
    salvar.append(arcos)

    return salvar
#---------------------- Grafo 2------------------------------------------------------------
def minimum_spanning_tree(nombre):#Para grafo dirigido y no dirigido     
    df = pd.read_csv(nombre, header=None) 
    b = nx.from_pandas_adjacency(df, create_using=nx.Graph())
    
    for i in range(30): # Ejecutar las 50 corridas 
        inicio = datetime.datetime.now()       
        for key in range(50):
            nx.minimum_spanning_tree(b)       
        final = datetime.datetime.now()
        tiempos.append((final - inicio).total_seconds()) # Guardo los tiempos de las corridas     
    
    media=np.mean(tiempos)
    desv=np.std(tiempos)
    mediana=np.median(tiempos)
    nodos=nx.number_of_nodes(b) 
    arcos=nx.number_of_edges(b) 
    salvar=[]
    salvar.append(media)
    salvar.append(desv)
    salvar.append(mediana)
    salvar.append(nodos)
    salvar.append(arcos)

    return salvar
#----------------------Grafo 3---------------------------------------------------------
def greedy_color(nombre): # Para grafo Simpe No dirigido Aciclico
    df = pd.read_csv(nombre, header=None) 
    b = nx.from_pandas_adjacency(df, create_using=nx.Graph())
    
    for i in range(30): # Ejecutar las 50 corridas 
        inicio = datetime.datetime.now()
        for key in range(50):
            nx.greedy_color(b) #, source=0, target=3)
        final = datetime.datetime.now()
        tiempos.append((final - inicio).total_seconds()) # Guardo los tiempos de las corridas 
        
    media=np.mean(tiempos)
    desv=np.std(tiempos)
    mediana=np.median(tiempos)
    nodos=nx.number_of_nodes(b) 
    arcos=nx.number_of_edges(b) 
    salvar=[]
    salvar.append(media)
    salvar.append(desv)
    salvar.append(mediana)
    salvar.append(nodos)
    salvar.append(arcos)
# 
    return salvar

#---------------------Grafo 4------------------------------------------------------------------------------
def max_clique(nombre):# Para Grafo Simple No dirigido
    df = pd.read_csv(nombre, header=None) 
    b = nx.from_pandas_adjacency(df, create_using=nx.Graph())

    for i in range(30): # Ejecutar las 50 corridas 
        inicio = datetime.datetime.now()
        for key in range(50):
            nx.make_max_clique_graph(b, create_using=None)        
        final = datetime.datetime.now()
        tiempos.append((final - inicio).total_seconds()) # Guardo los tiempos de las corridas 

    media=np.mean(tiempos)
    desv=np.std(tiempos)
    mediana=np.median(tiempos)
    nodos=nx.number_of_nodes(b) 
    arcos=nx.number_of_edges(b) 
    salvar=[]
    salvar.append(media)
    salvar.append(desv)
    salvar.append(mediana)
    salvar.append(nodos)
    salvar.append(arcos)

    return salvar
#----------------------Grafo 5---------------------------------------------------------------------
def maximal_matching(nombre):#Para Grafo Simple Aciclico No dirigido
    df = pd.read_csv(nombre, header=None) 
    b = nx.from_pandas_adjacency(df, create_using=nx.Graph())

    for i in range(30):
        inicio = datetime.datetime.now()
        for key in range(50): # Ejecutar las 50 corridas         
            nx.maximal_matching(b)
        final = datetime.datetime.now()
        tiempos.append((final - inicio).total_seconds()) # Guardo los tiempos de las corridas 
        
    media=np.mean(tiempos)
    desv=np.std(tiempos)
    mediana=np.median(tiempos)
    nodos=nx.number_of_nodes(b) 
    arcos=nx.number_of_edges(b) 
    salvar=[]
    salvar.append(media)
    salvar.append(desv)
    salvar.append(mediana)
    salvar.append(nodos)
    salvar.append(arcos)

    return salvar

#-------------------------------------Funcion Guarda todos los valores en un csv--------------------------------------------
def guardarDatosenCSV(nombre):
    
    valores={'Alg1':[],             # Estas son las columnas de la tabla del fichero CSV
             'grafo':[],
             'media':[],
             'arcos':[],
             'nodos':[],         
             }   
    for j in range(5):
          valores["Alg1"].append( "betweenness_centrality")
          valores["grafo"].append( (nombre+str(j) ))
          valores["media"].append( (betweenness_centrality(nombre+str(j)+".csv"  )) [0] )
          valores["arcos"].append( (betweenness_centrality(nombre+str(j)+".csv"  )) [4] )
          valores["nodos"].append( (betweenness_centrality(nombre+str(j)+".csv"  )) [3] )
          print(betweenness_centrality(nombre+str(j)+".csv")[0] , end="\n")
    for j in range(5):
        valores["Alg1"].append( "minimum_spanning_tree")
        valores["grafo"].append( (nombre+str(j) ))
        valores["media"].append( (minimum_spanning_tree(nombre+str(j)+".csv"  )) [0] )
        valores["arcos"].append( (minimum_spanning_tree(nombre+str(j)+".csv"  )) [4] )
        valores["nodos"].append(minimum_spanning_tree(nombre+str(j)+".csv")[3])    
    for j in range(5):
        valores["Alg1"].append( "greedy_color")
        valores["grafo"].append( (nombre+str(j) ))
        valores["media"].append( (greedy_color(nombre+str(j)+".csv"  )) [0] )
        valores["arcos"].append( (greedy_color(nombre+str(j)+".csv"  )) [4] )
        valores["nodos"].append(greedy_color(nombre+str(j)+".csv")[3])    
    for j in range(5):
        valores["Alg1"].append( "max_clique")
        valores["grafo"].append( (nombre+str(j))  )
        valores["media"].append( (max_clique(nombre+str(j)+".csv"  )) [0] )
        valores["arcos"].append( (max_clique(nombre+str(j)+".csv"  )) [4] )
        valores["nodos"].append(max_clique(nombre+str(j)+".csv")[3])    
    for j in range(5):
        valores["Alg1"].append( "maximal_matching")
        valores["grafo"].append( (nombre+str(j) ))
        valores["media"].append( (maximal_matching(nombre+str(j)+".csv"  )) [0] )
        valores["arcos"].append( (maximal_matching(nombre+str(j)+".csv"  )) [4] )
        valores["nodos"].append(maximal_matching(nombre+str(j)+".csv")[3])    
        print(nombre, end="\n")
    df = pd.DataFrame(valores) 
    df.to_csv("valoresNuevos.csv", index=None)     # Grafos de 150, 300, 600, 800, y 1000 nodos
    
#----------------------------------Para Graficar los Histogramas----------------------------------------------------
#def MakeHistograma(adress):
#    
#data = pd.read_csv("Valores.csv")
#plt.figure(figsize=(8, 12))
#
#plt.subplot(321) #facecolor='blue',
#x = plt.hist(data["media"][:5], 5,  alpha=0.5, color='#0504aa', rwidth=0.85, normed=True, histtype='stepfilled',edgecolor='none',linewidth=1 )
#
#plt.title('Algoritmo 1', size= 12)
#plt.xlabel('Tiempo Ejecución ', size= 12)
#plt.ylabel('Probabilidad de Ocurrencia', size= 12)
#
#plt.subplot(322)# facecolor='red'
#x = plt.hist(data["media"][5:10], 5, color='#607c8e', alpha=0.5, rwidth=0.85, linewidth=1)
#
#plt.title('Algoritmo 2', size= 12)
#plt.xlabel('Tiempo Ejecución ',size= 12)
#plt.ylabel('Probabilidad de Ocurrencia', size= 12)
#
#plt.subplot(323)#facecolor='green'
#x = plt.hist(data["media"][10:15], 5, color='steelblue', alpha=0.5, rwidth=0.85, edgecolor = 'black', linewidth=1)
#
##plt.title('Algoritmo 3', size= 12)
#plt.xlabel('Tiempo Ejecución ', size= 12)
#plt.ylabel('Probabilidad de Ocurrencia', size= 12)
#
#plt.subplot(324)
#x = plt.hist(data["media"][15:20], 5, facecolor='#E69F00', alpha=0.5, rwidth=0.85, normed=True, histtype='stepfilled', linewidth=1)
#
##plt.title('Algoritmo 4', size= 12)
#plt.xlabel('Tiempo Ejecución ', size= 12)
#plt.ylabel('Probabilidad de Ocurrencia', size= 12)
#
#plt.subplot(325)
#x = plt.hist(data["media"][20:25], 5, facecolor='darkgreen', alpha=0.5, rwidth=0.85, linewidth=1)
#
##plt.title('Algoritmo 5', size= 12)
#plt.xlabel('Tiempo Ejecución ', size= 12)
#plt.ylabel('Probabilidad de Ocurrencia', size= 12)
#
#plt.subplots_adjust(left=0.15)
#plt.savefig("HNuevo.eps")
#plt.tight_layout()
#plt.legend()
#plt.show()
    
#MakeScatter("valores.csv") 
#------------------------------------Para Graficar el Escatter Plot-------------------------------------------------
#def ScatterNodes(nameFile):
#data = pd.read_csv(nameFile)
#
#color_names = ["black", "green", "red", "blue", "yellow"]
#
#variation = np.diff(data["media"]) / data["media"][:-1]
#print(variation)
#
#betweenness_centrality = data[(data["Alg1"] == "betweenness_centrality")]
#minimun_spanning_tree= data[(data["Alg1"] == "minimum_spanning_tree")]
#greedy_color = data[(data["Alg1"] == "greedy_color")]
#max_clique = data[(data["Alg1"] == "max_clique")]
#maximal_matching = data[(data["Alg1"] == "maximal_matching")]
#
##dfs_tree = data[(data["Alg1"] == "dfs_tree")]
#
#size = (5 * data["arcos"][:5] / data["nodos"][:5])
#
#figure, axis = plt.subplots(figsize=(8, 8))
#axis.scatter(betweenness_centrality["media"], betweenness_centrality["nodos"],
#            s=size, c=color_names, marker="+",
#            label="Algoritmo Betweenness centrality", alpha=0.8, edgecolors='none')
#
##figure, axis = plt.subplots(figsize=(8, 8))
#axis.scatter(minimun_spanning_tree["media"], minimun_spanning_tree["nodos"],
#            s=size, c=color_names, marker="*",
#            label="Algoritmo Minimun Spanning Tree", alpha=0.8, edgecolors='none')
#
#
##figure, axis = plt.subplots(figsize=(8, 8))
#axis.scatter(greedy_color["media"], greedy_color["nodos"],
#            s=size, c=color_names, marker="D",
#            label="Algoritmo Greedy color", alpha=0.8, edgecolors='none')
#
##figure, axis = plt.subplots(figsize=(8, 8))
#axis.scatter(max_clique["media"], max_clique["nodos"],
#            s=size, c=color_names, marker="o",
#            label="Algoritmo Max Clique", alpha=0.8, edgecolors='none')
#
#
#axis.scatter(maximal_matching ["media"], maximal_matching ["nodos"],
#            s=size, c=color_names, marker="o",
#            label="Algoritmo maximal_matching ", alpha=0.8, edgecolors='none')
#
#axis.set_ylabel("Cantidad de nodos del grafo (units)", fontsize=10)
#axis.set_xlabel("Tiempo de ejecucion", fontsize=10)
#plt.ylim((min(greedy_color["nodos"])-5, max(greedy_color["nodos"]) + 5))
#
#print(axis)
#plt.axis('on')
#plt.savefig("scatterPlot.eps")
#axis.legend()
#plt.show()

guardarDatosenCSV('grafo')
