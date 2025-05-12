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
        sequence.append((line["col0"], line["col4"]))
    return sequence

def mapper(sequence):
    """Mapper"""
    #Aplicacion de Mapper 
    return [(value_1, sum(int(value.split(":")[1]) for value in seq_1)) for value_1, seq_1 in sequence]

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


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    #Ejecucion de funciones      
    sequence = load_input("./files/input/data.csv")
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    #Retorno secuencia
    return sequence
