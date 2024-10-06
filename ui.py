import streamlit as st
from PIL import Image
import psycopg2

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
            st.write('Aquí que incluye y en qué consiste el alojamiento')

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
            st.write('Aquí que incluye y en qué consiste el alojamiento')

def cabaña():
    st.title('CABAÑA COLORES')
    st.write("Bienvenidos a Ecoparadise")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
            image = Image.open("assets/cabaña.jpeg")
            st.image(image, use_column_width=True)
        with text_column:
            st.subheader("Cabaña Colores")
            st.write('Aquí que incluye y en qué consiste el alojamiento')


def iniciar_sesion():
    st.title('INICIAR SESIÓN')
    st.write("---")
  
    usuario = st.text_input("Ingrese su nombre de usuario")
    contraseña = st.text_input("Ingrese su contraseña", type="password")

    if st.button("INGRESAR"):
        res = get_all_records(usuario, contraseña)
        if len(res) > 0:
            st.session_state.pagina = 'reserva'  # Cambiamos a la página principal tras el login exitoso
            st.rerun()  # Forzamos recarga para reflejar el cambio
        else:
            st.error("Usuario o contraseña incorrectos")
  
    st.write('Si no tiene cuenta, regístrese aquí.') 
    if st.button("Registrarse"):
        st.session_state.pagina = 'registro'  # Cambiamos a la página de registro
        # registro_usuario()
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

def reserva_glamping():
    st.title("Reserva Glamping")
    st.write("---")

   


def get_connection():
    conn = psycopg2.connect(
        host="localhost",  # Cambia esto a la dirección de tu servidor PostgreSQL
        database="sale-system",  # Cambia esto al nombre de tu base de datos
        user="postgres",  # Cambia esto al usuario de PostgreSQL
        password="1234"  # Cambia esto a tu contraseña de PostgreSQL
    )
    return conn
def get_all_records(name, password):
    conn = get_connection()
    cursor = conn.cursor()
    select_query = "SELECT * FROM mytable"
    # cursor.execute(select_query)
    select_query = "SELECT * FROM mytable WHERE name = %s AND pet = %s"
    cursor.execute(select_query, (name, password))
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records
def create_user(name, password):
    conn = get_connection()
    cursor = conn.cursor()
    insert_query = "INSERT INTO mytable (name, pet) VALUES (%s, %s)"
    cursor.execute(insert_query, (name, password))
    conn.commit()
    cursor.close()
    conn.close()