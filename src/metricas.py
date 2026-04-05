def calcular_tiempo_primer_hit(datos):
"""
Devuelve el primer tiempo en el que ocurrió un hit entre todos los participantes.
    
    Parámetros:
    datos : list
        Lista de diccionarios, cada diccionario contiene:
        "ID", "tiempo", "hit", "x", "y", "condicion"
    
    Returns:
    float
        Primer tiempo donde hubo un hit, o None si no hay hits.
    """
#Incializador variable

primer_tiempo = None
 for participante in datos:
    for i in range(len(participante["hit"])):
         hit_actual = participante["hit"][i]
         tiempo_actual = participante["tiempo"][i]
        if hit_actual == True:
           if primer_tiempo is None:
                    primer_tiempo = tiempo_actual
                elif tiempo_actual < primer_tiempo:
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
    promedio: float
    Promedio del participante entre el tiempo y la cantidad total de hits.
    
    '''
    tiempo_ultimo = diccio['tiempo'][-1]
    hits_totales = calcular_hits_totales(diccio)
    promedio = hits_totales/tiempo_ultimo
    return promedio