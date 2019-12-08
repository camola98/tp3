from heapq import heappush, heappop, heapify
from cola import *
import random

def bfs(grafo, origen, destino):
    visitados = set()
    padres = {}
    orden = {}
    q = Cola()
    visitados.add(origen)
    padres[origen] = None
    orden[origen] = 0
    q.encolar(origen)
    while not q.esta_vacia():
        v = q.desencolar()
        if v == destino:
            break
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v
                orden[w] = orden[v] + 1
                q.encolar(w)
    
    return orden, padres

def reconstruir_ciclo(padres, origen, v):
    recorrido = [v]
    while recorrido[0] != origen:
        recorrido.insert(0, padres[recorrido[0]])
    recorrido.append(origen)
    return recorrido

def _obtener_ciclo_n_dfs(grafo, v, padres, orden, origen, n):
    if orden[v] == n-1 and grafo.estan_unidos(v, origen): 
        return reconstruir_ciclo(padres, origen, v)
    if orden[v] > n:
        padres.pop(v)
        orden.pop(v)
        return None
    for w in grafo.adyacentes(v):
        if w not in padres:
            padres[w] = v
            orden[w] = orden[v] + 1
            ciclo_n = _obtener_ciclo_n_dfs(grafo, w, padres, orden, origen, n)
            if ciclo_n: return ciclo_n

    padres.pop(v)
    orden.pop(v)
    return None

def obtener_ciclo_n_dfs(grafo, origen, n):
    padres = {}
    orden = {}
    padres[origen] = None
    orden[origen] = 0
    ciclo_n = _obtener_ciclo_n_dfs(grafo, origen, padres, orden, origen, n)
     
    return ciclo_n

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

def camino_minimo(grafo, origen, destino, valor):
    dist = {}
    padre = {}
    for v in grafo.ver_vertices(): dist[v] = -1
    dist[origen] = 0
    padre[origen] = None
    heap = []
    heapify(heap)
    heappush(heap, (dist[origen], origen))
    while len(heap) > 0:
        v = heappop(heap)[1]
        if destino and v == destino: break
        for w in grafo.adyacentes(v):
            if (dist[w] == -1) or (dist[v] + (grafo.peso(v, w))[valor] < dist[w]):
                dist[w] = dist[v] + (grafo.peso(v, w))[valor]
                padre[w] = v
                heappush(heap, (dist[w], w))
    
    return dist, padre

def segundo_elem(elem):
    return elem[1]

def ordenar_vertices(distancias):
    ordenados = []
    dists = list(distancias.items())
    dists.sort(key = segundo_elem, reverse = True)
    for i in range(len(dists)): ordenados.append(dists[i][0])
    return ordenados

def centralidad_aux(grafo):
    cent = {}
    for v in grafo.ver_vertices(): cent[v] = 0
    for v in grafo.ver_vertices():
        distancias, padre = camino_minimo(grafo, v, None, 2)
        cent_aux = {}
        for w in grafo.ver_vertices(): cent_aux[w] = 0
        vertices_ordenados = ordenar_vertices(distancias)
        for w in vertices_ordenados:
            if not padre[w]: continue
            cent_aux[padre[w]] += 1 + cent_aux[w]
        for w in grafo.ver_vertices():
            if w == v: continue
            cent[w] += cent_aux[w]
    return cent

def camino_aleatorio(grafo):
    visitados = set()
    cent = {}
    vertices = list(grafo.ver_vertices())
    for _ in range(100000):
        v = random.choice(vertices)
        if v in visitados or not grafo.adyacentes(v): continue
        visitados.add(v)
        for _ in range(50000):
            w = ady_aleatorio(grafo, v)
            cent[w] = cent.get(w,0) + 1
            if grafo.adyacentes(w): 
                v=w
                visitados.add(v)
    return cent

def ady_aleatorio(grafo, v):
    total = 0
    pesos = {}
    for w in grafo.adyacentes(v):
        pesos[w] = grafo.peso(v,w)[2]
        total+= pesos[w]
    rand = random.uniform(0, total)
    acum = 0
    for vertice, peso_arista in pesos.items():
        if acum + peso_arista >= rand:
            return vertice
        acum += peso_arista

#def arista_mas_pesada(grafo, v, visitados):
#    peso_max = 0
#    adyacente_mas_pesado = v
#    for w in grafo.adyacentes(v):
#        if w in visitados: continue
#        if grafo.peso(v,w)[2]>peso_max:
#            peso_max = grafo.peso(v,w)[2]
#            adyacente_mas_pesado = w
#    return adyacente_mas_pesado

def recorrido_orden_n(grafo, origen, n):
    for w in grafo.adyacentes(origen):
        visitados = [origen, w]
        _recorrido_orden_n(grafo, origen, w, n, visitados)
        if (len(visitados) == n and visitados[0] == visitados[-1] == origen): return visitados


def _recorrido_orden_n(grafo, origen, vertice, n, visitados):
    if (n==1 and not grafo.estan_unidos(vertice, origen)): return
    visitados.append(vertice)
    if n==1:
        visitados.append(origen)
        return visitados
    for w in grafo.adyacentes(vertice):
        if w in visitados: continue
        visitados.append(w)
        _recorrido_orden_n(grafo, origen, vertice, n-1, visitados)
        if (len(visitados) == n and visitados[0] == visitados[-1] == origen): return visitados
