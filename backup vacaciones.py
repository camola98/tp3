def _obtener_ciclo_n_dfs(grafo, v, padres, orden, origen, n, aeropuertos):
    if orden[v] == n-1:
        for a in aeropuertos:
            if grafo.estan_unidos(a,v): return reconstruir_ciclo(padres, origen, v, a)
    for w in grafo.adyacentes(v):
        if w not in padres and orden[v] < n-1:
            padres[w] = v
            orden[w] = orden[v] + 1
            ciclo_n = _obtener_ciclo_n_dfs(grafo, w, padres, orden, origen, n, aeropuertos)
            if ciclo_n: 
                return ciclo_n

    padres.pop(v)
    orden.pop(v)
    return None

def obtener_ciclo_n_dfs(grafo, origen, n, aeropuertos):
    padres = {}
    orden = {}
    for a in aeropuertos:
        padres[a] = None
        orden[a] = 0
    ciclo_n = _obtener_ciclo_n_dfs(grafo, origen, padres, orden, origen, n, aeropuertos)
     
    return ciclo_n

Chequeando ordenes:

def _obtener_ciclo_n_dfs(grafo, v, padres, orden, ord_probados, origen, n, aeropuertos):
    if orden[v] == n-1:
        for a in aeropuertos:
            if grafo.estan_unidos(a,v): return reconstruir_ciclo(padres, origen, v, a)
    for w in grafo.adyacentes(v):
        if w not in padres and orden[v] < n-1:
            if (w not in ord_probados or (orden[v] + 1) not in ord_probados[w]):
                padres[w] = v
                orden[w] = orden[v] + 1
                if w not in ord_probados: ord_probados[w] = set()
                ord_probados[w].add(orden[w])
                ciclo_n = _obtener_ciclo_n_dfs(grafo, w, padres, orden, ord_probados, origen, n, aeropuertos)
                if ciclo_n: 
                    return ciclo_n

    padres.pop(v)
    orden.pop(v)
    return None

def obtener_ciclo_n_dfs(grafo, origen, n, aeropuertos):
    padres = {}
    orden = {}
    ord_probados = {}
    for a in aeropuertos:
        padres[a] = None
        orden[a] = 0
        ord_probados[a] = 0
    ciclo_n = _obtener_ciclo_n_dfs(grafo, origen, padres, orden, ord_probados, origen, n, aeropuertos)
     
    return ciclo_n