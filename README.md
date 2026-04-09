Programa que se encarga de leer archivos de motion lab, pedir un id del participante del que se quiera saber sus metricas. E imprime el promedio de hits, primer tiempo que hizo un hit y cuantos hit hizo el participante.


Errores y Validaciones:

"Error al abrir el archivo, modificar ruta" La funcion cargar_datos se encarga de verificar si se puede abrir el archivo.

"Error de longitud en la linea" La funcion parsear_linea se encarga de verificar que la lista tenga 6 elementos.

"Error casteando (tipo de la variable)" La funcion validar_datos se encarga de verificar si un valor se puede castear.

"Error no ingresaste un int" El codigo principal llama a validar_datos de cargar_datos.py para verificar si ingresaste un int.

"Error ID no existe". La funcion filtar_por_participante de procesamiento_datos.py valida si el ID.

Division por 0: "No se puede calcular el promedio porque el ultimo tiempo es 0". La funcion calcular_promedio de metricas.py valida que el divisor no sea 0.

