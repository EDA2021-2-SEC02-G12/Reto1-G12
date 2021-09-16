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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronologicamente las adquisiciones")
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

def printSortResults(ord_artworks, sample=10): 
    size = lt.size(ord_artworks)
    if size > sample:
        print("Las primeros ", sample, " obras de arte son:") 
        i=1
        while i <= sample:
            artwork = lt.getElement(ord_artworks,i) 
            print('Titulo: ' + artwork["Title"] + ' Fecha: ' +
                  artwork["Date"] + ' Medio: ' + artwork["Medium"] +  'Dimensiones' + artwork["Dimensions"]) 
            i+=1
    else:
        print(size)
        print("El tamaño de la muestra excede el número de obras de arte.")

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
        size = int(input("Indique el tamaño de la muestra: "))
        algo_type = int(input("1- Insetion, 2 - Shell, 3 - Merge , 4 - Quick Sorts"))
        result = controller.sort_adq(catalog, int(size) , algo_type)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        printSortResults(result[1])

    else:
        sys.exit(0)
sys.exit(0)
