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
import datetime

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

    catalog['artworks'] = lt.newList(datastructure=tad_list_type, cmpfunction = cmpArtworkByDateAcquired)
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

def find_id_of_artist(catalog , artist_name):
    #REQUISITO 3

    artists = lt.subList(catalog['artists'],1,lt.size(catalog['artists']))
    artists = artists.copy()

    id = None

    for i in range(1 , lt.size(artists)):
        artist = lt.getElement(artists , i)

        if artist_name == artist["DisplayName"]:
            id = artist["ConstituentID"]
    
    return id

def list_of_artworks(catalog , id):
    #REQUISITO 3
    """
    Recibe el catalogo y el id del artista y devuelve sus obras en una lista.
    """
    
    original_list = catalog['artworks']
    new_list = lt.newList()
    i = 1
    for i in range(1 , lt.size(original_list)+1):
        artwork = lt.getElement(original_list , i)
        artwork_artists_ids = (artwork["ConstituentID"])
        artwork_artists_ids = (artwork_artists_ids.replace("[" , "")).replace("]" , "")
        list_artwork_artists_ids = (artwork_artists_ids.split(","))
        int_list_artwork_artists_ids = []
        for id_artist_str in list_artwork_artists_ids:
            int_list_artwork_artists_ids.append(int(id_artist_str))
        for each_id in int_list_artwork_artists_ids:
            if int(id) == each_id:
                lt.addLast(new_list , artwork)
    
    return new_list

def list_of_tecniques(list_of_artworks):
    #REQUISITO 3

    original_list = list_of_artworks
    list_of_tecniques = lt.newList()
    list_of_unique_tecniques = lt.newList()

    for i in range(1 , lt.size(original_list)+1):
        artwork = lt.getElement(original_list , i)
        tecnique = artwork["Medium"]
        lt.addLast(list_of_tecniques, tecnique)
    
    for j in range(1 , lt.size(list_of_tecniques)+1):
        tecnique1 = lt.getElement(list_of_tecniques , j)
        is_present = lt.isPresent(list_of_unique_tecniques , tecnique1)
        if is_present == 0:
            lt.addLast(list_of_unique_tecniques , tecnique1)
    
    return list_of_tecniques, list_of_unique_tecniques

def most_used_technique(list_of_techniques):
    #REQUISITO 3

    original_list = list_of_techniques
    most_used_technique = None
    number_of_appeareances = 0

    for i in range(1 , lt.size(original_list)+1):
        tecnique = lt.getElement(original_list , i)
        counter = 0
        for j in range(1 , lt.size(original_list)+1):
            tecnique2 = lt.getElement(original_list , j)
            if tecnique == tecnique2:
                counter += 1
        if counter > number_of_appeareances:
            number_of_appeareances = counter
            most_used_technique = tecnique
    
    return most_used_technique , number_of_appeareances

def list_of_most_used_tecnique(most_used_tecnique , list_of_artworks):
    #REQUISITO 3

    original_list = list_of_artworks
    list_of_most_used_tecnique = lt.newList()

    for i in range(1 , lt.size(original_list)+1):
        artwork = lt.getElement(original_list , i)
        if most_used_tecnique == artwork["Medium"]:
            lt.addLast(list_of_most_used_tecnique , artwork)
    
    return list_of_most_used_tecnique






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


def cmpArtistByBeginDate(artist1, artist2):
    """
    Devuelve verdadero (True) si el 'BeginDate' de artist1 es menor que el de artist2
    Args:
    artist1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artist2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    f1 = int(artist1["BeginDate"])
    f2 = int(artist2["BeginDate"])
    ret = None 

    if f1 < f2:
        ret = True
    else:
        ret = False

    return ret

# Funciones de ordenamiento

def date_filter(catalog, initial_date , final_date):
    """
    Recibe una lista y la filtra eliminando las fechas que no se encuentren en el rango
    propuesto por el ususario.
    """
    sub_list1 = lt.subList(catalog['artworks'],1,lt.size(catalog['artworks']))
    sub_list1 = sub_list1.copy()
    for i in range(1 , lt.size(sub_list1) + 1):
        artwork = lt.getElement(sub_list1 , i)
        date = tuple(artwork['DateAcquired'].split("-"))
        if lt.isPresent(sub_list1, i) == 0:
            break
        if date < initial_date or date > final_date:
            position = lt.isPresent(sub_list1 , artwork)
            lt.deleteElement(sub_list1 , position)
    return sub_list1


def sort_adquisitions_date(catalog, algo_type , initial_date , final_date):

    sub_list = filter_adquisitions(catalog, initial_date , final_date)

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

def filter_adquisitions(catalog , initial_date , final_date):
    original_list = catalog['artworks']
    new_list = lt.newList()
    i = 1
    for i in range(1 , lt.size(original_list)+1):
        artwork = lt.getElement(original_list , i)
        artwork_date_acquired = (artwork["DateAcquired"].split("-"))
        artwork_date_acquired_2 = []
        
        if (len(artwork_date_acquired[0]) != 0) and (len(artwork_date_acquired[1]) != 0 and (len(artwork_date_acquired[2]) != 0)):
            artwork_date_acquired_2.append(int(artwork_date_acquired[0]))
            artwork_date_acquired_2.append(int(artwork_date_acquired[1]))
            artwork_date_acquired_2.append(int(artwork_date_acquired[2]))
        
        elif (len(artwork_date_acquired[0]) != 0) and (len(artwork_date_acquired[1]) != 0):
            artwork_date_acquired_2.append(int(artwork_date_acquired[0]))
            artwork_date_acquired_2.append(int(artwork_date_acquired[1]))
        
        elif len(artwork_date_acquired[0]) != 0:
            artwork_date_acquired_2.append(int(artwork_date_acquired[0]))
        
        elif len(artwork_date_acquired[0]) == 0:
            artwork_date_acquired_2.append(0)

        var1 = date_comparison(artwork_date_acquired_2 , initial_date)
        var2 = date_comparison(artwork_date_acquired_2 , final_date)

        if (var1 == 1) and (var2 == 0):
            lt.addLast(new_list , artwork)
    
    return new_list

def sort_artist_date(catalog, algo_type , initial_year , final_year):

    sub_list = filter_artists(catalog , initial_year , final_year)
    sub_list = sub_list.copy()

    start_time = time.process_time()
    if algo_type == 1:
        sorted_list = ins.sort(sub_list, cmpArtistByBeginDate)
    elif algo_type == 2:
        sorted_list = sa.sort(sub_list, cmpArtistByBeginDate)
    elif algo_type == 3:
        sorted_list = mer.sort(sub_list, cmpArtistByBeginDate)
    elif algo_type == 4:
        sorted_list = qu.sort(sub_list , cmpArtistByBeginDate)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    
    return elapsed_time_mseg, sorted_list


def filter_artists(catalog , initial_year , final_year):
    original_list = catalog["artists"]
    new_list = lt.newList()
    i = 1
    for i in range(1 , lt.size(original_list)+1):
        artist = lt.getElement(original_list , i)
        artist_begin_date = int(artist["BeginDate"])
        if (artist_begin_date >= initial_year) and (artist_begin_date <= final_year):
            lt.addLast(new_list , artist)
    
    return new_list

def purchase_artworks(catalog , initial_date , final_date):
    filtered_list = filter_adquisitions(catalog , initial_date , final_date)
    counter = 0
    for i in range(1 , lt.size(filtered_list)+1):
        artist = lt.getElement(filtered_list , i)
        credit_line = artist["CreditLine"]
        if credit_line == "Purchase":
            counter += 1
    
    return counter

def find_artists(catalog , id2):
    artists = lt.subList(catalog["artists"] , 1 , lt.size(catalog["artists"]))
    artists = artists.copy()
    
    artists_list = []

    for individual in id2:
        for i in range(1, lt.size(artists)):
            artist = lt.getElement(artists, i)

            if int(individual) == int(artist["ConstituentID"]):
                artists_list.append(artist["DisplayName"])
    
    return artists_list





def date_comparison(date1, date2):
    """
    Recibe dos fechas en formato list y las compara, retorna 0 si la primera es menor y 1 si es mayor.
    """
    ret_value = None
    if len(date1) < len(date2):
        ret_value = 0
    elif len(date1) > len(date2):
        ret_value = 1
    elif len(date1) == 0 and len(date2) == 0:
        ret_value = 1
    elif len(date1) == 1 and len(date2) == 1:
        if date1[0] < date2[0]:
            ret_value = 0
        elif date1[0] > date2[0]:
            ret_value = 1
        else:
            ret_value = 1
    elif len(date1) == 2 and len(date2) == 2:
        if date1[0] < date2[0]:
            ret_value = 0
        elif date1[0] > date2[0]:
            ret_value = 1
        elif date1[0] == date2[0]:
            if date1[1] < date2[1]:
                ret_value = 0
            elif date1[1] > date2[1]:
                ret_value = 1
            elif date1[1] == date2[1]:
                ret_value = 1
    elif len(date1) == 3 and len(date2) == 3:
        if date1[0] < date2[0]:
            ret_value = 0
        elif date1[0] > date2[0]:
            ret_value = 1
        elif date1[0] == date2[0]:
            if date1[1] < date2[1]:
                ret_value = 0
            elif date1[1] > date2[1]:
                ret_value = 1
            elif date1[1] == date2[1]:
                if date1[2] < date2[2]:
                    ret_value = 0
                elif date1[2] > date2[2]:
                    ret_value = 1
                elif date1[2] == date2[2]:
                    ret_value = 1
        
    return ret_value
    

#FUNCIONES REQ 4:

def country_list(catalog):
    artists = catalog["artists"]
    countries = lt.newList()
    for i in range(1 , lt.size(artists)):
        artist = lt.getElement(artists, i)
        nationality = artist["Nationality"]
        lt.addLast(countries , nationality)

    return countries

def country_list_sorted(country_list , algo_type):
    countries = country_list
    countries_filter = lt.newList()

    for i in range(1 , lt.size(countries)+1):
        country1 = lt.getElement(countries , i)
        is_present = lt.isPresent(countries_filter , country1)
        if is_present == 0:
            lt.addLast(countries_filter , country1)
        
    sub_list = countries_filter
        
    if algo_type == 1:
        sorted_list = ins.sort(sub_list, cmpCountryByAplhabet)
    elif algo_type == 2:
        sorted_list = sa.sort(sub_list, cmpCountryByAplhabet)
    elif algo_type == 3:
        sorted_list = mer.sort(sub_list, cmpCountryByAplhabet)
    elif algo_type == 4:
        sorted_list = qu.sort(sub_list , cmpCountryByAplhabet)
        
    return sorted_list


def cmpCountryByAplhabet(country1, country2):
    """
    Devuelve verdadero (True) si country1 va antes que country 2.
    Args:
    country1
    country2
    """
    ret = None 

    if country1 < country2:
        ret = True
    else:
        ret = False

    return ret


def newDict_countries(country_list_sorted):

    catalog_countries = {}

    for i in range(1, lt.size(country_list_sorted) + 1):
        each_country = lt.getElement(country_list_sorted , i)
        catalog_countries[each_country] = None
        catalog_countries[each_country] = lt.newList(datastructure="ARRAY_LIST")

    return catalog_countries

def insert_artworks(catalog , dict_countries):
    original_list = catalog["artworks"]
    artists = catalog["artists"]

    for i in range(1 , lt.size(original_list)+1):

        artwork = lt.getElement(original_list , i)
        artwork_artists_ids = (artwork["ConstituentID"])
        artwork_artists_ids = (artwork_artists_ids.replace("[" , "")).replace("]" , "")
        list_artwork_artists_ids = (artwork_artists_ids.split(","))
        int_list_artwork_artists_ids = []
        for id_artist_str in list_artwork_artists_ids:
            int_list_artwork_artists_ids.append(int(id_artist_str))
        for each_id in int_list_artwork_artists_ids:
            for j in range(1 , lt.size(artists) + 1):
                artist = lt.getElement(artists , j)
                artist_id = int(artist["ConstituentID"])
                if each_id == artist_id:
                    nationality = artist["Nationality"]
                    lt.addLast(dict_countries[nationality] , artwork)
        
    return dict_countries


def rank_countries(dict_countries):
    dict_countries_2 = {}
    for country in dict_countries:
         dict_countries_2[country] = lt.size(dict_countries[country])

    return dict_countries_2

def order_rank_countries(dict_countries_ranked):
    list_countries = list(dict_countries_ranked.items())
    list_countries.sort(key=lambda x:x[1])


    return list_countries