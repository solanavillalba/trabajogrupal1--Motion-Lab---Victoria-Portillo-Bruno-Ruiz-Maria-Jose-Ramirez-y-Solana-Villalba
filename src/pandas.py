 
 
 
 
 
 
 
#metricas
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