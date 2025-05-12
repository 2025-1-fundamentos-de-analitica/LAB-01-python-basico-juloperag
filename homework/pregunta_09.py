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
    #Se crea tuplas (letra,1) por cada fila
    sequence = []
    for line in array_dir:
        for k,_ in (item.split(":") for item in line["col4"]):
            sequence.append((k,1))
    return sequence

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


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    #Ejecucion de funciones      
    sequence = load_input("./files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    #Retorno secuencia
    return sequence

