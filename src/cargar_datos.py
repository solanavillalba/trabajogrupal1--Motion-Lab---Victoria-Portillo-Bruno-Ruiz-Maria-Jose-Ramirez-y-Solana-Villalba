

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
    """
    try:
        archivo = open(ruta, "r")
    except FileNotFoundError:
        raise FileNotFoundError("No se pudo abrir el archivo")
    
    columna = archivo.readline()
    lineas = archivo.readlines()
    archivo.close()
    
    lista_lineas=[]
    
    for linea in lineas:
        lista_lineas.append(linea.strip())

    lista_valores=[]
    contador_posicion=1
    
    for string in lista_lineas:
        try:
            v.parsear_linea(string)
        except Exception as e:
            print(f"{e} de la fila numero {contador_posicion}, se eliminio el dato del analisis")  
            contador_posicion+=1
        else:
            lista_valores.append(v.parsear_linea(string))
            contador_posicion+=1


    lista_con_diccionario=[]
    
    while True:
        if len(lista_valores)==0:
            break

        buscar=lista_valores[0][0]
        datos_del_participante=[]

        for posicion in range(len(lista_valores)):
            if lista_valores[posicion][0]==buscar:
                datos_del_participante.append(lista_valores[posicion])
       
        participante={"ID": 0, "tiempo":[], "x":[], "y":[], "hit":[], "condicion": "" }

        for dato in datos_del_participante:
            lista_valores.remove(dato)
            participante["ID"]= dato[0]
            participante["tiempo"].append(dato[1])
            participante["x"].append(dato[2])
            participante["y"].append(dato[3])
            participante["hit"].append(dato[4])
            participante["condicion"]= dato[5]
            
        lista_con_diccionario.append(participante)
    """
    lista_con_diccionario=[]
    lista_id=[]
    while True:
        for dato in lista_valores:
            if dato[0] not in lista_id:
                par={"ID": 0, "tiempo":[], "x":[], "y":[], "hit":[], "condicion": "" }
                
                par["ID"]= dato[0]
                par["tiempo"].append(dato[1])
                par["x"].append(dato[2])
                par["y"].append(dato[3])
                par["hit"].append(dato[4])
                par["condicion"]= dato[5]
                lista_con_diccionario.append(par)
                lista_id.append(dato[0])

            else:
                for dicc in lista_con_diccionario:
                    if dicc["ID"]==dato[0]:    
                        dicc["tiempo"].append(dato[1])
                        dicc["x"].append(dato[2])
                        dicc["y"].append(dato[3])
                        dicc["hit"].append(dato[4])
                


       
        participante={"ID": 0, "tiempo":[], "x":[], "y":[], "hit":[], "condicion": "" }

        for dato in datos_del_participante:
            lista_valores.remove(dato)
            participante["ID"]= dato[0]
            participante["tiempo"].append(dato[1])
            participante["x"].append(dato[2])
            participante["y"].append(dato[3])
            participante["hit"].append(dato[4])
            participante["condicion"]= dato[5]
            
        lista_con_diccionario.append(participante)
            
    """

    return lista_con_diccionario