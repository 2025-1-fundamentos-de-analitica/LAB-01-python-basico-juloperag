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
    #Se crea tuplas (letra,1) por cada fila, donde la letra sera la correspondiente al elemento de la columna 1
    sequence = []
    for line in array_dir: 
        sequence.append((line["col0"], 1))
    return sequence
    
def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    #Se ordenan las tuplas por orden alfabetico
    return sorted(sequence, key=lambda x: x[0])

def reducer(sequence):
    """Reducer"""
    result = []
    #Se agrupan los elemento iguales 
    for key, group in groupby(sequence, lambda x: x[0]):
        result.append((key, sum(value for _, value in group)))
    return result


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """          
    #Ejecucion de funciones      
    sequence = load_input("./files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    #Retorno secuencia
    return sequence
