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
    
    


