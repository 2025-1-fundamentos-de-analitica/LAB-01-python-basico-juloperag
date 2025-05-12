"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    total = 0
    with open("./files/input/data.csv", "r") as f:
        for line in f:
            #Eliminacion espacios en blanco
            line = line.strip()
            #Divide la linea 
            fields = line.split("\t")
            #Suma la segunda columna
            total += int(fields[1])
    return total

#if __name__ == "__main__":
    #value = pregunta_01()
    #print(value)