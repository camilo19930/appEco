import streamlit as st
import requests

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

def contacto(email_contact):
    with st.container():
        st.write("---")
        st.header("Ponte en contacto con nosotros!")
        st.write("##")
        contact_form = f"""
        <form action="https://formsubmit.co/{email_contact}" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Tu nombre" required>
            <input type="email" name="email" placeholder="Tu email" required>
            <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
            <button type="submit">Enviar</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
