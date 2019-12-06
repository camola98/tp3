from Git.Grafo.cola import *
from Git.Grafo.grafo import *

#Verifica si los vértices de un grafo pueden dividirse en dos conjuntos
def es_bipartito(grafo):
    origen = grafo.v_random()
    q = Cola()
    q.encolar(origen)
    colores = {}
    colores[origen] = 1
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if w not in colores:
                colores[w] = not colores[v]
                q.encolar(w)
            if w in colores and colores[w] == colores[v]:
                return False
    return True