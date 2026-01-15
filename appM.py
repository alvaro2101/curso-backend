import streamlit as st
from PIL import Image

# 1. Configuración de la página
st.set_page_config(
    page_title="Nuestra Historia Juntos",
    page_icon="❤️",
    layout="centered"
)

# 2. Título y mensaje principal
st.title("❤️ Feliz Aniversario, Amor ❤️")
st.write("He creado esta cápsula del tiempo para recordar nuestros mejores momentos.")
st.write("---")

# 3. Datos de la historia (Aquí es donde editarás luego)
# Puedes agregar tantos momentos como quieras a esta lista
momentos = [
    {
        "fecha": "30/07/25",
        "titulo": "El inicio de todo",
        "descripcion": "En el momento en el te entrege la carta y te di la cadenita, estaba muy nervioso.",
        "icono": "❤️" 
    },
    {
        "fecha": "30/08/25",
        "titulo": "Nuestro primer mes",
        "descripcion": "Poco a poco nos fuimos conociendo, aunque a la vista de todos parece que vamos muy rapido para mi eres lo mejor que Dios me a dado.",
        "icono": "❤️"
    },
    {
        "fecha": "30/09/25",
        "titulo": "Nuestro segundo mes",
        "descripcion": "Fue nuestra cita al cine, fuimos a ver KNY como buenos otakus jsjsjsj.",
        "icono": "❤️"
    },
    {
        "fecha": "30/10/25",
        "titulo": "Nuestro tercer mes ",
        "descripcion": "Algunas peleas a lo largo de nuestra relacion, pero nada que no lo podriamos superar juntos.",
        "icono": "❤️"
    },
    {
        "fecha": "30/11/25",
        "titulo": "Nuestro cuarto mes",
        "descripcion": "Gracias por cada día juntos, me enseñas a quererte cada dia un poco mas.",
        "icono": "❤️"
    },
    {
        "fecha": "30/12/25",
        "titulo": "Nuestro quinto mes",
        "descripcion": "Aunque navidad la pasamos cada uno en su casita, me encanto pasar año nuevo a tu lado.",
        "icono": "❤️"
    }

]

# 4. Lógica para mostrar la línea de tiempo
for evento in momentos:
    with st.container():
        # Usamos columnas para que se vea ordenado (Columna pequeña para icono, grande para texto)
        col1, col2 = st.columns([1, 5])
        
        with col1:
            st.header(evento["icono"])
        
        with col2:
            st.subheader(f"{evento['fecha']} - {evento['titulo']}")
            st.write(evento["descripcion"])
            
    st.divider() # Línea separadora

# 5. Un detalle final en la barra lateral
st.sidebar.title("Dedicatoria")
st.sidebar.write("Creado con mucho amor y Python para ti.")
st.sidebar.balloons() # ¡Efecto de globos al cargar!