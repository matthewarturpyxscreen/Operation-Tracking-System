import streamlit as st
from database.supabase import supabase

st.title("Operation Tracking System")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("LOGIN"):

    try:

        response = supabase.auth.sign_in_with_password({

            "email": email,

            "password": password

        })

        st.session_state.user = response.user

        st.success("Login Berhasil")

        st.rerun()

    except Exception as e:

        st.error("Email atau Password salah")
