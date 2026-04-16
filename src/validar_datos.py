def validar_datos(valor, tipo):
    """
    Valida si el str que ingreso el usuario puede ser casteado al tipo de variable que quiere.
    
    Parámetros:
    valor: str
    Elemento que quiere ver si se puede castear

    tipo: str (int/float/bool)
    Tipo al que se quiere castear el valor, tiene que ser escrito de la manera especificada y en minuscula.

    Retorna:
        bool
    False si no se puede castear o True si sí
    """

    if tipo == "bool":
        if (valor.lower() != "true") and (valor.lower() != "false"):
            raise ValueError ("Error casteando booleano")
        
    elif tipo == "int":
        try:
            validacion= int(valor)
        except:
            raise ValueError ("Error casteando int")
        
    elif tipo == "float":
        try:
            valido= float(valor)
        except:
            raise ValueError ("Error casteando float")
    else:
        raise ValueError("Mal usada la funcion")
    return None


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

    Retorna:
        bool
    Devuelve si esta dentro del rango o no.
    """
    
    if incluido == True:
        if minimo<=numero and numero<=maximo:
            return True
        else:
            raise ValueError("Error, numero fuera de rango")
    else:
        if minimo<numero and numero<maximo:
            return True
        else:
            raise ValueError("Error, numero fuera de rango")
        
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

    Retorna:
    lista : list / falso: bool (si no se pudo castear)
    Es la lista con los elementos ya convertidos, pero si no se pudieron castear los datos devuelve False.

    '''
    lista = datos.split(",")
    if len(lista)!=6:
        raise ValueError("Error de longitud en la linea")
    
    try:
        validar_datos(lista[0], "int")
        validar_datos(lista[1], "float")
        numero_en_rango(float(lista[1]), True, 0)
        validar_datos(lista[2], "float")
        numero_en_rango(float(lista[2]), True, 0)
        validar_datos(lista[3], "float")
        numero_en_rango(float(lista[3]), True, 0)
        validar_datos(lista[4], "bool")
    except ValueError as e:
        raise ValueError (e)   
    else:
        lista[0] = int(lista[0])
        lista[1] = float(lista[1])
        lista[2] = float(lista[2])
        lista[3] = float(lista[3])
        if (lista[4].lower() == "true"):
            lista[4]= True
        else:
            lista[4]= False
        return lista
