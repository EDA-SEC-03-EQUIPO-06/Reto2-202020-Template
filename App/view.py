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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller as controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

Casting = "themoviesdb/MoviesCastingRaw-small.csv"
Details = "themoviesdb/SmallMoviesDetailsCleaned.csv"

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
def printinfo(lst):
    print("Se cargaron "+ str(controller.detailsSize(lista_details))+" películas")
    print("\nInformación Primera Película\n ")
    primer_elemento =controller.getFirstElement(lst)
    print("Título: " + controller.getTitle(primer_elemento))
    print("Fecha de estreno: " + controller.getDate(primer_elemento))
    print("Promedio de votación: " + controller.getAverage(primer_elemento))
    print("Numero de votos: " + controller.getVotes(primer_elemento))
    print("Idioma de la película: " + controller.getLang(primer_elemento))
    print("\nInformación Última Película\n")
    ultimo_elemento = controller.getLastElement(lst)
    print("Título: " + controller.getTitle(ultimo_elemento))
    print("Fecha de estreno: " + controller.getDate(ultimo_elemento))
    print("Promedio de votación: " + controller.getAverage(ultimo_elemento))
    print("Número de votos: " + controller.getVotes(ultimo_elemento))
    print("Idioma de la película: " + controller.getLang(ultimo_elemento))
    print("\n")


def printMenu():
    print("Opción 1: Cargar Archivos")
    print("Opción 2: Requerimiento 1")
    print("Opción 3: Requerimiento 2")
    print("Opción 4: Requerimiento 3")
    print("Opción 5: Requerimiento 4")
    print("Opción 6: Requerimiento 5")
    print("Opción 7: Salir")
    


# ___________________________________________________
#  Menu principal
# ___________________________________________________
while True:
    
    lista_details = controller.newListDetails()
    printMenu()
    inputs = input("Selecciones una opción para continuar\n")

    if int(inputs[0]) == 1:
        print("Cargando Archivos...")
        controller.loadDetails(lista_details, Details)
        printinfo(lista_details)
        
    elif int(inputs[0]) == 2:
        print(0)
    elif int(inputs[0]) == 3:
        print(0)
    elif int(inputs[0]) == 4:
        print(0)
    elif int(inputs[0]) == 5:
        print(0)
    elif int(inputs[0]) == 6:
        print(0)
    else:
        sys.exit(0)
sys.exit()





