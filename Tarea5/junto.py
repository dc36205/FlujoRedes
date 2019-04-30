# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 01:50:43 2019

@author: Daniel Chong
"""
import networkx as nx
import numpy as np 
import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt
from time import time
from scipy.stats import truncnorm
import scipy.stats as scipy
from networkx.algorithms.flow import edmonds karp 
from networkx.algorithms.flow import maximum flow
import researchpy as rp

import statsmodels.api as sm
from statsmodels.formula.api import ols

import pingouin as pg
import seaborn as sns
from statsmodels.stats.multicomp import pairwise tukeyhsd
import csv

def GeneradorDeGrafo(n, k, p): 
    s=nx.watts strogatz graph(n, k, p) 
    scale = 2 
    rang = 10 
    size=s.number of edges()
    e=s.edges(nbunch=None, data=True, default=None)
    X = truncnorm(a=-rang/scale, b=+rang/scale, scale=scale).rvs(size=size) 
    X = X.round().astype(int)+rang+2
    G=nx.Graph()
    count=0
    for i in e:
        G.add_edge(i[0], i[1], capacity=X[count])
        count+=1        
    df=pd.DataFrame()
    df=nx.to pandas adjacency(G, dtype=int, weight='capacity')
    df.to csv("grafo1.csv", index=None, header=None)
        
def CapturarGraph(adress):
    ds = pd.read csv(adress, header=None)
    G = nx.from pandas adjacency(ds)
    return G    
    
def Edmond(G,a,b): 
    start time=time()          
    edmonds karp(G, a, b, capacity ='weight') 
    time elapsed = time() - start time      
    return time elapsed

def CalculoTiemp(G):    
    dic={"Grafo":[],"Fuente":[], "Sumidero":[], "Media":[], "Mediana":[], "Std":[], "FlujoMax":[] ,"Grado":[], "Coef Agrup":[], "Centralidad Ce":[], "Centralidad Car":[], "Excentricidad":[], "PageRank":[] }   
    Nodes=G.nodes;
    for i in Nodes: 
        for j in Nodes: 
            if i!=j: 
                t=[]                    
                for k in range(5): 
                   t.append(Edmond(G,i,j))                   
                dic["Grafo"].append(nombre)    
                dic["Fuente"].append(i)    
                dic["Sumidero"] .append(j)  
                dic["Media"].append(np.mean(t))    
                dic["Mediana"].append(np.median(t))    
                dic["Std"].append(np.std(t)) # standar Desviation         
                dic["FlujoMax"].append(nx.maximum flow value(G, i, j, capacity='weight')) 
                dic["Grado"].append(G.degree(i)) 
                dic["Coef Agrup"].append(nx.clustering(G,i))
                dic["Centralidad Ce"].append(nx.closeness centrality(G,i))
                dic["Centralidad Car"].append(nx.load centrality(G,i))
                dic["Excentricidad"].append(nx.eccentricity(G,i))
                PageR=nx.pagerank(G,weight="capacity")                
                dic["PageRank"]=PageR[i]
    df=pd.DataFrame(dic)
    df.to_csv("times.csv", index=None, mode ='a')
    
def Combo():
    list= [ "timesdelGrafo7.csv" ,"timesdelGrafo8.csv" ,"timesdelGrafo9.csv" ,"timesdelGrafo10.csv" ,"timesdelGrafo11.csv" ]     
    props= [ "Grado" ,"Coef Agrup" ,"Centralidad Ce" ,"Centralidad Car" ,"Excentricidad", "PageRank"]   
    for i in list:   
        df = pd.read csv(i)
        dfil = df.groupby(["Fuente"]).median()
        for prop in props:     
            fig = plt.figure(figsize=(10, 10))
            ax = fig.add_subplot(1, 1, 1)
            count, bins, ignored = ax.hist(dfil[prop],bins=len(dfil[prop]), density=1, facecolor='#61b136', alpha=0.85, edgecolor="black", linewidth=0.3)
            ymax_val = max(count) + 0.005            
            bincenters = 0.5*(bins[1:]+bins[:-1])            
            mu = dfil[prop].mean()
            sigma = round(stats.pstdev(dfil[prop], mu), 2)            
            y = scipy.norm.pdf(bincenters, mu, sigma)            
            ax.plot(bincenters, y, 'r--', linewidth=2.5)            
            ax.setxlabel('Valores de ' + prop)
            ax.setylabel('Ocurrencia')            
            ax.setxlim(min(dfil[prop]), max(dfil[prop]))
            ax.setylim(0, ymaxval)
            ax.grid(True)    
            plt.savefig("hist_" + prop + i +".png", bbox_inches="tight", dpi=100)
            plt.savefig("hist_" + prop + i +".eps", bbox_inches="tight", dpi=100)
            plt.show()     
            
def UniondeCSV(): 
    list={"grafo1.csv" , "grafo2.csv" , "grafo3.csv" , "grafo4.csv" , "grafo5.csv"}
    for i in list:
        G=ReadGraph(i)
        Time(G)
        
def PintarGrafoResidual(G, pos, fuentes, sumideros): 
    pos=nx.kamada_kawai layout(G,scale=1.2)     
    negros=[]
    flujos=[]
    rojos=[]
    negrospesos=[]
    rojospesos=[]
    maxi=0
    for edge in G.edges:
        if G.edges[edge]['flow']==0:
            negros.append(edge)
            negrospesos.append(G.edges[edge]['capacity'])
        else:
            rojos.append(edge)
            rojospesos.append(G.edges[edge]['capacity'])
            flujos.append(G.edges[edge]['flow'])
    flujos[:] = [x+300 for x in flujos]
    for i in flujos:
        if i>maxi:
            maxi=i
    negrospesos[:] = [x/10*x/7 for x in negrospesos]
    rojospesos[:] = [x/10*x/7 for x in rojospesos]   
    nx.draw networkx nodes(G, pos, node_size=200, nodecolor='r', node_shape='o')   
    nx.draw networkx nodes(G, pos, nodelist=fuentes, node size=200, node color='y', node shape='o')  
    nx.draw networkx nodes(G, pos, nodelist=sumideros, node size=200, node color='b', node shape='o')     
    nx.draw networkx edges(G, pos, edgelist=negros, edge color='g', width=negrospesos, arrows=False)   
    nx.draw networkx edges(G, pos, edgelist=rojos, edgecmap=plt.cm.Blues, width=rojospesos, edge color='g', arrows=False)
    labels = {}
    for i in G.nodes:
        labels[i]=str(i)
    nx.draw networkx labels(G, pos, labels, font size=8)    
    plt.axis('off')    
    plt.savefig("fig8delGrafo8.eps",dpi=500)        
    
#-----------------------------------------------------------------------------------------------------------------------
df = pd.read_csv("timesCopiaKOk.csv", index_col=None, usecols=[4,7,8,9,10,11,12],dtype={ 'Mediana': np.float64, 'Grado': np.int, 'CoefAgrup':np.float64, 'CentralidadCe': np.float64,'CentralidadCar': np.float64,
                                                                        'Excentricidad': np.int,'PageRank': np.float64} )

for column in range(0, df["PageRank"].count()):
    pass
    if  df.iat[column, 6] >=0.0399806  and df.iat[column, 6] < 0.04669785 :
        df.iat[column, 6] = 1
    elif df.iat[column, 6] >=0.04669785  and df.iat[column, 6] < 0.0534151:
        df.iat[column, 6] = 2
    else:
        df.iat[column, 6] = 3
df['PageRank'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
for column in range(0, df["CoefAgrup"].count()):
    pass
    if  df.iat[column, 2] >=0 and df.iat[column, 2] < 0.33333333:
        df.iat[column, 2] = 1
    elif df.iat[column, 2] >=0.33333333 and df.iat[column, 2] < 0.66666667:
        df.iat[column, 2] = 2
    else:
        df.iat[column, 2] = 3
df['CoefAgrup'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
for column in range(0, df["CentralidadCe"].count()):
    pass
    if  df.iat[column, 3] >=0.33333333 and df.iat[column, 3] < 0.39814815:
        df.iat[column, 3] = 1
    elif df.iat[column, 3] >=0.39814815 and df.iat[column, 3] < 0.46296296:
        df.iat[column, 3] = 2
    else:
        df.iat[column, 3] = 3
df['CentralidadCe'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
for column in range(0, df["CentralidadCar"].count()):
    pass
    if  df.iat[column, 4] >=0 and df.iat[column, 4] < 0.08828785:
        df.iat[column, 4] = 1
    elif df.iat[column, 4] >=0.08828785 and df.iat[column, 4] < 0.1765757:
        df.iat[column, 4] = 2
    else:
        df.iat[column, 4] = 3
df['CentralidadCar'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
for column in range(0, df["Grado"].count()):
    pass
    if  df.iat[column, 1] >=2 and df.iat[column, 1] < 3.33333333:
        df.iat[column, 1] = 1
    elif df.iat[column, 1] >=3.33333333 and df.iat[column, 1] < 4.66666667:
        df.iat[column, 1] = 2
    else:
        df.iat[column, 1] = 3
df['Grado'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
for column in range(0, df["Excentricidad"].count()):
    pass
    if  df.iat[column, 5] >=3 and df.iat[column, 5] < 3.66666667:
        df.iat[column, 5] = 1
    elif df.iat[column, 5] >=3.66666667 and df.iat[column,5] < 4.66666667:
        df.iat[column, 5] = 2
    else:
        df.iat[column, 5] = 3
df['Excentricidad'].replace({1:"baja", 2: 'media', 3:'alta' }, inplace= True)
logX = np.log1p(df['Mediana'])
df = df.assign(mediana_log=logX.values)
df.drop(['Mediana'], axis= 1, inplace= True)
factores=["Grado","CoefAgrup","CentralidadCe","CentralidadCar","Excentricidad","PageRank"]
plt.figure(figsize=(8, 6))
for i in factores:
        anova = pg.anova (dv='mediana_log', between=i, data=df, detailed=True , )
    pg. export table (anova,("ANOVAs"+i+".csv"))
    ax=sns.boxplot(x=df["mediana_log"], y=df[i], data=df, palette="cubehelix")
    plt.savefig("boxplot_" + i + ".eps", bbox inches='tight')
    tukey = pairwise tukeyhsd(endog = df["mediana_log"], groups= df[i], alpha=0.05)
    tukey.plot_simultaneous(xlabel='Tiempo', ylabel=i)
    plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")
    plt.savefig("simultaneous_tukey" + i + ".eps", bbox inches='tight')
    print(tukey.summary())
    t_csv = open("Tukey"+i+".csv", 'w')
    with t_csv:
        writer = csv.writer(t csv)
        writer.writerows(tukey.summary())
    plt.show()    
        