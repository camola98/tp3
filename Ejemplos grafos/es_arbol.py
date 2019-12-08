import random 

class Cola:

    def __init__(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError
        return self.items.pop(0)
        
    def esta_vacia(self):
        return len(self.items) == 0

class Grafo:
    def __init__(self, dirigido):
        self.vertices = {}
        self.dirigido = dirigido

    def ver_vertices(self):
        return self.vertices

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}
    
    def sacar_vertice(self, v):
        if not self.dirigido and v in self.vertices:
            for w in self.vertices[v]:
                self.vertices[w].pop(v)
        self.vertices.pop(v)

    def agregar_arista(self, v, w, peso):
        self.agregar_vertice(v)
        self.agregar_vertice(w)
        self.vertices[v][w] = peso
        if not self.dirigido:
            self.vertices[w][v] = peso

    def sacar_arista(self, v, w):
        if v in self.vertices and w in self.vertices[v]:
            self.vertices[v].pop(w)
            if not self.dirigido:
                self.vertices[w].pop(v)
    
    def estan_unidos(self, v, w):
        if v not in self.vertices:
            return False
        return w in self.vertices[v]

    def adyacentes(self, vertice):
        return self.vertices[vertice]

    def v_random (self):
        if not len(self.vertices):
            return None
        return random.choice(list(self.vertices.keys))

    def __repr__(self):
        cad = "{"
        for clave, valor in self.vertices.items():
            cad += "{}: {}, ".format(clave, valor)
        cad += "}"
        return cad

    def __str__(self):
        return self.vertices

def cant_vertices(grafo):
    vertices = 0
    aristas = 0
    for v in grafo.ver_vertices():
        vertices += 1
        for w in grafo.adyacentes(v):
            aristas += 1
    return vertices, aristas/2

def _hay_ciclos(grafo, v, visitados, padres):
    visitados.add(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            padres[w] = v
            if _hay_ciclos(grafo, w, visitados, padres):
                return True
        if w in visitados and w != padres[v]:
            return True
    return False

def hay_ciclos(grafo):
    visitados = set()
    padres = {}
    for v in grafo.ver_vertices():
        if v not in visitados:
            padres[v] = None
            if _hay_ciclos(grafo, v, visitados, padres):
                return True
    return False

def es_arbol(grafo):
    vertices, aristas = cant_vertices(grafo)
    return aristas == vertices - 1 and not hay_ciclos(grafo)