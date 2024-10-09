import streamlit as st
from PIL import Image
import psycopg2
from db import get_generic_all_records, create_user, get_all_records, create_reserva

def glamping_tres_elementos():
    st.title('GLAMPING TRES ELEMENTOS')
    st.write("Bienvenidos a Ecoparadise")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
            image = Image.open("assets/gte.jpeg")
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader("Glamping Tres Elementos")
            st.write('El glamping tres elementos es un domo geodésico equipado con todo lo de un hotel convencional, es una experiencia diferente a lo que comúnmente conocemos sin dejar de lado la comodidad y la experiencia en un medio muy natural, sus atardeceres desde nuestro jacuzzi son lo máximo ❤️')

def Alpes():
    st.title('GLAMPING LOS ALPES')
    st.write("Bienvenidos a Ecoparadise")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
            image = Image.open("assets/alpes.jpeg")
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader("Glamping Los Alpes")
            st.write('Nuestro glamping Los Alpes tiene una particular infraestructura en forma de pirámide, está rodeada de árboles frutales y nos permite la oportunidad de observar atardeceres hermosos desde la malla catamaran 🌅')

def cabana():
    st.title('cabana COLORES')
    st.write("Bienvenidos a Ecoparadise")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
            image = Image.open("assets/cabana.jpeg")
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader("cabana Colores")
            st.write('La cabana Colores es todo lo que necesitas para descansar, está construida en guadua y es el alojamiento más grande que tiene Ecoparadise, es perfecto para parejas, familia y amigos por su amplio espacio.')


def iniciar_sesion():
    st.title('INICIAR SESIÓN')
    st.write("---")
  
    usuario = st.text_input("Ingrese su nombre de usuario")
    contraseña = st.text_input("Ingrese su contraseña", type="password")

    if st.button("INGRESAR"):
        res = get_all_records(usuario, contraseña)
        if len(res) > 0:
            # Guardar los datos del usuario en session_state
            st.session_state['usuario'] = {
                'nombre': usuario,
                'datos': res  # Aquí puedes guardar todos los datos que obtuviste de la base de datos
            }
            st.session_state.pagina = 'reserva'  # Cambiamos a la página principal tras el login exitoso
            st.rerun()  # Forzamos recarga para reflejar el cambio
        else:
            st.error("Usuario o contraseña incorrectos")
  
    st.write('Si no tiene cuenta, regístrese aquí.') 
    if st.button("Registrarse"):
        st.session_state.pagina = 'registro'  # Cambiamos a la página de registro
        st.rerun() 
           

def registro_usuario():
    st.title("Registro de Usuario")
    st.write("---")

    # Formulario de registro
    nombre = st.text_input("Ingrese su nombre de usuario")
    contraseña = st.text_input("Ingrese su contraseña", type="password")
    confirmar_contraseña = st.text_input("Confirme su contraseña", type="password")

    if st.button("Registrar"):
        # Validación básica
        if contraseña != confirmar_contraseña:
            st.error("Las contraseñas no coinciden.")
        elif len(nombre) == 0 or len(contraseña) == 0:
            st.error("Todos los campos son obligatorios.")
        else:
            # Llamamos a la función que inserta el usuario en la base de datos
            create_user(nombre, contraseña)
            st.success("Usuario registrado exitosamente.")
            st.session_state.pagina = 'reserva'  # Redirigir a la página principal
            st.rerun()  # Recargar la página
    

import streamlit as st

def mis_reservas():
    st.title("Mis Reservas")
    st.write("---")
    dataUser = {}
    
    if 'usuario' in st.session_state:
        dataUser = st.session_state['usuario']['datos']
        usuario = st.session_state['usuario']['nombre']
        st.write(f"Bienvenido, {usuario}")
    else:
        st.warning("Por favor, inicie sesión para ver sus reservas.")
        
    fecha_reserva = st.date_input("Selecciona la fecha de tu reserva")
    dias_reserva = st.text_input("Ingrese la cantidad de días de la reserva")
    records = get_generic_all_records("SELECT * FROM cabanas")
    # Crear un diccionario donde la clave es el ID (elementos[0]) y el valor es el nombre (elementos[3])
    dict_cabanas = {elementos[0]: elementos[3] for elementos in records}
    # Crear una lista de los valores (nombres de cabanas) para mostrar en el selectbox
    cabanas = list(dict_cabanas.values())
    # Mostrar selectbox
    cabana_seleccionada_nombre = st.selectbox("Selecciona tu cabana", cabanas)
    
    # Obtener la clave correspondiente al valor seleccionado
    cabana_seleccionada_id = next(key for key, value in dict_cabanas.items() if value == cabana_seleccionada_nombre)
    comprobante = st.file_uploader("Adjunta tu comprobante de pago", type=["png", "jpg", "pdf"])
    
    if st.button("Confirmar reserva"):
        if comprobante:
            st.success(f"Reserva confirmada para el {fecha_reserva} en la cabana '{cabana_seleccionada_nombre}' (ID: {cabana_seleccionada_id}). Comprobante recibido.")
            create_reserva(fecha_reserva, dias_reserva, cabana_seleccionada_id, dataUser[0][0])
            st.success("Reserva Creada exitosamente.")
            
        else:
            st.error("Por favor, adjunta tu comprobante de pago.")


 
