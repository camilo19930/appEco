import streamlit as st
from home_page import pagina_principal, nosotros
from ui import glamping_tres_elementos, Alpes, cabana , iniciar_sesion, registro_usuario, mis_reservas
from utils import css_load

def sidebar():
    # Si no existe 'pagina' en session_state, inicialízala
    if 'pagina' not in st.session_state:
        st.session_state.pagina = 'pagina principal'
    
    st.sidebar.title('Menú de navegación')
    
    # Usamos el valor guardado en session_state para el selectbox
    pagina = st.sidebar.selectbox('Selecciona una página', 
                                  ['pagina principal', 'glamping tres elementos', 
                                   'glamping los alpes', 'cabaña colores', 'login','registro', 'reserva' ], 
                                  index=['pagina principal', 
                                         'glamping tres elementos', 
                                         'glamping los alpes', 
                                         'cabaña colores', 'login', 'registro', 'reserva'].index(st.session_state.pagina))

    # Guardamos la selección en el estado de sesión
    st.session_state.pagina = pagina
    
    boton = st.sidebar.button("login")
    if boton:
        st.session_state.pagina = 'login'  # Cambiamos a la página de login
        st.rerun()  # Recargamos la página para reflejar el cambio

    # Dependiendo del valor en session_state, se carga una página u otra
    if st.session_state.pagina == 'login':
        iniciar_sesion()  # Aquí deberías manejar la lógica de login
    elif st.session_state.pagina == 'pagina principal':
        pagina_principal()
        nosotros()
    elif st.session_state.pagina == 'glamping tres elementos':
        glamping_tres_elementos()
    elif st.session_state.pagina == 'glamping los alpes':
        Alpes()
    elif st.session_state.pagina == 'cabaña colores':
        cabana()
    elif st.session_state.pagina == 'registro':
        registro_usuario()
    elif st.session_state.pagina == 'reserva':
        mis_reservas()

if __name__ == "__main__":
    css_load("style/main.css")
    sidebar()
