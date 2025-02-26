import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title="Finalmente llegó el gran momento", layout="wide", page_icon="🎉")

# Mensaje inicial
st.markdown("<h1 style='text-align: center;'>¡Finalmente llegó este día!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Andá apretando este botón para que vayan apareciendo las sorpresas</h3>", unsafe_allow_html=True)

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
    st.markdown("<h1 id='letter-section'>Una Carta para Mi Amada Arquitectica</h1>", unsafe_allow_html=True)
    st.write("""
    Anna Banana,

    Y finalmente, este día llegó.
    Después de tanto recorrido, viendo desde el primer día la aventura que implicó avanzar en este hermoso camino, ayer cerraste una etapa única en la vida. Y diría, con la mayor de las distinciones, que alcanzaste un logro personal enorme. Algo que a veces cuesta reconocer o dimensionar, pero que nos define como personas: la vocación.
    
    La palabra cierre quizá no sea del todo precisa para algo que, dadas las circunstancias, se vuelve un pilar en nuestra vida. Porque más que terminar, este proceso es de construir, crear y darle forma al lugar que imaginas. Y es un camino de frustraciones, como de alegrías, pero también una herramienta única para dejar huella, para plasmar en el tiempo y el espacio todo lo que nuestra energía joven tiene para dar. Y en ese sentido, lo que lograste no fue solo cerrar una etapa, sino concretarla. Grande, rígida, arbitraria, estructurada y, a veces, incomprensible, se nos presentan los caminos hacia la vocación, pero siempre un desafío apasionante al que le hiciste frente con determinación.
    
    Por todo esto, siempre voy a estar fascinado por la forma, la firmeza y las ganas con las que atravesaste este tiempo. Y si miramos hacia atrás, parece casi de película: una pandemia, noches larguísimas, enfermedades, alegrías y algo de inseguridad por el qué hacer… Y aún así, acá estás, en una pieza. Como observador de este camino, este momento me llena, una vez más, de las tantas que disfruté a lo largo de este tiempo, de orgullo. Orgullo de verte caminar, de encontrarte con lo desconocido sin miedo, y de disfrutar cómo construís a la par de los lugares y desafíos que te hacen crecer.
    
    Solo con estas cosas, te aseguro, cada momento compartido es una alegría inmensa para mí.
    
    Y como hay tanto por delante, tanto por descubrir. Como persona y como profesional, todo lo que tenés para hacer y dejar como huella es inmenso. Por ello, apenas puedo expresar con estas palabras cuánto te quiero y cuánto significa para mí celebrar este logro tuyo.
    
    Espero que, con un poco más de tiempo y entre las nuevas cosas por organizar, armar y proyectar, nos encontremos juntos, construyendo como lo hicimos hasta ahora.
    
    Con todo el amor del mundo,  
    Martín
    """)

# Enlace opcional para ir a la carta
if st.session_state.gift_index >= len(gifts):
    st.markdown("[Ir a la carta](#letter-section)")
