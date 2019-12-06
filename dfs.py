from Git.Grafo.cola import *
from Git.Grafo.grafo import *

#Recorrido en profundidad (recursivo)
def _dfs(grafo, v, visitados, padres, orden):
    visitados.add(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            padres[w] = v
            orden[w] = orden[v] + 1
            _dfs(grafo, w, visitados, padres, orden)

def dfs(grafo):
    visitados = set()
    padres = {}
    orden = {}
    for v in grafo.ver_vertices():
        if v not in visitados:
            padres[v] = None
            orden[v] = 0
            _dfs(grafo, v, visitados, padres, orden)

    return padres, orden