import streamlit as st

st.header("Home page")
st.write("hello world")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

tab_login, tab_register = st.tabs(["login", "Register"])

with tab_login:
    if st.button("log in"):
        st.session_state['logged_in'] = True
        st.success("you are now logged in.")

with tab_register:
    st.info("Registration:")
    reg_name = st.text_input("choose a username")
    reg_password = st.text_input("choose a password", type="password")

    if st.button("Register"):
        st.success("Registered successfully!")
