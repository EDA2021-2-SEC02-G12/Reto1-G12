"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
import time
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as qu

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog(tad_list_type):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artworks': None,
               'artists': None,}

    catalog['artworks'] = lt.newList(datastructure=tad_list_type)
    catalog['artists'] = lt.newList(datastructure=tad_list_type,
                                    cmpfunction=compareartists)

    return catalog
# Construccion de modelos

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['artworks'], artwork)


def addArtist(catalog, artist):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['artists'], artist)

# Funciones para creacion de datos

def ultimo_elemento(catalog):
    lt.size(catalog['artworks'])
    

# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista
def compareartists(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menor que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    f1 = artwork1["DateAcquired"]
    f2 = artwork2["DateAcquired"]
    f1_lst = f1.split("-")
    f2_lst = f2.split("-")
    ret = None

    if len(f1_lst) > len(f2_lst):
        ret = False
    elif len(f1_lst) < len(f2_lst):
        ret = True
    elif len(f1_lst) == 3 and len(f2_lst) == 3:
        if f1_lst[0] < f2_lst[0]:
            ret = True
        elif f1_lst[0] > f2_lst[0]:
            ret = False
        elif f1_lst[0] == f2_lst[0]:
            if f1_lst[1] < f2_lst[1]:
                ret = True
            elif f1_lst[1] > f2_lst[1]:
                ret = False
            else:
                if f1_lst[2] < f2_lst[2]:
                    ret = True
                elif f1_lst[2] > f2_lst[2]:
                    ret = False
                else:
                    ret = False
    return ret

# Funciones de ordenamiento

def sort_adq(catalog, size , algo_type):
    sub_list = lt.subList(catalog['artworks'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if algo_type == 1:
        sorted_list = ins.sort(sub_list, cmpArtworkByDateAcquired)
    elif algo_type == 2:
        sorted_list = sa.sort(sub_list, cmpArtworkByDateAcquired)
    elif algo_type == 3:
        sorted_list = mer.sort(sub_list, cmpArtworkByDateAcquired)
    elif algo_type == 4:
        sorted_list = qu.sort(sub_list , cmpArtworkByDateAcquired)
    
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
