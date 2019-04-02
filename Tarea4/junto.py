# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:26:52 2019

@author: Daniel Chong
"""

import numpy as np
import networkx as nx
from networkx.algorithms.flow import dinitz
from networkx.algorithms.flow import maximum_flow_value
from networkx.algorithms.flow import shortest_augmenting_path
import datetime as dt
import pandas as pd
import statistics as stats

mu, sigma = 15, 0.2
cantidad_instancias_grafo = 10
rango_instancias_grafo = 11 
mediciones = 5
tipo_x_nodos = 4 
base_calculo_nodos = 2.6 
archivo_CSV = "Datoss.csv"
base_inicio_calculo_nodos = 4
probabilidad = 0.215 
control_iteraciones = 0
generadores_grafos = {"powerlaw_cluster_graph":nx.powerlaw_cluster_graph,"watts_strogatz_graph": nx.watts_strogatz_graph, "connected_watts_strogatz_graph": nx.connected_watts_strogatz_graph }
algoritmos_flujo = { "maximum_flow_value": maximum_flow_value,  "dinitz": dinitz,"shortest_augmenting_path": shortest_augmenting_path}
estructura_CSV = {"grafo": [],"generador": [], "algoritmo_flujo": [], "vertices": [],"aristas": [],"fuente": [],"sumidero": [],"densidad": [],"media": [],"mediana": [],
    "varianza": [],"desviacion": []}
for generador_grafo in generadores_grafos:
    for instancia_grafo_x_nodos in [round(pow(base_calculo_nodos, value + 1))
                                    for value in
                                    range(base_inicio_calculo_nodos, base_inicio_calculo_nodos + tipo_x_nodos)]:        
        for grafo in range(1, cantidad_instancias_grafo + 1):
            USGraph = generadores_grafos[generador_grafo](instancia_grafo_x_nodos, round((instancia_grafo_x_nodos * probabilidad) / 2),probabilidad, seed=None)            
            fuente = np.random.randint(1, high=(instancia_grafo_x_nodos - 1), dtype="int")
            sumidero = np.random.randint(1, high=(instancia_grafo_x_nodos - 1), dtype="int")             
            while sumidero == fuente:
                fuente = np.random.randint(1, high=(instancia_grafo_x_nodos - 1), dtype="int")
                sumidero = np.random.randint(1, high=(instancia_grafo_x_nodos - 1), dtype="int")
            if fuente > sumidero:
                swapping = fuente
                fuente = sumidero
                sumidero = swapping            
            aristas = USGraph.number_of_edges()
            pesos_normalmente_distribuidos = np.random.normal(mu, sigma, aristas)
            loop = 0 
            for (u, v) in USGraph.edges(): 
                USGraph.edges[u, v]["capacity"] = pesos_normalmente_distribuidos[loop] 
                loop += 1
            for instancia_grafo in range(1, 11):
                for algoritmo_flujo in algoritmos_flujo:  
                    matriz_tiempos_ejecucion = []  
                    for medicion in range(1, mediciones + 1):
                        hora_inicio = dt.datetime.now()
                        obj = algoritmos_flujo[algoritmo_flujo](USGraph, fuente, sumidero, capacity="capacity")
                        hora_fin = dt.datetime.now()
                        tiempo_consumido_segundos = (hora_fin - hora_inicio).total_seconds() 
                        matriz_tiempos_ejecucion.append(tiempo_consumido_segundos)
                    media = stats.mean(matriz_tiempos_ejecucion)
                    if media == 0:                                                
                    print("iteracion %s tiempo consumido promedio %s" % (control_iteraciones + 1, round(media, 4)))
                    control_iteraciones +=1
                    estructura_CSV["grafo"].append("vertices" + str(instancia_grafo_x_nodos) + "aristas" + str(aristas))
                    estructura_CSV["algoritmo_flujo"].append(algoritmo_flujo)
                    estructura_CSV["generador"].append(generador_grafo)
                    estructura_CSV["vertices"].append(instancia_grafo_x_nodos)
                    estructura_CSV["aristas"].append(aristas)
                    estructura_CSV["fuente"].append(fuente)
                    estructura_CSV["sumidero"].append(sumidero)
                    estructura_CSV["densidad"].append(round(nx.density(USGraph),5))
                    estructura_CSV["media"].append(round(media, 5))
                    estructura_CSV["mediana"].append(round(stats.median(matriz_tiempos_ejecucion), 5))
                    estructura_CSV["varianza"].append(round(stats.pvariance(matriz_tiempos_ejecucion, mu=media), 5))
                    estructura_CSV["desviacion"].append(round(stats.pstdev(matriz_tiempos_ejecucion, mu=media), 5))
                    matriz_tiempos_ejecucion = [] 