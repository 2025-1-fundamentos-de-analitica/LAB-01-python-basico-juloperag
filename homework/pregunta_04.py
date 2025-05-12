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
        data = line["col2"].split("-")
        sequence.append((data[1], 1))
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



def pregunta_04(): 
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    #Ejecucion de funciones      
    sequence = load_input("./files/input/data.csv")
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    #Retorno secuencia
    return sequence

