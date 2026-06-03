import os #lo que nos explicaron para poder movernos entre carpetas sin tener que cambiar la ruta constantemente
import pandas as pd 


def cargar_datos (ruta, nombre_archivo):
    """ 
    Abre un archivo CSV y lo carga como un DataFrame
    
    Parámetros
    ruta : str
        Ruta por donde se puede acceder al archivo.
    Retorna
     df : DataFrame
        Tabla con todos los datos del archivo.
    Raises
    FileNotFoundError:
        Si no fue posible encontrar el archivo.
    """ 
    os.chdir(ruta)
    try: 
     df = pd.read_csv(nombre_archivo)
    except FileNotFoundError:
        raise FileNotFoundError("No se logro abrir el archivo")
    return df 

#asi se usaria despues, cada uno pone su propia ruta y el nombre del archivo:
# ruta = reemplaza con tu ruta
# nombre_archivo = reemplazar con el nombre de tu archivo 
#df = cargar_datos(aca se pone la ruta deseada)
#print(df) 



def filtrar_por_participante(df, id_buscado):
    """
    Filtra las filas del DataFrame según el ID del participante.
    
    Parámetros
    df : DataFrame
        Tabla con todos los datos cargados.
    id_buscado : int
        ID del participante que se quiere filtrar.
    
    Retorna
    participante : DataFrame
        Tabla con solo las filas del participante buscado.
    """
    #aca la máscara revisa fila por fila si el ID coincide
    # devuelve True o False para cada fila

    mascara = df["ID"] == id_buscado
    #aca nos quedamos solo con las filas donde la mascara devuelve True
    participante = df[mascara]
    return participante

ruta = 'C:\\Users\\estudiante\\Downloads\\Proyectos - Ficha Técnica-20260528\\MotionLab'
df = cargar_datos(ruta, "MotionLab_mock_data.csv")




def calcular_tiempo_primer_hit(datframe, id_participante):

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

