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
        for k,v in (item.split(":") for item in line["col4"]):
            sequence.append((k,int(v)))
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
        list_value = [value for _, value in group]
        result.append((key, min(list_value), max(list_value)))
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    #Ejecucion de funciones      
    sequence = load_input("./files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    #Retorno secuencia
    return sequence

