'''Comandos a codear:
listar_operaciones() : imprime las funcionalidades disponibles en O(1).
*camino_mas(barato o rapido, origen, destino) : imprime una lista con los 
    aeropuertos con los cuales vamos de la ciudad origen a la ciudad 
    destino de la forma más rápida o más barata, teniendo en cuenta todos
    los aeropuertos, y todas las combinaciones posibles. En O(Flog(A)), 
    A cantidad de aeropuertos, y F cantidad de vuelos entre aeropuertos.
*camino_escalas(origen, destino) : imprime lista con los aeropuertos con
    los cuales vamos de origen a destino con la menor cantidad de escalas.
    O(F+A), A la cantidad de aeropuertos, y F de vuelos entre aeropuertos.
***centralidad(cantidad de aeropuertos a mostrar): imprime de mayor 
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
***recorrer_mundo(ciudad de origen): devuelve una lista en orden de cómo debemos 
    movernos por el mundo para visitar todas las ciudades del mundo, demorando 
    lo menos posible. Podemos volver a usar un aeropuerto ya usado, u otro de alguna 
    ciudad ya visitada, si eso mejora la duración de nuestro viaje. 
    O(lo que se nos cante).
*recorrer_mundo_aprox(origen): lo mismo pero aprox. O(idealmente cuadratico).
***vacaciones(origen, n): Obtener algún recorrido que comience en origen y que 
    termine en origen también, de largo n (sin contar la última vuelta al origen).
    Si no puede devuelve "No se encontro recorrido". O(A^n).
**itinerario(la ruta el archivo del itinerario): La primera línea indica las ciudades 
    que se desean visitar. Las siguientes indican la prioridad. Imprimir el orden en 
    el que deben visitarse dichas ciudades. Imprimir el camino mínimo en tiempo o 
    escalas (según lo que se haya implementado en ese caso) a realizar. O(I+R)
    I la cantidad de ciudades a visitar, y R la cantidad de restricciones impuestas.
    El cálculo de los caminos debe realizarse en O(I*Flog(A)) o bien O(I*(A+F)).
*exportar_kml(archivo): exporta el archivo KML con la ruta del último comando ejecutado.
    Cualquier comando salvo estadísticas, u obtención de los aeropuertos más centrales.
    O(A+F).
'''
