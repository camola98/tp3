from Git.Grafo.cola import *
from Git.Grafo.grafo import *

#Solo para grafos acíclicos y dirigidos
def orden_topo(grafo):
    grados = {}
    for v in grafo.ver_vertices(): #Setea todos en grado 0
        grados[v] = 0
    for v in grafo.ver_vertices():
        for w in grafo.adyacentes(v): #Setea el grado de entrada de cada vértice
            grados[w] += 1
    q = Cola() 
    for v in grafo.ver_vertices(): #Encola todos los de grado 0
        if grados[v] == 0:
            q.encolar(v)
    resul = []
    while not q.esta_vacia():
        v = q.desencolar()
        resul.append(v) #V tiene grado 0, asi que lo appendea al resultado
        for w in grafo.adyacentes(v):
            grados[w] -= 1 #Resta un grado a todos sus adyacentes
            if grados[w] == 0: 
                q.encolar(w) #Encola el adyacente si quedó con grado 0

    return resul
