from cola import *

def peliculas_marvel(peliculas):
    grados = {}
    for v in peliculas.ver_vertices():
        grados[v] = 0
    for v in peliculas.ver_vertices():
        for w in peliculas.adyacentes(v):
            grados[w] += 1
    q = Cola()
    for v in peliculas.ver_vertices():
        if grados[v] == 0:
            q.encolar(v)
    orden_peliculas = []
    while not q.esta_vacia():
        v = q.desencolar()
        orden_peliculas.append(v)
        for w in peliculas.adyacentes(v):
            grados[w] -= 1
            if grados[w] == 0:
                q.encolar(w)
    return orden_peliculas