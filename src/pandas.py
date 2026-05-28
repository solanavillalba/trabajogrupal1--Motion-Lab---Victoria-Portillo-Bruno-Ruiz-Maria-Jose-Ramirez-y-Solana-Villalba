#metricas
<<<<<<< Updated upstream
 def calcular_tiempo_primer_hit(dataframe,id):
=======
def calcular_tiempo_primer_hit(datframe, id_participante):
>>>>>>> Stashed changes
    '''
    Devuelve el primer tiempo en el que ocurrió un hit entre todos los participantes.
    Parámetros:
    dataframe: dataframe con las siguientes columnas: "ID", "tiempo", "hit", "x", "y", "condicion".
    id: participante a conseguir su primer tiempo.

    Retorna:
    int | float | None :el primer tiempo del participante (haya tenido o no)

    '''
    mascara=(dataframe["hit"]==True) & (dataframe["ID"]==id_participante)
    filtrado=dataframe[mascara]
    return filtrado.iloc[0]['tiempo']

def calcular_hits_totales(df, id_participante):
    '''
    Calcula la cantidad de hits que tuvo el participante.

    Parámetros:
    df: DataFrame
        dataframe del participante con las siguientes columnas: "ID", "tiempo", "hit", "x", "y", "condicion".
   
   id: str
      participante a conseguir sus hits totales.
    
    Retorna:
    contador: int
        Cantidad de hits que tuvo el participante.
    
    '''
    mascara= df["ID"]== id_participante
    cant_t = df[mascara]["hit"].sum()

    return cant_t
   

def calcular_promedio(df, id_participante):
    '''
    Calcula el promedio entre el tiempo y la cantidad total de hits del participante.

    Parámetros:
    df: dataframe
        dataframe del participante con las siguientes columnas: "ID", "tiempo", "hit", "x", "y", "condicion".
   id: str
      participante a calcular su promedio.
    
    Retorna:
    promedio: float False:bool
        Promedio del participante entre el tiempo y la cantidad total de
             hits, False si el ultimo tiempo es 0.
    Raises: 
    ZeroDivisionError:
        Ocurre cuando el último tiempo ingresado es el numero 0. 
    '''
    cant_t = calcular_hits_totales(df, id_participante)
    mascara = df["ID"] == id_participante

    tiempo_ultimo = df[mascara].iloc[-1]["tiempo"]

    if tiempo_ultimo==0:
        raise ZeroDivisionError("El ultimo tiempo es 0")
    
    prom = round(cant_t / tiempo_ultimo)
    return prom

