import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import joblib
import numpy as np
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Salud Mental",  # Título de la ventana
    page_icon="⚕️",  # Favicon: puedes usar emojis o un archivo de imagen (.png, .ico, etc.)
    layout="centered",  # Opcional: "centered" o "wide" para la disposición de la página
    initial_sidebar_state="expanded"  # Opcional: Estado inicial de la barra lateral
)

with st.sidebar:
    st.image("PaginaWeb/logo.png", use_container_width=True)
    
    selected = option_menu("Menú Principal", ['Inicio','Ansiedad','Depresión','Estrés'], 
        icons=["house-fill",'emoji-grimace-fill', 'emoji-tear-fill', 'emoji-angry-fill'], 
        menu_icon="clipboard2-pulse-fill", default_index=1)

#PÁGINA INICIO
if selected == "Inicio":
    st.markdown(
    """
    <div style="text-align: center; margin-top: 20px;">
        <h1>Aplicación de Análisis de transtornos en estudiantes universitarios.</h1>
    </div>
    """,
    unsafe_allow_html=True
)
    st.subheader("💠 Tu herramienta para evaluar riesgos de ansiedad, depresión y estrés para estudiantes universitarios.")
    st.write("""
    La salud mental es un pilar fundamental en el desarrollo integral de los estudiantes. 
    Durante las etapas educativas, los jóvenes enfrentan múltiples desafíos: exigencias académicas, 
    cambios emocionales, construcción de identidad, relaciones interpersonales y, en muchos casos, 
    la transición hacia la vida adulta. Estas experiencias, aunque enriquecedoras, pueden generar 
    estrés, ansiedad y otros problemas emocionales si no se gestionan adecuadamente.

    En esta plataforma, buscamos sensibilizar y apoyar a los estudiantes en su camino hacia el 
    bienestar emocional, ofreciendo análisis personalizados y recursos prácticos para fortalecer 
    su salud mental. Porque un estudiante saludable es un estudiante preparado para transformar su 
    entorno y alcanzar sus metas.
    """)
    
    st.image("/workspaces/PaginaWeb/1.png", use_container_width=True)

    st.write("---")  # Línea divisoria

    st.subheader("🔮 ¿Cómo usar esta aplicación?")
    st.markdown("""
    1. **Selecciona una opción en el menú lateral:**  
   Dirígete al cuestionario que desees responder (Ansiedad, Depresión, Estrés).
    2. **Llena el formulario:**  
   Completa las preguntas basadas en tus experiencias recientes.
    3. **Analiza tus resultados:**  
   Una vez completado, revisa los resultados generados automáticamente por el sistema.
    """)

    st.subheader("🔮 ¿Por qué usar esta aplicación?")
    st.write("""
    - **Fácil de usar:** Interfaz intuitiva y directa para cualquier usuario.
    - **Análisis basado en datos:** Algoritmos de Machine Learning respaldan las predicciones.
    - **Resultados útiles:** Gráficos y tablas fáciles de entender.
    - **Privacidad garantizada:** Tus datos no se almacenan ni se comparten.
    """)

    st.image("/workspaces/PaginaWeb/2.png", use_container_width=True)

#SELECCIÓN ANSIEDAD
if selected == "Ansiedad":
    st.title("ANÁLISIS DE NIVEL DE ANSIEDAD")
    
    # SELECCIONAR MODELO
    model = joblib.load('/workspaces/PaginaWeb/salud_mental_ansiedad_MLP.pkl')

    # ASIGNACIÓN DE VALORES
    valores_respuestas = {
    "Nunca.": 0,
    "De vez en cuando.": 1,
    "Muchas veces.": 2,
    "Casi Siempre.": 3,
    "Siempre.": 4
    }
    
    # CONTENIDO
    st.write("Rellene las siguientes preguntas:")

     # Pregunta N1
    st.write("1. En un semestre, ¿con qué frecuencia te sentiste nervioso, ansioso o nervioso debido a la presión académica?")
    respuesta1 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta1"
    )

    # Pregunta N2
    st.write("2. En un semestre, ¿cuántas veces no has podido dejar de preocuparte por tus asuntos académicos?")
    respuesta2 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta2"
    )
    
     # Pregunta N3
    st.write("3. En un semestre, ¿con qué frecuencia has tenido problemas para relajarte debido a la presión académica?")
    respuesta3 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta3"
    )

    # Pregunta N4
    st.write("4. En un semestre, ¿con qué frecuencia te has sentido fácilmente molesto o irritado debido a la presión académica?")
    respuesta4 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta4"
    )

    # Pregunta N5
    st.write("5. En un semestre, ¿con qué frecuencia te has preocupado demasiado por asuntos académicos?")
    respuesta5 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta5"
    )

    # Pregunta N6
    st.write("6. En un semestre, ¿cuántas veces te has sentido tan inquieto debido a la presión académica que te resulta difícil quedarte quieto?")
    respuesta6 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta6"
    )

    # Pregunta N7
    st.write("7. En un semestre, ¿cuántas veces has sentido miedo, como si algo terrible pudiera pasar?")
    respuesta7 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta7"
    )

    respuestas = [
    valores_respuestas[respuesta1],
    valores_respuestas[respuesta2],
    valores_respuestas[respuesta3],
    valores_respuestas[respuesta4],
    valores_respuestas[respuesta5],
    valores_respuestas[respuesta6],
    valores_respuestas[respuesta7],
]
    # Usar Modelo
    features = [valores_respuestas[respuesta1], valores_respuestas[respuesta2], valores_respuestas[respuesta3],
    valores_respuestas[respuesta4], valores_respuestas[respuesta5],valores_respuestas[respuesta6],valores_respuestas[respuesta7]]
    
    if st.button("Generar Progresión de Ansiedad"):
        # Calcular porcentaje acumulado
        porcentaje_acumulado = np.cumsum(respuestas) / (len(respuestas) * 4) * 100

     # Generar gráfico de línea
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(range(1, len(respuestas) + 1), porcentaje_acumulado, marker="o", linestyle="-", color="red")
        ax.set_xticks(range(1, len(respuestas) + 1))
        ax.set_xticklabels([f"{i}" for i in range(1, len(respuestas) + 1)])
        ax.set_ylabel("Ansiedad Acumulada (%)")
        ax.set_xlabel("Número de Pregunta")
        ax.set_title("Progresión del Nivel de Ansiedad")
        ax.grid(True)

        # Mostrar el gráfico
        st.pyplot(fig)

        # Crear una tabla asociada a las preguntas
        preguntas = [
        "Te sentiste nervioso/a debido a la presión académica",
        "No dejaste de preocuparte por asuntos académicos",
        "Tuviste problemas para relajarte",
        "Te sentiste molesto/a o irritado/a",
        "Te preocupaste demasiado por asuntos académicos",
        "Te sentiste inquieto/a y no pudiste quedarte quieto/a",
        "Sentiste miedo como si algo terrible pudiera pasar",
        ]

        # Crear un DataFrame con las preguntas y los números
        tabla_preguntas = pd.DataFrame({
        "Número de Pregunta": range(1, len(preguntas) + 1),
        "Pregunta": preguntas
        })

        # Generar tabla HTML sin índices y agregar estilo para centrarla
        tabla_html = tabla_preguntas.to_html(index=False, escape=False)
        tabla_centrada = f"""
        <div style="display: flex; justify-content: center; margin-top: 20px;">
        {tabla_html}
        </div>
        """

        # Mostrar la tabla centrada
        st.markdown(tabla_centrada, unsafe_allow_html=True)

        # Mostrar el porcentaje total de ansiedad
        porcentaje_total = porcentaje_acumulado[-1]
        # Mostrar el porcentaje total de ansiedad centrado
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 20px;">
            <h3>Ansiedad Total: {porcentaje_total:.2f}%</h3>
            </div>
            """,
            unsafe_allow_html=True
)

#SELECCIÓN DEPRESIÓN
elif selected == "Depresión":
    st.title("ANÁLISIS DE NIVEL DE DEPRESIÓN")
    
    # SELECCIONAR MODELO
    model = joblib.load('/workspaces/PaginaWeb/salud_mental_depression_MLP.pkl')
    
    # ASIGNACIÓN DE VALORES
    valores_respuestas = {
    "Nunca.": 0,
    "De vez en cuando.": 1,
    "Muchas veces.": 2,
    "Casi Siempre.": 3,
    "Siempre.": 4
    }

    # CONTENIDO
    st.write("Rellene las siguientes preguntas:")

    # Pregunta N1
    st.write("1. En un semestre, ¿con qué frecuencia has tenido poco interés o placer en hacer las cosas?")
    respuesta1 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta1"
    )

    # Pregunta N2
    st.write("2. En un semestre, ¿con qué frecuencia te has sentido deprimido, desanimado o sin esperanza?")
    respuesta2 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta2"
    )

    # Pregunta N3
    st.write("3. En un semestre, ¿con qué frecuencia ha tenido problemas para conciliar el sueño o permanecer dormido, o ha dormido demasiado?")
    respuesta3 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta3"
    )

    # Pregunta N4
    st.write("4. En un semestre, ¿con qué frecuencia te has sentido cansado o con poca energía?")
    respuesta4 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta4"
    )

    # Pregunta N5
    st.write("5. En un semestre, ¿con qué frecuencia has tenido falta de apetito o has comido en exceso?")
    respuesta5 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta5"
    )

    # Pregunta N6
    st.write("6. En un semestre, ¿con qué frecuencia te has sentido mal contigo mismo, o que eres un fracasado, o que te has decepcionado a ti mismo o a tu familia?")
    respuesta6 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta6"
    )

     # Pregunta N7
    st.write("7. En un semestre, ¿con qué frecuencia has tenido problemas para concentrarte en cosas, como leer libros o mirar televisión?")
    respuesta7 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta7"
    )

    # Pregunta N8
    st.write("8. En un semestre, ¿con qué frecuencia te has movido o has hablado demasiado lento para que otras personas lo notaran? ¿O te has estado moviendo mucho más de lo habitual porque has estado inquieto?")
    respuesta8 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta8"
    )

    # Pregunta N9
    st.write("9. En un semestre, ¿con qué frecuencia has pensado que estarías mejor muerto o que te harías daño?")
    respuesta9 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.","Casi Siempre.", "Siempre."),
        key="pregunta9"
    )
    
    # Usar Modelo
    features = [valores_respuestas[respuesta1], valores_respuestas[respuesta2], valores_respuestas[respuesta3],
    valores_respuestas[respuesta4], valores_respuestas[respuesta5],valores_respuestas[respuesta6],valores_respuestas[respuesta7],
    valores_respuestas[respuesta8],valores_respuestas[respuesta9]]
    
    respuestas = [
        valores_respuestas[respuesta1],
        valores_respuestas[respuesta2],
        valores_respuestas[respuesta3],
        valores_respuestas[respuesta4],
        valores_respuestas[respuesta5],
        valores_respuestas[respuesta6],
        valores_respuestas[respuesta7],
        valores_respuestas[respuesta8],
        valores_respuestas[respuesta9],
    ]

    if st.button("Generar Progresión de Depresión"):
        # Calcular porcentaje acumulado
        porcentaje_acumulado = np.cumsum(respuestas) / (len(respuestas) * 4) * 100

        # Generar gráfico de línea
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(range(1, len(respuestas) + 1), porcentaje_acumulado, marker="o", linestyle="-", color="red")
        ax.set_xticks(range(1, len(respuestas) + 1))
        ax.set_xticklabels([f"{i}" for i in range(1, len(respuestas) + 1)])
        ax.set_ylabel("Depresión Acumulada (%)")
        ax.set_xlabel("Número de Pregunta")
        ax.set_title("Progresión del Nivel de Depresión")
        ax.grid(True)

        # Mostrar el gráfico
        st.pyplot(fig)

        # Crear una tabla asociada a las preguntas
        preguntas = [
            "Poco interés o placer en hacer las cosas",
            "Te sentiste deprimido/a o sin esperanza",
            "Tuviste problemas para dormir",
            "Te sentiste cansado/a o con poca energía",
            "Falta de apetito o comiste en exceso",
            "Te sentiste mal contigo mismo/a",
            "Tuviste problemas para concentrarte",
            "Te moviste o hablaste lento o estuviste inquieto",
            "Pensaste en hacerte daño o estarías mejor muerto/a",
        ]

        # Crear un DataFrame con las preguntas y los números
        tabla_preguntas = pd.DataFrame({
            "Número de Pregunta": range(1, len(preguntas) + 1),
            "Pregunta": preguntas
        })

        # Generar tabla HTML sin índices y centrarla
        tabla_html = tabla_preguntas.to_html(index=False, escape=False)
        tabla_centrada = f"""
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            {tabla_html}
        </div>
        """

        # Mostrar la tabla centrada
        st.write("### Asociaciones entre números y preguntas:")
        st.markdown(tabla_centrada, unsafe_allow_html=True)

        # Mostrar el porcentaje total de depresión
        porcentaje_total = porcentaje_acumulado[-1]
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 20px;">
                <h3>Depresión Total: {porcentaje_total:.2f}%</h3>
            </div>
            """,
            unsafe_allow_html=True
        )       


# SELECCIÓN ESTRÉS
elif selected == "Estrés":
    st.title("ANÁLISIS DE NIVEL DE ESTRÉS")
    
    # SELECCIONAR MODELO
    model = joblib.load('/workspaces/PaginaWeb/salud_mental_stress_SVC.pkl')
    
    # ASIGNACIÓN DE VALORES
    valores_respuestas = {
        "Nunca.": 0,
        "De vez en cuando.": 1,
        "Muchas veces.": 2,
        "Casi Siempre.": 3,
        "Siempre.": 4
    }

    # ASIGNACIÓN DE VALORES INVERSOS PARA PREGUNTAS ESPECÍFICAS
    valores_respuestas_inversos = {
        "Nunca.": 4,
        "De vez en cuando.": 3,
        "Muchas veces.": 2,
        "Casi Siempre.": 1,
        "Siempre.": 0
    }

    # CONTENIDO
    st.write("Rellene las siguientes preguntas:")

    # Preguntas del cuestionario
    st.write("1. En un semestre, ¿con qué frecuencia te has sentido molesto debido a algo que sucedió en tus asuntos académicos?")
    respuesta1 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.", "Casi Siempre.", "Siempre."),
        key="pregunta1"
    )

    st.write("2. En un semestre, ¿con qué frecuencia te sentiste incapaz de controlar cosas importantes en tus asuntos académicos?")
    respuesta2 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.", "Casi Siempre.", "Siempre."),
        key="pregunta2"
    )

    st.write("3. En un semestre, ¿con qué frecuencia se sintió nervioso y estresado debido a la presión académica?")
    respuesta3 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.", "Casi Siempre.", "Siempre."),
        key="pregunta3"
    )

    st.write("4. En un semestre, ¿con qué frecuencia sintió que no podía hacer frente a todas las actividades académicas obligatorias? (p. ej., tareas, exámenes, cuestionarios)")
    respuesta4 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.", "Casi Siempre.", "Siempre."),
        key="pregunta4"
    )

    st.write("5. En un semestre, ¿con qué frecuencia se sintió seguro de su capacidad para manejar sus problemas académicos/universitarios?")
    respuesta5 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.", "Casi Siempre.", "Siempre."),
        key="pregunta5"
    )

    st.write("6. En un semestre, ¿con qué frecuencia sintió que las cosas en su vida académica iban por buen camino?")
    respuesta6 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.", "Casi Siempre.", "Siempre."),
        key="pregunta6"
    )

    st.write("7. En un semestre, ¿con qué frecuencia puede controlar las irritaciones en sus asuntos académicos/universitarios?")
    respuesta7 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.", "Casi Siempre.", "Siempre."),
        key="pregunta7"
    )

    st.write("8. En un semestre, ¿con qué frecuencia sintió que su desempeño académico era excelente?")
    respuesta8 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.", "Casi Siempre.", "Siempre."),
        key="pregunta8"
    )

    st.write("9. En un semestre, ¿cuántas veces te enojaste debido a un mal desempeño o bajas calificaciones que estaban fuera de tu control?")
    respuesta9 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.", "Casi Siempre.", "Siempre."),
        key="pregunta9"
    )

    st.write("10. En un semestre, ¿con qué frecuencia sintió que las dificultades académicas se acumulaban tanto que no podía superarlas?")
    respuesta10 = st.radio(
        "Seleccione una opción",
        ("Nunca.", "De vez en cuando.", "Muchas veces.", "Casi Siempre.", "Siempre."),
        key="pregunta10"
    )

    # Convertir respuestas a valores numéricos (con inversión en preguntas 5, 6, 7, 8)
    respuestas = [
        valores_respuestas[respuesta1],
        valores_respuestas[respuesta2],
        valores_respuestas[respuesta3],
        valores_respuestas[respuesta4],
        valores_respuestas_inversos[respuesta5],  # Valores inversos
        valores_respuestas_inversos[respuesta6],  # Valores inversos
        valores_respuestas_inversos[respuesta7],  # Valores inversos
        valores_respuestas_inversos[respuesta8],  # Valores inversos
        valores_respuestas[respuesta9],
        valores_respuestas[respuesta10],
    ]

    if st.button("Generar Progresión de Estrés"):
        # Calcular porcentaje acumulado
        porcentaje_acumulado = np.cumsum(respuestas) / (len(respuestas) * 4) * 100

        # Generar gráfico de línea
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(range(1, len(respuestas) + 1), porcentaje_acumulado, marker="o", linestyle="-", color="red")
        ax.set_xticks(range(1, len(respuestas) + 1))
        ax.set_xticklabels([f"{i}" for i in range(1, len(respuestas) + 1)])
        ax.set_ylabel("Estrés Acumulado (%)")
        ax.set_xlabel("Número de Pregunta")
        ax.set_title("Progresión del Nivel de Estrés")
        ax.grid(True)

        # Mostrar el gráfico
        st.pyplot(fig)

        # Crear una tabla asociada a las preguntas
        preguntas = [
            "Te sentiste molesto por asuntos académicos",
            "Sentiste incapacidad para controlar cosas importantes",
            "Te sentiste nervioso/a y estresado/a",
            "No pudiste hacer frente a actividades académicas",
            "Te sentiste seguro de manejar problemas académicos",
            "Sentiste que tu vida académica iba bien",
            "Controlaste irritaciones académicas",
            "Tu desempeño académico fue excelente",
            "Te enojaste por malas calificaciones fuera de tu control",
            "Las dificultades académicas se acumularon",
        ]

        # Crear un DataFrame con las preguntas y los números
        tabla_preguntas = pd.DataFrame({
            "Número de Pregunta": range(1, len(preguntas) + 1),
            "Pregunta": preguntas
        })

        # Generar tabla HTML sin índices y centrarla
        tabla_html = tabla_preguntas.to_html(index=False, escape=False)
        tabla_centrada = f"""
        <div style="display: flex; justify-content: center; margin-top: 20px;">
            {tabla_html}
        </div>
        """

        # Mostrar la tabla centrada
        st.write("### Asociaciones entre números y preguntas:")
        st.markdown(tabla_centrada, unsafe_allow_html=True)

        # Mostrar el porcentaje total de estrés
        porcentaje_total = porcentaje_acumulado[-1]
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 20px;">
                <h3>Estrés Total: {porcentaje_total:.2f}%</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
