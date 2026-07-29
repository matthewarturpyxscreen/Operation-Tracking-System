import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================================
# CONFIG
# ==========================================================
st.set_page_config(
    page_title="Operation Tracking System",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================
st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:20px;
padding-bottom:20px;
padding-left:2rem;
padding-right:2rem;
}

html,body{
background:#f5f7fb;
}

.main-title{
font-size:40px;
font-weight:800;
color:#1e293b;
margin-bottom:0px;
}

.sub-title{
font-size:15px;
color:#64748b;
margin-top:-10px;
margin-bottom:30px;
}

.metric-card{

background:white;

padding:25px;

border-radius:18px;

box-shadow:0px 10px 30px rgba(0,0,0,.08);

border:1px solid #ececec;

transition:.3s;

}

.metric-card:hover{

transform:translateY(-5px);

}

.metric-title{

font-size:14px;

color:#64748b;

}

.metric-value{

font-size:38px;

font-weight:700;

color:#2563eb;

}

.sidebar-title{

font-size:20px;

font-weight:bold;

}

.login-box{

background:white;

padding:40px;

border-radius:20px;

box-shadow:0px 20px 50px rgba(0,0,0,.15);

}

.stButton>button{

width:100%;

height:48px;

border-radius:12px;

font-weight:bold;

background:#2563eb;

color:white;

border:none;

}

.stButton>button:hover{

background:#1d4ed8;

}

</style>
""",unsafe_allow_html=True)

# ==========================================================
# SESSION
# ==========================================================
if "login" not in st.session_state:
    st.session_state.login=False

if "nama" not in st.session_state:
    st.session_state.nama=""

if "role" not in st.session_state:
    st.session_state.role=""

# ==========================================================
# DUMMY LOGIN
# NANTI DIGANTI SUPABASE
# ==========================================================

USER="admin"

PASSWORD="admin123"

def login_page():

    col1,col2,col3=st.columns([1,1.2,1])

    with col2:

        st.markdown("<br><br>",unsafe_allow_html=True)

        st.markdown("<div class='login-box'>",unsafe_allow_html=True)

        st.markdown("<h1 style='text-align:center;'>📦</h1>",unsafe_allow_html=True)

        st.markdown(
        "<h2 style='text-align:center;'>Operation Tracking System</h2>",
        unsafe_allow_html=True)

        st.write("")

        username=st.text_input("Username")

        password=st.text_input(
            "Password",
            type="password"
        )

        st.write("")

        if st.button("LOGIN"):

            if username==USER and password==PASSWORD:

                st.session_state.login=True

                st.session_state.nama="Administrator"

                st.session_state.role="ADMIN"

                st.rerun()

            else:

                st.error("Username / Password salah.")

        st.markdown("</div>",unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

def sidebar():

    st.sidebar.markdown("## 📦 Operation Tracking")

    st.sidebar.success(st.session_state.nama)

    st.sidebar.caption(st.session_state.role)

    st.sidebar.divider()

    menu=st.sidebar.radio(

        "Menu",

        [

            "Dashboard",

            "Gate → Container",

            "Bundle → MAP",

            "Sortir → QC",

            "QC → Arsip",

            "Monitoring",

            "Master User"

        ]

    )

    st.sidebar.divider()

    if st.sidebar.button("Logout"):

        st.session_state.login=False

        st.rerun()

    return menu

# ==========================================================
# DASHBOARD
# ==========================================================

def dashboard():

    st.markdown(
        """
        <h1 class='main-title'>📊 Operation Tracking System</h1>
        <p class='sub-title'>
        Welcome back, Administrator
        </p>
        """,
        unsafe_allow_html=True
    )

    c1,c2,c3,c4=st.columns(4)

    with c1:

        st.markdown("""
        <div class='metric-card'>
            <div class='metric-title'>
            Total Container
            </div>

            <div class='metric-value'>
            125
            </div>
        </div>
        """,unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class='metric-card'>
            <div class='metric-title'>
            Total MAP
            </div>

            <div class='metric-value'>
            532
            </div>
        </div>
        """,unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class='metric-card'>
            <div class='metric-title'>
            Total QC
            </div>

            <div class='metric-value'>
            487
            </div>
        </div>
        """,unsafe_allow_html=True)

    with c4:

        st.markdown("""
        <div class='metric-card'>
            <div class='metric-title'>
            Total Arsip
            </div>

            <div class='metric-value'>
            421
            </div>
        </div>
        """,unsafe_allow_html=True)

    st.write("")

    left,right=st.columns([2,1])

    with left:

        st.subheader("📈 Recent Activity")

        df=pd.DataFrame({

            "Jam":[
                "08:10",
                "08:15",
                "08:22",
                "08:40"
            ],

            "Proses":[
                "Gate → Container",
                "Bundle → MAP",
                "Sortir → QC",
                "QC → Arsip"
            ],

            "Nomor":[
                "RCV001",
                "RCV002",
                "MAP001",
                "MAP001"
            ]

        })

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    with right:

        st.subheader("📌 Progress")

        st.progress(.85)

        st.metric(
            "Today's Progress",
            "85%"
        )
    st.title(menu)

    st.write("Halaman masih dalam tahap development.")
    
