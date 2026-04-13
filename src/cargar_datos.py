def validar_datos(valor, tipo):
    """
    Valida si el str que ingreso el usuario puede ser casteado al tipo de variable que quiere.
    
    Parámetros:
    valor: str
    Elemento que quiere ver si se puede castear

    tipo: str (int/float/bool)
    Tipo al que se quiere castear el valor, tiene que ser escrito de la manera especificada y en minuscula.

    Returns:
    resultado: bool
    False si no se puede castear o True si sí
    """

    if tipo == "bool":
        if (valor.lower() == "true") or (valor.lower() == "false"):
            return True
        else:
            return False
        
    if tipo == "int":
        try:
            validacion= int(valor)
        except:
            return False
        else:
            return True

    if tipo == "float":
        try:
            valido= float(valor)
        except:
            return False
        else:
            return True

def numero_en_rango(numero, incluido, minimo=-float('inf'), maximo=float('inf')):

    """
    Verifica si el numero de entrada esta dentro del rango o no.

    Parámetros:
    numero : int/float
    Numero para verificar
    
    incluido : Bool
    Si queres que el minimo y maximo se incluya en el rango o no.
    minimo : int/float
    Minimo del rango (Si no se especifica, no se utiliza)

    maximo: int/float
    Maximo del rango (Si no se especifica, no se utiliza)

    Returns:
    Respuesta : bool
    Devuelve si esta dentro del rango o no.
    """
    
    if incluido == True:
        if minimo<=numero and numero<=maximo:
            return True
        else:
            return False
    else:
        if minimo<numero and numero<maximo:
            return True
        else:
            return False
        
def parsear_linea(datos):
    '''
    Convierte los datos suministrados en el tipo de dato 
    requerido para su analisis posterior.
    Estos datos requieren de un orden previo
    para poder ser correctamente clasificados.
    Este es: "id; tiempo; x; y; hit; condicion".
    Esta función devolvera una lista de datos con su tipo de dato requerido.

    Parámetros:
    datos : str
    Son los elementos de los cuales se convertira su tipo de datos.

    Returns:
    lista : list / falso: bool (si no se pudo castear)
    Es la lista con los elementos ya convertidos, pero si no se pudieron castear los datos devuelve False.

    '''
    lista = datos.split(",")
    if len(lista)!=6:
        return "Error de longitud en la linea"
    
    if validar_datos(lista[0], "int") == True:
        lista[0] = int(lista[0])
    else:
        return "Error casteando el ID"
    
    if validar_datos(lista[1], "float") and numero_en_rango(float(lista[1]), True, 0):
        lista[1] = float(lista[1])
    else:
        return "Error casteando el Tiempo"
        
    if validar_datos(lista[2], "float") and numero_en_rango(float(lista[2]), True, 0):
        lista[2] = float(lista[2])
    else:
        return "Error casteando la posición X"
        
    if validar_datos(lista[3], "float") and numero_en_rango(float(lista[3]), True, 0):
        lista[3] = float(lista[3])
    else:
        return "Error casteando la Posición Y"
        
    if validar_datos(lista[4], "bool"):
        if (lista[4].lower() == "true"):
            lista[4]= True
        else:
            lista[4]= False
    else:
        return "Error casteando el Hit"
        
    return lista



def cargar_datos(ruta): 
    """
    Abre un archivo de Motion Lab y ordena los datos por participante.
    
    Parámetros
    ----------
    Ruta : string
    Ruta por donde se puede acceder al archivo.
    Retorna
    Datos: Lista de dicionarios
    Lista con diccionarios, cada diccionario corresponde a un participantes con sus datos (ID, Tiempo, x, y, hit y condición). Si no se pudieron castear los valores de alguna lista, se informara.
    """
    try:
        archivo = open(ruta, "r")
    except:
        return "No se pudo abrir el archivo"
    
    columna = archivo.readline()
    lineas = archivo.readlines()
    archivo.close()
    
    lista_lineas=[]
    
    for linea in lineas:
        lista_lineas.append(linea.strip())

    lista_valores=[]
    contador_posicion=1
    
    for string in lista_lineas:
        if type(parsear_linea(string)) == list:
            lista_valores.append(parsear_linea(string))
            contador_posicion+=1
        else:
            print(f"{parsear_linea(string)} de la fila numero {contador_posicion}, se eliminio el dato del analisis")
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
       
        participante={}

        for dato in datos_del_participante:
            lista_valores.remove(dato)
            
            if "ID" not in participante:
                participante["ID"]= dato[0]
            
            if "tiempo" not in participante:
                participante["tiempo"]= [dato[1]]
            else:
                participante["tiempo"].append(dato[1])
            
            if "x" not in participante:
                participante["x"]= [dato[2]]
            else:
                participante["x"].append(dato[2])
            
            if "y" not in participante:
                participante["y"]= [dato[3]]
            else:
                participante["y"].append(dato[3])
            
            if "hit" not in participante:
                participante["hit"]= [dato[4]]
            else:
                participante["hit"].append(dato[4])
        
            if "condicion" not in participante:
                participante["condicion"]= dato[5]
        
        lista_con_diccionario.append(participante)
            

    return lista_con_diccionario


