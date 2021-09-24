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

def find_id_of_artist(catalog , artist_name):
    #REQUISITO 3

    return model.find_id_of_artist(catalog , artist_name)

def list_of_artworks(catalog , id):
    #REQUISITO 3

    return model.list_of_artworks(catalog , id)

def list_of_tecniques(list_of_artworks):
    #REQUISITO 3

    return model.list_of_tecniques(list_of_artworks)

def most_used_technique(list_of_techniques):
    #REQUISITO 3

    return model.most_used_technique(list_of_techniques)

def list_of_most_used_tecnique(most_used_tecnique , list_of_artworks):
    #REQUISITO 3

    return model.list_of_most_used_tecnique(most_used_tecnique , list_of_artworks)

#Funciones Requisito 4

def country_list(catalog):
    return model.country_list(catalog)

def country_list_sorted(country_list , algo_type):
    return model.country_list_sorted(country_list , algo_type)

def newDict_countries(country_list_sorted):
    return model.newDict_countries(country_list_sorted)

def insert_artworks(catalog , dict_countries):
    return model.insert_artworks(catalog , dict_countries)

def rank_countries(dict_countries):
    return model.rank_countries(dict_countries)

def order_rank_countries(dict_countries_ranked):
    return model.order_rank_countries(dict_countries_ranked)