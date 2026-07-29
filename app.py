import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Operation Tracking System",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("📦 Operation Tracking System")

menu = st.sidebar.radio(
    "Menu",
    [
        "Dashboard",
        "Gate → Container",
        "Bundle → MAP",
        "Sortir → QC",
        "QC → Arsip",
        "Monitoring"
    ]
)

# =========================
# HALAMAN
# =========================
if menu == "Dashboard":
    st.title("📊 Dashboard")
    st.write("Halaman Dashboard")

elif menu == "Gate → Container":
    st.title("🚚 Gate → Container")
    st.write("Form Gate → Container")

elif menu == "Bundle → MAP":
    st.title("📁 Bundle → MAP")
    st.write("Form Bundle → MAP")

elif menu == "Sortir → QC":
    st.title("📦 Sortir → QC")
    st.write("Form Sortir → QC")

elif menu == "QC → Arsip":
    st.title("🗄 QC → Arsip")
    st.write("Form QC → Arsip")

elif menu == "Monitoring":
    st.title("📈 Monitoring")
    st.write("Halaman Monitoring")
