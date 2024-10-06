import streamlit as st
from utils import css_load, contacto

email_contact = "marcelatamayo53@gmail.com"

def pagina_principal():
    st.write("Bienvenidos a Ecoparadise")
    st.write('usa el menú de la izquierda para navegar')

def nosotros():
    with st.container():
        st.header("Somos Ecoparadise 👋")
        st.title("¡Sueña, explora y descubre!")
        st.write(
            "Somos un hotel ecológico, apasionados por la naturaleza y rodeados de ambientes llenos de tranquilidad y paz. Ubicados en el corregimiento de La Marina, a 20 minutos de Tuluá, Valle del Cauca."
        )
    with st.container():
        st.write("---")
        st.header("Sobre nosotros 🔍")
        st.write(
            """
            Hola 👋 Encontraste el lugar que estabas buscando...
            Ecoparadise es un conjunto de emociones inolvidables.
            Permítenos hacer realidad la noche de tus sueños... Te estamos esperando ♥
            """
        )
    contacto(email_contact)

