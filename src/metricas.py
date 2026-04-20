def calcular_tiempo_primer_hit(datos):
    """
    Devuelve el primer tiempo del participante seleccionado.
    
    Parámetros:
    datos : dict
    Diccionario de un participante que contiene:
    "ID", "tiempo", "hit", "x", "y", "condicion"
        
    Retorna:
    tiempo_actual: float
    Es el primer tiempo donde hubo un hit.
    primer_tiempo: str  
    En caso de no haber hits, devuelve: "No hizo ningún hit".

    """

#Incializador variable

    primer_tiempo = "No hizo ningún hit"

    for i in range(len(datos["hit"])):
         hit_actual = datos["hit"][i]
         tiempo_actual = datos["tiempo"][i]
         if hit_actual == True:
                return tiempo_actual
    
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
    
    Raises:
    ZeroDivisionError: "El ultimo tiempo es 0"
        En caso de que el ultimo tiempo sea 0, ya que no se podra usar como cociente.
    
    '''
    tiempo_ultimo = diccio['tiempo'][-1]
    if tiempo_ultimo==0:
        raise ZeroDivisionError("El ultimo tiempo es 0")
    
    hits_totales = calcular_hits_totales(diccio)
    promedio = round(hits_totales/tiempo_ultimo)
    return promedio