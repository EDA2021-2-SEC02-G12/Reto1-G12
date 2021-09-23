"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import sys
import datetime

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 1000 
sys.setrecursionlimit(default_limit*10)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronologicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento ")
    print("7- Proponer una nueva exposición en el museo")

def initCatalog(tad_list_type):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(tad_list_type)

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

def printSortResults_artworks(ord_artworks, purchased , catalog , sample=3): 
    size = lt.size(ord_artworks)
    if size > sample:
        print("El numero de obras compradas dentro del rango seleccionado es: " + str(purchased))
        print("Las primeros ", sample, " obras de arte son:") 
        i=1
        while i <= sample:
            artwork = lt.getElement(ord_artworks,i)
            
            id = (artwork["ConstituentID"][1: len(artwork["ConstituentID"])-1]).split(',')
            id2 = []
            for element in id:
                int_element = int(element)
                id2.append(int_element)
            
            artist_list = controller.find_artists(catalog , id2)
            artists_str = ""
            for each_artist in artist_list:
                artists_str = artists_str + str(each_artist)

            print('Titulo: ' + artwork["Title"] + " Artista(s): "  + artists_str + ' Fecha: ' +
                  artwork["Date"] + ' Medio: ' + artwork["Medium"] +  'Dimensiones' + artwork["Dimensions"]) 
            i+=1
        print("Las ultimas 3 obras de arte son: ")
        i = lt.size(ord_artworks) - 2
        while i <= lt.size(ord_artworks):
            artwork = lt.getElement(ord_artworks,i)

            id = (artwork["ConstituentID"][1: len(artwork["ConstituentID"])-1]).split(',')
            id2 = []
            for element in id:
                int_element = int(element)
                id2.append(int_element)
            
            artist_list = controller.find_artists(catalog , id2)
            artists_str = ""
            for each_artist in artist_list:
                artists_str = artists_str + str(each_artist)


            print('Titulo: ' + artwork["Title"] + " Artista(s) " + artists_str + ' Fecha: ' +
                  artwork["Date"] + ' Medio: ' + artwork["Medium"] +  'Dimensiones' + artwork["Dimensions"])  
            i+=1
    else:
        print(size)
        print("El tamaño de la muestra excede el número de obras de arte.")


def printSortResults_artists(ord_artists, sample=3): 
    size = lt.size(ord_artists)
    if size > sample:
        print("Las primeros ", sample, " artistas son:") 
        i=1
        while i <= sample:
            artist = lt.getElement(ord_artists,i)
            print('Nombre: ' + artist["DisplayName"] + ' Fecha de Nacimiento: ' +
                  artist["BeginDate"] + ' Año de Fallecimiento: ' + artist["EndDate"] +  ' Nacionalidad: ' + artist["Nationality"] +  ' Género: ' + artist["Gender"]) 
            i+=1
        print("Los ultimos 3 artistas son: ")
        i = lt.size(ord_artists) - 2
        while i <= lt.size(ord_artists):
            artist = lt.getElement(ord_artists,i) 
            print('Nombre: ' + artist["DisplayName"] + ' Fecha de Nacimiento: ' +
                  artist["BeginDate"] + ' Año de Fallecimiento: ' + artist["EndDate"] +  ' Nacionalidad: ' + artist["Nationality"] +  ' Género: ' + artist["Gender"]) 
            i+=1
    else:
        print(size)
        print("El tamaño de la muestra excede el número de artistas.")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tad_int = int(input("Escriba 1 si desea usar Single Linked o 2 si desea usar Array List: "))
        print("Cargando información de los archivos ....")
        if tad_int == 1:
            tad_list_type = 'SINGLE_LINKED'
        elif tad_int == 2:
            tad_list_type = 'ARRAY_LIST'
        catalog = initCatalog(tad_list_type)
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))

    elif int(inputs[0]) == 2:
        initial_year = int(input("Ingrese el año incial: "))
        final_year = int(input("Ingrese el año final: "))
        algo_type = int(input("1- Insetion, 2 - Shell, 3 - Merge , 4 - Quick Sorts"))
        result = controller.sort_artist_date(catalog , algo_type , initial_year , final_year)

        print("Para la muestra de", "1" , " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        printSortResults_artists(result[1])

    elif int(inputs[0]) == 3:
        print("Ingrese los valores de fecha inicial: ")
        initial_year1 = int(input("Ingrese el año de la fecha inicial: "))
        initial_month1 = int(input("Ingrese el mes de la fecha inicial: "))
        initial_day1 = int(input("Ingrese el dia de la fecha inicial: "))
        print("Ingrese los valores de fecha final: ")
        initial_year2 = int(input("Ingrese el año de la fecha final: "))
        initial_month2 = int(input("Ingrese el mes de la fecha final: "))
        initial_day2 = int(input("Ingrese el dia de la fecha final: "))

        initial_date = [initial_year1 , initial_month1 , initial_day1]
        final_date = [initial_year2 , initial_month2 , initial_day2]

        algo_type = int(input("1- Insetion, 2 - Shell, 3 - Merge , 4 - Quick Sorts"))

        purchased = controller.purchase_artworks(catalog , initial_date , final_date)

        result = controller.sort_adquisitions_date(catalog, algo_type , initial_date , final_date)
        print("Para la muestra de", "1" , " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        printSortResults_artworks(result[1] , purchased , catalog)


    else:
        sys.exit(0)
sys.exit(0)
 