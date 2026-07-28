import streamlit as st

st.set_page_config(
    page_title="Operation Tracking System",
    page_icon="📦",
    layout="wide",
)

st.title("📦 Operation Tracking System")

st.divider()

st.subheader("Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

login = st.button(
    "Login",
    use_container_width=True
)

if login:

    st.success("Login berhasil (sementara)")
