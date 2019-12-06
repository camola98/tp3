import random 

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
        return random.choice(list(self.vertices.keys()))

    def __repr__(self):
        cad = "{"
        for clave, valor in self.vertices.items():
            cad += "{clave}: {valor}, "
        cad += "}"
        return cad

    def __str__(self):
        return self.vertices