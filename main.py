import src.metricas as m
import src.cargar_datos as c
import src.procesamiento_datos as p

nombre_archivo = "datos/MotionLab_mock_data.csv"
lista_diccionario= c.cargar_datos(nombre_archivo)

while True:
    id_participante=input("ingrese id del participante del que quiere saber los datos: ")
    if c.validar_datos(id_participante, "int"):
        id_participante=int(id_participante)
        break
    print("no ingresaste un int")
    
diccionario= p.filtar_por_participante(id_participante, lista_diccionario)

if diccionario == False:
    print("Id no existe")
    
else:
    primer_hit=m.calcular_tiempo_primer_hit(diccionario)
    hits_tot=m.calcular_hits_totales(diccionario)
    prom=m.calcular_promedio(diccionario)

    print("el participante con id", id_participante)
    print("hizo su primer hit en el tiempo", primer_hit)
    print("tiene", hits_tot, "hit en total")
    print("y un promedio de", prom, "hits por segundo")
