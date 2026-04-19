import src.metricas as m
import src.cargar_datos as c
import src.procesamiento_datos as p
import src.validar_datos as v

nombre_archivo = "datos/MotionLab_mock_data_error01.csv"
try:
    lista_diccionario= c.cargar_datos(nombre_archivo)
except FileNotFoundError as e:
    print(e)

else:
    while True:
        id_participante=input("ingrese id del participante del que quiere saber los datos: ")
        try:
            ccc= v.validar_datos(id_participante, "int")
        except Exception as e:
            print(e)
        else:
            id_participante=int(id_participante)
            try:   
                diccionario= p.filtar_por_participante(id_participante, lista_diccionario)
            except ValueError as e:
                print(e)
            else:
                break

    primer_hit=m.calcular_tiempo_primer_hit(diccionario)
    hits_tot=m.calcular_hits_totales(diccionario)

    print("el participante con id", id_participante)
    if type(primer_hit)==str: 
        print(primer_hit)
    else:
        print("Hizo su primer hit en el tiempo", primer_hit)
            
    print("Tiene", hits_tot, "hit en total")
        
    try:
        prom=m.calcular_promedio(diccionario)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("Y un promedio de", prom, "hits por segundo")
