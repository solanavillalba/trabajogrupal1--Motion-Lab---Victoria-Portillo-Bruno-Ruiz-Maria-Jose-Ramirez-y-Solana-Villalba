

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
            if lista[0] not in lista_id:
                par={"ID": 0, "tiempo":[], "x":[], "y":[], "hit":[], "condicion": "" }
            
                par["ID"]= lista[0]
                par["tiempo"].append(lista[1])
                par["x"].append(lista[2])
                par["y"].append(lista[3])
                par["hit"].append(lista[4])
                par["condicion"]= lista[5]
                lista_con_diccionario.append(par)
                lista_id.append(lista[0])
            else:
                for dicc in lista_con_diccionario:
                    if dicc["ID"]==lista[0]:    
                        dicc["tiempo"].append(lista[1])
                        dicc["x"].append(lista[2])
                        dicc["y"].append(lista[3])
                        dicc["hit"].append(lista[4])
    return lista_con_diccionario