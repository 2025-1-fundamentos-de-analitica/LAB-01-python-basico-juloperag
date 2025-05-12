def parse_file_to_dict(dir_file):
    result = []
    #Abrimos el archivo
    with open(dir_file, "r") as f:
        #Recorremos cada linea del archivo
        for line in f:
            #Eliminacion de espacios y separacion de elementos  
            parts = line.strip().split("\t")
            #Separacion de cada columna
            entry = {
                "col0" : parts[0],
                "col1" : int(parts[1]),
                "col2" : parts[2],
                "col3" : parts[3].split(","),
                "col4" : parts[4].split(",")
            }
            #Agregar diccionario 
            result.append(entry)

    return result 