import streamlit as st
import os
import base64

# Configuración de la página
st.set_page_config(page_title="Finalmente llegó el gran momento", layout="wide", page_icon="🎉")

# Función para cargar y reproducir el audio automáticamente
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# Reproducir el audio al cargar la página
audio_path = "audio/track.mp3"  # Ajusta esta ruta según el nombre de tu archivo
if os.path.exists(audio_path):
    autoplay_audio(audio_path)
else:
    st.write("No se encontró el archivo de audio. Asegúrate de subirlo a la carpeta 'audio'.")

# Mensaje inicial
st.markdown("<h1 style='text-align: center;'>¡Finalmente llegó este día!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Andá apretando este botón para que vayan apareciendo las sorpresas</h3>", unsafe_allow_html=True)

# Lista de imágenes y mensajes en el orden específico
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
    cols = st.columns(3)  # Cuadrícula de 3 columnas
    for i in range(st.session_state.gift_index):
        with cols[i % 3]:
            st.image(gifts[i]["image"], use_column_width=True)
            st.write(gifts[i]["message"])

# Mostrar la carta cuando se hayan revelado todas las imágenes
if st.session_state.gift_index >= len(gifts):
    st.markdown("---")
    st.markdown("<h1 id='letter-section'>Una Carta para Mi Amor</h1>", unsafe_allow_html=True)
    st.write("""
    Anna Banana,

    Y un día llegó. Después de un hermoso camino y una etapa única en tu vida, hoy te veo cerrar este proyecto que, con tanto esfuerzo y empeño, lograste completar. Siempre voy a estar orgulloso y fascinado de verte caminar, de encontrarte en esos lugares que te hacen ser quien sos, donde disfrutás y das vida a lo que llena tu tiempo. Solo con eso, te aseguro, cada momento compartido será una alegría única para mí.

    Hay tanto por delante, tanto por descubrir, como en todo lo que tenés para hacer y dejar como huella, como persona y como profesional. Que apenas puedo expresar con esto un poco de cuánto te quiero y cuánto significa para mí celebrar este logro tuyo. 

    Espero que, con un poco más de tiempo y entre las nuevas cosas por organizar, armar y proyectar, nos encontremos juntos, construyendo como lo hicimos hasta ahora.  
    
    Con todo el amor del mundo,  
    Martín
    """)

# Enlace opcional para ir a la carta (aparece solo si ya se mostró)
if st.session_state.gift_index >= len(gifts):
    st.markdown("[Ir a la carta](#letter-section)")