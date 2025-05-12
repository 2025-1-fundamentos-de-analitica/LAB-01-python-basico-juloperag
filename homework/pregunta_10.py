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
        sequence.append((line["col0"], line["col3"], line["col4"]))
    return sequence

def mapper(sequence):
    """Mapper"""
    #Se queda solamente con los elementos categoricos de la columna 5
    return [(key, seq_1, [value.split(":")[0] for value in seq_2]) for key, seq_1, seq_2 in sequence]

def reducer(sequence):
    """Reducer"""
    result = []
    #Se calcula la cantidad de elementos
    for key, seq_1, seq_2 in sequence: 
        result.append((key, len(seq_1), len(seq_2)))
    return result

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
   #Ejecucion de funciones      
    sequence = load_input("./files/input/data.csv")
    sequence = mapper(sequence)
    sequence = reducer(sequence)
    #Retorno secuencia
    return sequence


