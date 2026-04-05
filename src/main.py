import metricas as m
import cargar_datos as c
import procesamiento_datos as p

nombre_archivo = "datos_ejemplo.csv"
lista_diccionario= c.cargar_datos(nombre_archivo)

while True:
    id_participante=input("ingrese id del participante del que quiere saber los datos: ")
    if c.validar_datos(id_participante, "int"):
        break
    print("no ingresaste un int")
    
diccionario=p.filtar_por_participante(id, lista_diccionario)

hits_tot=m.calcular_hits_totales(diccionario)
prom=m.calcular_promedio(diccionario)

print("el participante con id", id_participante)
print("tiene", hits_tot, "hits totales")
print("y un promedio de ", prom, "hits por segundo")
