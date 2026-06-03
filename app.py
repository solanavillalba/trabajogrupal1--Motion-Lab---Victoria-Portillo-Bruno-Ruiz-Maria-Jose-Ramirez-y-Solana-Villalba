 
import streamlit as st
import matplotlib.pyplot as plt
import tempfile
import os
 
# Importamos nuestros propios módulos del backend
import src.cargar_datos as c
import src.procesamiento_datos as p
import src.metricas as m


"""
app.py. Dashboard interactivo de MotionLab con Streamlit.
 
Este script es la interfaz gráfica del sistema. Permite al usuario subir
el archivo CSV del laboratorio, validarlo, y ver los resultados de forma
visual para cada participante.
 
Para ejecutar la aplicación, correr en la terminal:
    streamlit run app.py
 
Módulos propios utilizados:
    src.cargar_datos        → carga y parsea el CSV
    src.procesamiento_datos → filtra por participante
    src.metricas            → calcula los KPIs del participante
"""
 
# Configuración general de la página
 
st.set_page_config(
    page_title="MotionLab Dashboard",
    page_icon="🎯",
    layout="centered"
)
 
st.title("🎯 MotionLab — Dashboard de Análisis")
st.markdown("Subí el archivo CSV del laboratorio para explorar los datos de cada participante.")
 
st.divider()
 
 
# Carga dinámica del archivo CSV

 
st.subheader("📂 Paso 1: Cargar el archivo de datos")
 
archivo_subido = st.file_uploader(
    label="Arrastrá o seleccioná el archivo CSV del laboratorio",
    type=["csv"]
)
 
# Si el usuario no subió nada todavía, no seguimos
if archivo_subido is None:
    st.info("Esperando el archivo CSV para comenzar el análisis...")
    st.stop()
 
 
# Validación defensiva del archivo
 
# Guardamos el archivo subido en un archivo temporal para poder leerlo con nuestro backend
with tempfile.NamedTemporaryFile(delete=False, suffix=".csv", mode="wb") as tmp:
    tmp.write(archivo_subido.read())
    ruta_temporal = tmp.name
 
# Intentamos cargar los datos usando nuestra función del backend
try:
    lista_diccionario = c.cargar_datos(ruta_temporal)
except FileNotFoundError as e:
    st.error(f"No se pudo abrir el archivo: {e}")
    st.stop()
except ValueError as e:
    st.error(f"El archivo tiene un error de formato: {e}")
    st.stop()
except Exception as e:
    st.error(f"Error inesperado al cargar el archivo: {e}")
    st.stop()
finally:
    # Borramos el archivo temporal al terminar (siempre)
    os.unlink(ruta_temporal)
 
# Si llegamos acá, el archivo está bien cargado
st.success(f"Archivo cargado correctamente con {len(lista_diccionario)} participantes.")
 
st.divider()
 
 

# Selección del participante
#  
st.subheader("Seleccionar participante")
 
# Obtenemos todos los IDs disponibles usando nuestra función de métricas
ids_disponibles = m.obtener_ids_participantes(lista_diccionario)
 
id_seleccionado = st.selectbox(
    label="Elegí el ID del participante:",
    options=ids_disponibles
)
 
# Buscamos el diccionario del participante elegido
try:
    diccionario_participante = p.filtar_por_participante(id_seleccionado, lista_diccionario)
except ValueError as e:
    st.error(f"Error al buscar el participante: {e}")
    st.stop()
 
st.divider()
 
 
# KPIs — Tarjetas de indicadores clave
 
st.subheader(f" Resultados del Participante ID {id_seleccionado}")
 
# Calculamos los KPIs usando nuestras funciones de métricas
hits_totales = m.calcular_hits_totales(diccionario_participante)
primer_hit   = m.calcular_tiempo_primer_hit(diccionario_participante)
 
try:
    promedio = m.calcular_promedio(diccionario_participante)
    promedio_str = f"{promedio} hits/seg"
except ZeroDivisionError:
    promedio_str = "Sin datos"
 
# Mostramos las tarjetas de métricas (KPIs) en 3 columnas
col1, col2, col3 = st.columns(3)
 
with col1:
    st.metric(
        label="Hits Totales",
        value=hits_totales
    )
 
with col2:
    if primer_hit is not None:
        st.metric(
            label="Tiempo Primer Hit",
            value=f"{primer_hit} seg"
        )
    else:
        st.metric(
            label=" Tiempo Primer Hit",
            value="Sin hits"
        )
 
with col3:
    st.metric(
        label="Promedio hits/seg",
        value=promedio_str
    )
 
# Mostramos también la condición experimental
st.caption(f"Condición experimental: **{diccionario_participante['condicion']}**")
 
st.divider()
 
 
# Visualizaciones — Gráficos
 
st.subheader("Gráficos del Participante")
 
 
# Gráfico 1: Línea de tiempo del primer hit
 
if primer_hit is not None:
    st.markdown("**Primer Hit**")
 
    fig1, ax1 = plt.subplots(figsize=(8, 2))
 
    # Graficamos todos los tiempos donde hubo hit
    tiempos_con_hit = [
        diccionario_participante['tiempo'][i]
        for i, hit in enumerate(diccionario_participante['hit'])
        if hit
    ]
 
    ax1.scatter(tiempos_con_hit, [1] * len(tiempos_con_hit), color='steelblue', zorder=5, label='Hits')
    ax1.scatter([primer_hit], [1], color='crimson', s=150, zorder=6, label=f'Primer Hit ({primer_hit}s)')
    ax1.set_xlabel('Tiempo (segundos)')
    ax1.set_yticks([])
    ax1.set_title(f'Línea de Tiempo — Hits del Participante {id_seleccionado}')
    ax1.legend()
 
    st.pyplot(fig1)
    plt.close(fig1)
else:
    st.info("ℹ️ Este participante no registró ningún hit.")
 
 
# ── Gráfico 2: Total de hits por participante ──────────────
 
st.markdown("**Total de hits por participante**")
 
# Calculamos los hits de todos los participantes para comparar
todos_ids = []
todos_hits = []
 
for dicc in lista_diccionario:
    todos_ids.append(dicc["ID"])
    todos_hits.append(m.calcular_hits_totales(dicc))
 
fig2, ax2 = plt.subplots(figsize=(8, 4))
 
# Resaltamos el participante seleccionado en otro color
colores = [
    'crimson' if id_p == id_seleccionado else 'steelblue'
    for id_p in todos_ids
]
 
ax2.bar(todos_ids, todos_hits, color=colores)
ax2.set_xlabel('ID del Participante')
ax2.set_ylabel('Cantidad de Hits')
ax2.set_title('Total de Hits por Participante')
ax2.set_xticks(todos_ids)
 
# Pequeña leyenda manual
from matplotlib.patches import Patch
leyenda = [
    Patch(color='crimson', label='Participante seleccionado'),
    Patch(color='steelblue', label='Otros participantes')
]
ax2.legend(handles=leyenda)
 
st.pyplot(fig2)
plt.close(fig2)
 