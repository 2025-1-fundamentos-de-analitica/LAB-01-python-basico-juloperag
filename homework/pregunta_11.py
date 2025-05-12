"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from .util import parse_file_to_dict as pdict
from itertools import groupby

def load_input(input_directory):
    #Se carga el archivo y se genera un array de diccionarios por cada linea del mismo
    array_dir = pdict(input_directory)
    #Se crea tuplas (letra,numero) por cada fila
    sequence = []
    for line in array_dir: 
        sequence.append((line["col3"], line["col1"]))
    return sequence

def mapper(sequence):
    """Mapper"""
     #Aplicacion de Mapper 
    return [(value_2, value_1) for seq_1, value_1 in sequence for value_2 in seq_1]

def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    #Se ordenan las tuplas por orden alfabetico
    return sorted(sequence, key=lambda x: x[0])

def reducer(sequence):
    """Reducer"""
    result = {}
    #Se agrupan los elemento iguales 
    for key, group in groupby(sequence, lambda x: x[0]):
        result[key] = sum(value for _, value in group)
    return result


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    #Ejecucion de funciones      
    sequence = load_input("./files/input/data.csv")
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    #Retorno secuencia
    return sequence
