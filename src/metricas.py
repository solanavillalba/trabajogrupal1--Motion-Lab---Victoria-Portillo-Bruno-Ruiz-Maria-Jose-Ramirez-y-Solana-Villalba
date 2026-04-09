def calcular_tiempo_primer_hit(datos):
    """
    Devuelve el primer tiempo en el que ocurrió un hit entre todos los participantes.
    Parámetros:
    datos : list
    Lista de diccionarios, cada diccionario contiene:
    "ID", "tiempo", "hit", "x", "y", "condicion"
        
    Returns:
    resultado: float  No hizo ningún hit : Str
    Primer tiempo donde hubo un hit, o no hizo ningún hit si no hay hits.

    """

#Incializador variable

    primer_tiempo = "No hizo ningún hit"

    for i in range(len(datos["hit"])):
         hit_actual = datos["hit"][i]
         tiempo_actual = datos["tiempo"][i]
         if hit_actual == True:
                primer_tiempo = tiempo_actual
                return primer_tiempo






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
    Promedio del participante entre el tiempo y la cantidad total de hits, False si el ultimo tiempo es 0.
    
    '''
    tiempo_ultimo = diccio['tiempo'][-1]
    if tiempo_ultimo==0:
         return False
    
    hits_totales = calcular_hits_totales(diccio)
    promedio = round(hits_totales/tiempo_ultimo)
    return promedio