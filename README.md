Programa que se encarga de leer archivos de motion lab, pedir un id del participante del que se quiera saber sus metricas. E imprime el promedio de hits, primer tiempo que hizo un hit y cuantos hit hizo el participante.


Errores y Validaciones:

"Error al abrir el archivo, modificar ruta" La funcion cargar_datos se encarga de verificar si se puede abrir el archivo.

"Error de longitud en la linea" La funcion parsear_linea se encarga de verificar que la lista tenga 6 elementos.

"Error casteando (tipo de la variable)" La funcion validar_datos se encarga de verificar si un valor se puede castear.

"Error no ingresaste un int" El codigo principal llama a validar_datos de cargar_datos.py para verificar si ingresaste un int.

"Error ID no existe". La funcion filtar_por_participante de procesamiento_datos.py valida si el ID.

Division por 0: "No se puede calcular el promedio porque el ultimo tiempo es 0". La funcion calcular_promedio de metricas.py valida que el divisor no sea 0.

-------------------------------------------------------------------------------------
  Procedimiento con objetos:

  clase: Participante
  atributos:
  - ID
  - tiempo
  - hit
  - x
  - y
  - condicion
  metodos:
  - promedio
  - tiempo de primer hit
  - cantidad de hit

  clase: Muestra
  atributos:
  - lista de objetos
  metodos:
  - Mostrar datos de un participante
  - Calcular promedio de todos los participantes
  - Promedio de primer hit
  - Hits totales
  - Promedio de hits totales

-------------------------------------------------------------------------------------

PANDAS:
  En lugar de leer el archivo línea por línea como hacía nuestra función cargar_datos(), con pandas vamos a usar pd.read_csv() para cargar todo de una vez, convirtiendo el archivo csv en un dataframe (una tabla de filas y columnas). 

Luego la función filtrar_por_participante() la vamos a reemplazar por una máscara que filtre directamente las filas donde el ID coincida con el participante buscado.  

Para calcular_tiempo_primer_hit(), vamos a usar una máscara que combine el id del participante con la condición de que hit sea True, y con .iloc[0] se obtendría el tiempo de la primera fila que cumpla esa condición. Para calcular_hits_totales() hay dos opciones, una es usar una máscara que filtre los True y implementar .count() para contar las filas que resulten true, o la segunda opción, usaríamos .sum() sobre la columna hit, que suma solo los true ignorando los false. Y para calcular_promedio() usaremos .mean en la mascara del participante.
