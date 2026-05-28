 def calcular_tiempo_primer_hit(dataframe,id):
    '''
    Devuelve el primer tiempo en el que ocurrió un hit entre todos los participantes.
    Parámetros:
    dataframe: dataframe con las siguientes columnas: "ID", "tiempo", "hit", "x", "y", "condicion".
    id: participante a conseguir su primer tiempo.

    Retorna:
    int | float | None :el primer tiempo del participante (haya tenido o no)

    '''
    mascara=(dataframe["hit"]==True) & (dataframe["ID"]==id)
    filtrado=dataframe[mascara]
    return filtrado.iloc[0]['tiempo']


def calcular_hits_totales(diccio):
    '''
    Calcula la cantidad de hits que tuvo el participante.

    Parámetros:
    diccio: dict
        Diccionario del participante a extraer los datos de los hits.
    
    Retorna:
    contador: int
        Cantidad de hits que tuvo el participante.
    
    '''
    contador=0
    for hit in diccio['hit']:
        if hit==True:
            contador+=1
    return contador

def calcular_promedio(diccio):
    '''
    Calcula el promedio entre el tiempo y la cantidad total de hits del participante.

    Parámetros:
    diccio: dict
        Diccionario del participante con la información para calcular el promeido (tiempo y hits).
    
    Retorna:
    promedio: float False:bool
        Promedio del participante entre el tiempo y la cantidad total de
             hits, False si el ultimo tiempo es 0.
    Raises: 
    ZeroDivisionError:
        Ocurre cuando el último tiempo ingresado es el numero 0. 
    '''
    tiempo_ultimo = diccio['tiempo'][-1]
    if tiempo_ultimo==0:
        raise ZeroDivisionError("El ultimo tiempo es 0")
    
    hits_totales = calcular_hits_totales(diccio)
    promedio = round(hits_totales/tiempo_ultimo)
    return promedio