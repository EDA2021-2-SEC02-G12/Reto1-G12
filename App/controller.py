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
 """

import config as cf
import model
import csv
import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(tad_list_type):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(tad_list_type)
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtworks(catalog)
    loadArtists(catalog)


def loadArtworks(catalog):
    """
    Carga las obras de arte del archivo.  Por cada obra de arte se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia a la obra de arte que se esta procesando.
    """
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def loadArtists(catalog):
    """
    Carga todos los artistas del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

# Funciones de ordenamiento

def sort_adquisitions_date(catalog, algo_type , initial_date , final_date):
    """
    Ordena las obras de arte por fecha de adquisición
    """
    return model.sort_adquisitions_date(catalog, algo_type , initial_date , final_date)

def sort_artist_date(catalog , algo_type , initial_year , final_year):
    """
    Ordena las obras de arte por fecha de adquisición
    """
    return model.sort_artist_date(catalog, algo_type , initial_year , final_year)


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def purchase_artworks(catalog , initial_date , final_date):

    return model.purchase_artworks(catalog , initial_date , final_date)

def find_artists(catalog , id2):

    return model.find_artists(catalog , id2)