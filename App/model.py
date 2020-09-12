"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de peliculas
# -----------------------------------------------------
def newCatalog():
    """ Inicializa el catálogo de peliculas

    Crea una lista vacia para guardar todos los peliculas

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'Movies': None,
               'production_companies': None,
               'directors': None,
               'actors': None,
               'actor_director': None,
               'genres': None,
               'production_countries': None}

    catalog['Movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog["MoviesId"] = mp.newMap(2000,
                                    maptype='PROBING', # No entiendo
                                    loadfactor=0.4,  # No entiendo
                                    comparefunction=compareMapMoviesIds) #No entiendo
    catalog['production_companies'] = mp.newMap(2000,
                                                maptype='PROBING',  # Esto no lo entiendo
                                                loadfactor=0.4,    #Esto no lo entiendo
                                                comparefunction=compareCompanies) #Esto lo entiendo mas pero tampoco lo entiendo
    catalog['directors'] = mp.newMap(2000,
                                         maptype='PROBING', #No lo entiendo
                                         loadfactor=0.4, #No entiendo
                                         comparefunction=compareDirectorsByName) #No entiendo
    catalog['actors'] = mp.newMap(2000,
                                      maptype='CHAINING', #No entiendo
                                      loadfactor=0.7, #No entiendo
                                      comparefunction=compareActorsByName) # No entiendo
    catalog['genres'] = mp.newMap(2000,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareByGenre)
    catalog['production_countries'] = mp.newMap(2000,
                                                maptype='CHAINING',
                                                loadfactor=0.7,
                                                comparefunction=compareCountries)
    """                                           
    catalog['actor_director'] = mp.newMap(2000,
                                          maptype='CHAINING',
                                          loadfactor=0.7,
                                          comparefunction=compareActorByDirector)
    """
    return catalog

def newCompany(name):
    company = {"name": "", "movies": None, "average_rating": 0}
    company["name"] = name
    company["movies"] = lt.newList("SINGLE_LINKED", compareCompanies)
    return company

def newDirector(name):
    """
    Crea una nueva estructura para modelar las películas 
    de un director y su promedio de ratings
    """
    director = {'name': "", "movies": None,  "average_rating": 0}
    director['name'] = name
    director['movies'] = lt.newList('SINGLE_LINKED', compareDirectorsByName)
    return director   

def newActor(actor):
    actor = {"name": "", "movies": None, "average_rating": 0}
    actor["name"] = actor
    actor["movies"] = lt.newList("SINGLE_LINKED", compareActorsByName)
    return actor

def newGenre(genre):
    """
    Esta funcion crea la estructura de libros asociados
    a un año.
    """
    entry = {'genre': "", "movies": None}
    entry['genre'] = genre
    entry["movies"] = lt.newList('SINGLE_LINKED', compareByGenre)
    return entry

def newCountry(country):
    entry = {"country": "", "movies": None}
    entry["country"] = country
    entry["movies"] = lt.newList("SINGLE_LINKED", compareCountries)
    return entry

# Funciones para agregar informacion al catalogo

def addMovie(catalog, movie, casting):
    lt.addLast(catalog["Movies"], movie)
    mp.put(catalog["MoviesId"], movie["id"], movie)
    addMovieGenre(catalog,movie)
    addMovieCompany(catalog, movie)
    addMovieDirector(catalog, movie, casting)
    addMovieActor(catalog, movie, casting)
    addMovieActorByDirector(catalog, casting)

def addMovieCompany(catalog, movie):
    mapa = catalog["production_companies"]
    company = movie["production_companies"]
    existcompany = mp.contains(mapa, company)
    if existcompany:
        entry = mp.get(mapa,company)
        comp = me.getValue(entry)
    else:
        comp = newCompany(company)
        mp.put(mapa, company, comp)
    lt.addLast(comp["movies"], movie)

    compavg = company['average_rating']
    movieavg = movie['average_rating']
    if (comphavg == 0.0):
        company['average_rating'] = float(movieavg)
    else:
        company['average_rating'] = (compavg + float(movieavg)) / 2

def addMovieDirector(catalog, details, casting):
    mapa = catalog["directors"]
    director = casting["director_name"]
    existdirector = mp.contains(mapa, director)
    if existdirector:
        entry = mp.get(mapa, director)
        comp = me.getValue(entry)
    else:
        comp = newDirector(director)
        mp.put(mapa, director, comp)
    lt.addLast(comp["movies"], details)

def addMovieActor(catalog, details, casting):
    mapa = catalog["actors"]
    actors = [casting["actor1_name"],casting["actor2_name"],casting["actor3_name"],casting["actor4_name"],casting["actor5_name"]]
    for actor in actors:
        existActor = mp.contains(mapa, actor)
        if existActor:
            entry = mp.get(mapa,actor)
            comp = me.getValue(entry)
        else:
            comp = newActor(actor)
            mp.put(mapa,actor, comp)
        lt.addLast(comp["movies"], details)

def addMovieGenre(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    mapa = catalog['genres']
    genres = movie['genres'].split("|")
    for genre in genres:
        existgenre = mp.contains(mapa, genre)
        if existgenre:
            entry = mp.get(mapa, genre)
            genero = me.getValue(entry)
        else:
            genero = newGenre(genre)
            mp.put(mapa, genre, genero)
        lt.addLast(genero["movies"], movie)
    

def addMovieCountry(catalog, movie):
    mapa = catalog["production_countries"]
    country = movie["production_countries"]
    existcountry = mp.contains(mapa, country)
    if existcountry:
        entry = mp.get(mapa,country)
        comp = me.getValue(entry)
    else:
        comp = newCountry(country)
        mp.put(mapa, country, comp)
    lt.addLast(comp["movies"], movie)


def addMovieActorByDirector(catalog,casting):
    mapa = catalog["actor_director"]
    actors = [casting["actor1_name"],casting["actor2_name"],casting["actor3_name"],casting["actor4_name"],casting["actor5_name"]]
    for actor in actors:
        existActor = mp.contains(mapa, actor)
        if existActor:
            entry = mp.get(mapa,actor)
            comp = me.getValue(entry)
        else:
            comp = newActor(actor)
            mp.put(mapa,actor, comp)
        lt.addLast(comp["movies"], casting)
    
# ==============================
# Funciones de consulta
# ==============================

def moviesSize(catalog):
    """Numero de películas
    """
    return lt.size(catalog["movies"])


def directorsSize(catalog):
    """Numero de directores leido
    """
    return lt.size(catalog["directors"])


def actorsSize(catalog):
    """Numero de actores leido
    """
    return lt.size(catalog["actors"])

def listsize(movies):
    return lt.size(movies)

  
def getMoviesByProductionCompany(catalog,ProductionCompanyName):
    productioncompany=mp.get(catalog["production_companies"],ProductionCompanyName)
    if productioncompany:
        return me.getValue(productioncompany)
    return None


def getMoviesByDirector(catalog, directorname):
    """
    Retorna las películas de un director
    """
    director=mp.get(catalog["directors"],directorname)
    if director:
        return me.getValue(director)

    return None


def getMoviesByActor(catalog, actorname):
    """
    Retorna las películas de un actor
    """
    actor=mp.get(catalog["actors"],actorname)
    if actor:
        return me.getValue(actor)
    return None


def getMoviesByGenre(catalog, genrename):
    """
    Retorna las películas de un género
    """
    genre=mp.get(catalog["genres"],genrename)
    if genre:
        return me.getValue(genre)
    return None


def getMoviesByCountry(catalog, countryname):
    """
    Retorna las películas de un país
    """
    country=mp.get(catalog["production_countries"],countryname)
    if country:
        return me.getValue(country)
    return None

# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(id1, id2):
    """
    Compara dos ids de películas
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def compareMapMoviesIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1
def compareCompanies(keyname,company):
    companyentry=me.getKey(company)
    if keyname==companyentry:
        return 0
    elif keyname > companyentry:
        return 1
    else:
        return -1
def compareDirectorsByName(keyname,director):
    directorentry=me.getKey(director)
    if keyname==directorentry:
        return 0
    elif keyname > directorentry:
        return 1
    else:
        return -1

def compareActorsByName(keyname,actor):
    actorentry=me.getKey(actor)
    if keyname==actorentry:
        return 0
    elif keyname > actorentry:
        return 1
    else:
        return -1
    return 0     

def compareByGenre(keyname,genre):
    genreentry=me.getKey(genre)
    if keyname==genreentry:
        return 0
    elif keyname > genreentry:
        return 1
    else:
        return -1
    
def compareCountries(keyname,country):
    countryentry=me.getKey(country)
    if keyname==countryentry:
        return 0
    elif keyname > countryentry:
        return 1
    else:
        return -1
