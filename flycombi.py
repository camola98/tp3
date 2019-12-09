import sys
import csv
from grafo import Grafo
from biblioteca import *

COMANDOS = ["camino_mas", "camino_escalas", "centralidad", "recorrer_mundo", "vacaciones", "itinerario"]

'''
    Comandos a codear:
    11*/10* para aprobar
    11*/12* para buena nota
    11*/16* para el 11
    11*/20* en total

listar_operaciones() : imprime las funcionalidades disponibles en O(1).
✓ *camino_mas(barato o rapido, origen, destino) : imprime una lista con los 
    aeropuertos con los cuales vamos de la ciudad origen a la ciudad 
    destino de la forma más rápida o más barata, teniendo en cuenta todos
    los aeropuertos, y todas las combinaciones posibles. En O(Flog(A)), 
    A cantidad de aeropuertos, y F cantidad de vuelos entre aeropuertos.
✓ *camino_escalas(origen, destino) : imprime lista con los aeropuertos con
    los cuales vamos de origen a destino con la menor cantidad de escalas.
    O(F+A), A la cantidad de aeropuertos, y F de vuelos entre aeropuertos.
✓ ***centralidad(cantidad de aeropuertos a mostrar): imprime de mayor 
    importancia a menor importancia los n aeropuertos más centrales/
    importantes del mundo. O(A×Flog(A)). 
✓centralidad_aprox(cantidad de aeropuertos a mostrar): mismo que arriba.
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
✓ ***vacaciones(origen, n): Obtener algún recorrido que comience en origen y que 
    termine en origen también, de largo n (sin contar la última vuelta al origen).
    Si no puede devuelve "No se encontro recorrido". O(A^n).
X **itinerario(la ruta el archivo del itinerario): La primera línea indica las ciudades 
    que se desean visitar. Las siguientes indican la prioridad. Imprimir el orden en 
    el que deben visitarse dichas ciudades. Imprimir el camino mínimo en tiempo o 
    escalas (según lo que se haya implementado en ese caso) a realizar. O(I+R)
    I la cantidad de ciudades a visitar, y R la cantidad de restricciones impuestas.v
    El cálculo de los caminos debe realizarse en O(I*Flog(A)) o bien O(I*(A+F)).
*exportar_kml(archivo): exporta el archivo KML con la ruta del último comando ejecutado.
    Cualquier comando salvo estadísticas, u obtención de los aeropuertos más centrales.
    O(A+F).
'''
def itinerario(aeropuertos, vuelos, nombre_ruta):
    grafo = Grafo(True)
    with open (nombre_ruta, "r") as archivo:
        archivo_csv = csv.reader(archivo) 
        ciudades = next(archivo_csv)
        for ciudad in ciudades: grafo.agregar_vertice(ciudad)
        for linea in archivo_csv: grafo.agregar_arista(linea[0],linea[1],0)
    orden = orden_topo(grafo)
    print(", ".join(orden))
    for i in range(len(orden) - 1):
        camino_escalas(aeropuertos, vuelos, orden[i], orden[i+1])

def vacaciones(aeropuertos, vuelos, origen, n):
    for a_origen in aeropuertos[origen]:
        recorrido = obtener_ciclo_n_dfs(vuelos, a_origen, n, aeropuertos[origen])
        if recorrido: break
    if not recorrido: print("No se encontro recorrido") 
    else: print(" -> ".join(recorrido))

def centralidad(vuelos, n):
    cent = centralidad_aux(vuelos)
    centrales_ordenados = ordenar_vertices(cent)
    print(", ".join(centrales_ordenados[:n]))

def centralidad_aprox(grafo,n):
    cent = camino_aleatorio(grafo)
    centrales_ordenados = ordenar_vertices(cent)
    print(", ".join(centrales_ordenados[:n]))

def camino_aux(minimo):
    recorrido = [minimo[3]]
    while recorrido[0] != minimo[2]:
        recorrido.insert(0, (minimo[1])[recorrido[0]])
    print(" -> ".join(recorrido))

def camino_mas(aeropuertos, vuelos, filtro, origen, destino):
    peso = 0
    if filtro == "barato":
        peso = 1
    minimo = ()
    for a_origen in aeropuertos[origen]:
        for a_destino in aeropuertos[destino]:
            dist, padre = camino_minimo(vuelos, a_origen, a_destino, peso)
            if not len(minimo) or (dist[a_destino] < (minimo[0])[minimo[3]]):
                minimo = (dist, padre, a_origen, a_destino)
    camino_aux(minimo)  

def camino_escalas(aeropuertos, vuelos, origen, destino):
    minimo = ()
    for a_origen in aeropuertos[origen]:
        for a_destino in aeropuertos[destino]:
            orden, padre = bfs(vuelos, a_origen, a_destino)
            if not len(minimo) or (orden[a_destino] < (minimo[0])[minimo[3]]):
                minimo = (orden, padre, a_origen, a_destino)
    camino_aux(minimo)
    
def procesar_archivos():
    aeropuertos = {}    
    vuelos = Grafo(False)
    with open(sys.argv[1]) as a:
        a_csv = csv.reader(a)
        for linea in a_csv:
            aeropuertos[linea[0]] = aeropuertos.get(linea[0], []) + [linea[1]]
    with open(sys.argv[2]) as v:
        v_csv = csv.reader(v)
        for origen, destino, tiempo, precio, cant_vuelos in v_csv:
            vuelos.agregar_arista(origen, destino, (int(tiempo), int(precio), int(cant_vuelos)))
    return aeropuertos, vuelos

def listar_operaciones():
    [print(c) for c in COMANDOS]

def ejecutar_comandos(comando_arr, aeropuertos, vuelos):
    if comando_arr[0] == "listar_operaciones":
        return listar_operaciones()
    datos = (" ".join(comando_arr[1:])).split(",")
    if comando_arr[0] == "camino_mas":
        return camino_mas(aeropuertos, vuelos, datos[0], datos[1], datos[2])
    if comando_arr[0] == "camino_escalas":
        return camino_escalas(aeropuertos, vuelos, datos[0], datos[1])
    if comando_arr[0] == "centralidad":
        return centralidad(vuelos, int(datos[0]))
    if comando_arr[0] == "vacaciones":
        return vacaciones(aeropuertos, vuelos, datos[0], int(datos[1]))
    if comando_arr[0] == "centralidad_aprox":
        return centralidad_aprox(vuelos, int(datos[0]))
    if comando_arr[0] == "itinerario":
        return itinerario(aeropuertos, vuelos, datos[0])

def procesar_entradas(aeropuertos, vuelos):
    for linea in sys.stdin:
        comando_arr = (linea.rstrip('\n')).split(" ")
        ejecutar_comandos(comando_arr, aeropuertos, vuelos)

def main():
    aeropuertos, vuelos = procesar_archivos()
    procesar_entradas(aeropuertos, vuelos)

main()