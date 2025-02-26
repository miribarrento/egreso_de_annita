import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Finalmente llegó el gran momento", layout="wide", page_icon="🎉")

# Aplicar estilos CSS personalizados
st.markdown(
    """
    <style>
        /* Importar fuente EB Garamond */
        @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;700&display=swap');

        /* Estilos generales */
        body {
            font-family: 'EB Garamond', serif;
            background-color: #FAF3E0;  /* Fondo color hueso */
            color: #4A4A4A;  /* Texto en gris oscuro */
        }

        /* Centrar títulos */
        h1, h2, h3 {
            text-align: center;
        }

        /* Estilo para la carta */
        .letter {
            font-size: 20px;
            line-height: 1.6;
            text-align: justify;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.8); /* Fondo semi-transparente */
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Mensaje inicial
st.markdown("<h1>¡Finalmente llegó este día!</h1>", unsafe_allow_html=True)
st.markdown("<h3>Andá apretando este botón para que vayan apareciendo las sorpresas</h3>", unsafe_allow_html=True)

# Lista de imágenes y mensajes
gifts = [
    {"image": "images/balaclava.jpg", "message": "A elección y de donde quieras + alguna carterita. ¡Quiero una carterita para vos!"},
    {"image": "images/fiesta.jpg", "message": "Confirmá y vas"},
    {"image": "images/sobre.jpg", "message": "Abrilo y leé lo que sigue..."}
]

# Estado para controlar cuántas sorpresas se han mostrado
if 'gift_index' not in st.session_state:
    st.session_state.gift_index = 0

# Botón para revelar las sorpresas
if st.button("¡Siguiente sorpresa!"):
    if st.session_state.gift_index < len(gifts):
        st.session_state.gift_index += 1

# Mostrar las sorpresas reveladas hasta ahora
if st.session_state.gift_index > 0:
    st.markdown("---")
    st.title("Tus Regalos")
    cols = st.columns(3)
    for i in range(st.session_state.gift_index):
        with cols[i % 3]:
            st.image(gifts[i]["image"], use_container_width=True)
            st.write(gifts[i]["message"])

# Mostrar la carta cuando se hayan revelado todas las imágenes
if st.session_state.gift_index >= len(gifts):
    st.markdown("---")
    st.markdown("<h1 id='letter-section'>Una Carta para Mi Amor</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='letter'>
            <p>Anna Banana,</p>
            <p>Y finalmente, este día llegó.</p>
            <p>Después de tanto recorrido, viendo desde el primer día la aventura que implicó avanzar en este hermoso camino, ayer cerraste una etapa única en la vida. Y diría, con la mayor de las distinciones, que alcanzaste un logro personal enorme. Algo que a veces cuesta reconocer o dimensionar, pero que nos define como personas: la vocación.</p>

            <p>La palabra cierre quizá no sea del todo precisa para algo que, dadas las circunstancias, se vuelve un pilar en nuestra vida. Porque más que terminar, este proceso es de construir, crear y darle forma al lugar que imaginas. Y es un camino de frustraciones, como de alegrías, pero también una herramienta única para dejar huella, para plasmar en el tiempo y el espacio todo lo que nuestra energía joven tiene para dar. Y en ese sentido, lo que lograste no fue solo cerrar una etapa, sino concretarla. Grande, rígida, arbitraria, estructurada y, a veces, incomprensible, se nos presentan los caminos hacia la vocación, pero siempre un desafío apasionante al que le hiciste frente con determinación.</p>

            <p>Por todo esto, siempre voy a estar fascinado por la forma, la firmeza y las ganas con las que atravesaste este tiempo. Y si miramos hacia atrás, parece casi de película: una pandemia, noches larguísimas, enfermedades, alegrías y algo de inseguridad por el qué hacer… Y aún así, acá estás, en una pieza. Como observador de este camino, este momento me llena, una vez más, de las tantas que disfruté a lo largo de este tiempo, de orgullo. Orgullo de verte caminar, de encontrarte con lo desconocido sin miedo, y de disfrutar cómo construís a la par de los lugares y desafíos que te hacen crecer.</p>

            <p>Solo con estas cosas, te aseguro, cada momento compartido es una alegría inmensa para mí.</p>

            <p>Y como hay tanto por delante, tanto por descubrir. Como persona y como profesional, todo lo que tenés para hacer y dejar como huella es inmenso. Por ello, apenas puedo expresar con estas palabras cuánto te quiero y cuánto significa para mí celebrar este logro tuyo.</p>

            <p>Espero que, con un poco más de tiempo y entre las nuevas cosas por organizar, armar y proyectar, nos encontremos juntos, construyendo como lo hicimos hasta ahora.</p>

            <p><strong>Con todo el amor del mundo,</strong><br>Martín</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Enlace opcional para ir a la carta
if st.session_state.gift_index >= len(gifts):
    st.markdown("[Ir a la carta](#letter-section)")
