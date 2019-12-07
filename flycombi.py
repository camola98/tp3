import sys
import csv
from grafo import Grafo
from biblioteca import *

COMANDOS = {"camino_mas", "listar_operaciones", "camino_escalas", "centralidad", "recorrer_mundo", "vacaciones", "itinerario"}

'''
    Comandos a codear:
    4*/10* para aprobar
    4*/12* para buena nota
    4*/16* para el 11
    4*/20* en total

listar_operaciones() : imprime las funcionalidades disponibles en O(1).
X *camino_mas(barato o rapido, origen, destino) : imprime una lista con los 
    aeropuertos con los cuales vamos de la ciudad origen a la ciudad 
    destino de la forma más rápida o más barata, teniendo en cuenta todos
    los aeropuertos, y todas las combinaciones posibles. En O(Flog(A)), 
    A cantidad de aeropuertos, y F cantidad de vuelos entre aeropuertos.
X *camino_escalas(origen, destino) : imprime lista con los aeropuertos con
    los cuales vamos de origen a destino con la menor cantidad de escalas.
    O(F+A), A la cantidad de aeropuertos, y F de vuelos entre aeropuertos.
X ***centralidad(cantidad de aeropuertos a mostrar): imprime de mayor 
    importancia a menor importancia los n aeropuertos más centrales/
    importantes del mundo. O(A×Flog(A)). 
*centralidad_aprox(cantidad de aeropuertos a mostrar): mismo que arriba.
    O(A+F).
**pagerank(cantidad de aeropuertos a mostrar): los n aeropuertos más 
    centrales/importantes del mundo según el algoritmo de pagerank, de 
    mayor importancia a menor importancia. O(K(A+F)), puede 
    simplificarse O(A+F).
**nueva_aerolinea(ruta del archivo de salida): exportar un archivo con las 
    rutas que permitan implementar una nueva aerolínea tal que se pueda 
    comunicar a todos los aeropuertos (en esta primera iteración, sólo de 
    Estados Unidos) con dicha aerolínea, pero que el costo total de la 
    licitación de las rutas aéreas(trabajar con costo de pasajes) sea mínima. 
    Se busca que la nueva aerolínea pueda llegar a todos los aeropuertos. La 
    salida de este comando debe ser un archivo con el mismo formato del archivo 
    vuelos.csv, pero únicamente con las rutas de vuelo a utilizar por ésta 
    aerolínea. O(Flog(A)).
X ***recorrer_mundo(ciudad de origen): devuelve una lista en orden de cómo debemos 
    movernos por el mundo para visitar todas las ciudades del mundo, demorando 
    lo menos posible. Podemos volver a usar un aeropuerto ya usado, u otro de alguna 
    ciudad ya visitada, si eso mejora la duración de nuestro viaje. 
    O(lo que se nos cante). 
*recorrer_mundo_aprox(origen): lo mismo pero aprox. O(idealmente cuadratico).
X ***vacaciones(origen, n): Obtener algún recorrido que comience en origen y que 
    termine en origen también, de largo n (sin contar la última vuelta al origen).
    Si no puede devuelve "No se encontro recorrido". O(A^n).
X **itinerario(la ruta el archivo del itinerario): La primera línea indica las ciudades 
    que se desean visitar. Las siguientes indican la prioridad. Imprimir el orden en 
    el que deben visitarse dichas ciudades. Imprimir el camino mínimo en tiempo o 
    escalas (según lo que se haya implementado en ese caso) a realizar. O(I+R)
    I la cantidad de ciudades a visitar, y R la cantidad de restricciones impuestas.
    El cálculo de los caminos debe realizarse en O(I*Flog(A)) o bien O(I*(A+F)).
*exportar_kml(archivo): exporta el archivo KML con la ruta del último comando ejecutado.
    Cualquier comando salvo estadísticas, u obtención de los aeropuertos más centrales.
    O(A+F).
'''

def centralidad(grafo, n):
    cent = {}
    for v in grafo: cent[v] = 0
    for v in grafo:
        for w in grafo:
            distancias, padre = camino_minimo(grafo, v,w, grafo.peso(v,w))
        cent_aux = {}
        for w in grafo: cent_aux[w] = 0
        # Aca filtramos (de ser necesario) los vertices a distancia infinita, 
        # y ordenamos de mayor a menor
        vertices_ordenados = ordenar_vertices(distancias) 
        for w in vertices_ordenados:
            cent_aux[padre[w]] += 1 + cent_aux[w]
        # le sumamos 1 a la centralidad de todos los vertices que se encuentren en 
        # el medio del camino
        for w in grafo:
            if w == v: continue
            cent[w] += cent_aux[w]
    centrales_ordenados = ordenar_vertices(cent)
    for i in range(n+1):
        print (centrales_ordenados[i])


def camino_mas(aeropuertos, vuelos, datos):
    if len(datos) < 3:
        sys.stderr.write("Cant parámetros incorrecta")
        return
    tipo = {"rapido": 0, "barato": 1}
    peso, origen, destino = tipo[datos[0]], datos[1], datos[2]
    minimo = (None, None)
    for a1 in aeropuertos[origen]:
        for a2 in aeropuertos[destino]:
            dist, padre = camino_minimo(vuelos, a1, a2, peso)
            if not minimo[0] or dist < minimo[0]:
                minimo = (dist, padre)
    recorrido = [destino]
    while recorrido[0] != origen:
        recorrido.insert(0, (minimo[1])[recorrido[0]])
    print(" -> ".join(recorrido))       

def procesar_archivos():
    aeropuertos = {}    
    vuelos = Grafo(True)
    with open(sys.argv[1]) as a:
        a_csv = csv.reader(a)
        for linea in a_csv:
            aeropuertos[linea[0]] = aeropuertos.get(linea[0], []) + [linea[1]]
    with open(sys.argv[2]) as v:
        v_csv = csv.reader(v)
        for origen, destino, tiempo, precio, cant_vuelos in v_csv:
            vuelos.agregar_arista(origen, destino, (tiempo, precio, cant_vuelos))
    return aeropuertos, vuelos

def listar_operaciones():
    [print(c) for c in COMANDOS]

def ejecutar_comandos(comando, datos, aeropuertos, vuelos):
    if comando == "listar_operaciones":
        return listar_operaciones()
    if comando == "camino_mas":
        return camino_mas(aeropuertos, vuelos, datos)
    if comando == "camino_escalas":
        return camino_escalas(aeropuertos, vuelos, datos)

def procesador_entrads(aeropuertos, vuelos):
    for linea in sys.stdin:
        comando_arr = (linea.rstrip('\n')).split(" ")
        if comando_arr[0] not in COMANDOS and comando_arr[0] != "listar_operaciones":
            sys.stderr.write("Parámetro incorrecto")
            return
        ejecutar_comandos(comando_arr[0], comando_arr[1].split(","), aeropuertos, vuelos)

def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Cant parámetros incorrecta")
        return
    aeropuertos, vuelos = procesar_archivos()
    ejecutar_comandos(aeropuertos, vuelos)

main()