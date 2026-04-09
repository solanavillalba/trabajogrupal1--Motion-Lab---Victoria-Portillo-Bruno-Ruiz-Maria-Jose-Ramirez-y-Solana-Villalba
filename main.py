import src.metricas as m
import src.cargar_datos as c
import src.procesamiento_datos as p

nombre_archivo = "datos/MotionLab_mock_data.csv"
lista_diccionario= c.cargar_datos(nombre_archivo)

if lista_diccionario is str:
    print("Error al abrir el archivo, modificar ruta")


else:

    while True:
        id_participante=input("ingrese id del participante del que quiere saber los datos: ")
        if c.validar_datos(id_participante, "int"):
            id_participante=int(id_participante)
            break
        print("Error, no ingresaste un int")
        
    diccionario= p.filtar_por_participante(id_participante, lista_diccionario)

    if type(diccionario) == bool:
        print("Error, Id no existe")

    elif type(diccionario) == dict:
        primer_hit=m.calcular_tiempo_primer_hit(diccionario)
        hits_tot=m.calcular_hits_totales(diccionario)

        print("el participante con id", id_participante)
        if type(primer_hit)==str: 
            print(primer_hit)
        else:
            print("Hizo su primer hit en el tiempo", primer_hit)
            
        print("Tiene", hits_tot, "hit en total")
        prom=m.calcular_promedio(diccionario)
        
        if prom==False:
            print("Y no se puede calcular el promedio porque el ultimo tiempo es 0")
        else:
            print("Y un promedio de", prom, "hits por segundo")
