

import src.validar_datos as v
def cargar_datos(ruta): 
    """
    Abre un archivo de Motion Lab y ordena los datos por participante.
    
    Parámetros
    ----------
    ruta : str
    Ruta por donde se puede acceder al archivo.
    Retorna
    lista_con_diccionario: list
    Lista con diccionarios, cada diccionario corresponde a un participantes con sus datos (ID, Tiempo, x, y, hit y condición). Si no se pudieron castear los valores de alguna lista, se informara.
    
    Raises:
    FileNotFoundError: Exception 
    Si no fue posible encontrar el archivo.

    ValueError: Exception
    Si no fue posible castear una linea.

    """
    try:
        archivo = open(ruta, "r")
    except FileNotFoundError:
        raise FileNotFoundError("No se pudo abrir el archivo")
    lineas = archivo.readlines()
    archivo.close()
    
    lista_con_diccionario=[]
    lista_id=[]
    contador_posicion=1


    for linea1 in lineas:
        linea=linea1.strip()
        try:
            lista=v.parsear_linea(linea)
        except Exception as e:
            raise ValueError(f"{e} de la fila numero {contador_posicion}, se corta el programa")  
        else:
            contador_posicion+=1
            if linea[0] not in lista_id:
                par={"ID": 0, "tiempo":[], "x":[], "y":[], "hit":[], "condicion": "" }
            
                par["ID"]= linea[0]
                par["tiempo"].append(linea[1])
                par["x"].append(linea[2])
                par["y"].append(linea[3])
                par["hit"].append(linea[4])
                par["condicion"]= linea[5]
                lista_con_diccionario.append(par)
                lista_id.append(linea[0])
            else:
                for dicc in lista_con_diccionario:
                    if dicc["ID"]==linea[0]:    
                        dicc["tiempo"].append(linea[1])
                        dicc["x"].append(linea[2])
                        dicc["y"].append(linea[3])
                        dicc["hit"].append(dato[4])
    return lista_con_diccionario