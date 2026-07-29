import streamlit as st

st.set_page_config(
    page_title="Operation Tracking System",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# SESSION
# ==============================

if "login" not in st.session_state:
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = "Administrator"

if "role" not in st.session_state:
    st.session_state.role = "ADMIN"

if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

# ==============================
# CSS
# ==============================

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

.block-container{
padding-top:0rem;
padding-bottom:0rem;
padding-left:0rem;
padding-right:0rem;
}

html,body,[class*="css"]{

font-family:'Segoe UI';

}

.main{

background:#eef2f7;

}

.login-bg{

height:100vh;

display:flex;

justify-content:center;

align-items:center;

background:linear-gradient(135deg,#2563eb,#0f172a);

}

.login-card{

width:430px;

background:white;

padding:40px;

border-radius:18px;

box-shadow:0px 25px 60px rgba(0,0,0,.25);

}

.logo{

font-size:65px;

text-align:center;

margin-bottom:10px;

}

.title{

font-size:32px;

font-weight:700;

text-align:center;

color:#1e293b;

margin-bottom:5px;

}

.subtitle{

text-align:center;

color:gray;

margin-bottom:25px;

}

.topbar{

height:70px;

background:white;

display:flex;

justify-content:space-between;

align-items:center;

padding-left:30px;

padding-right:30px;

box-shadow:0 4px 20px rgba(0,0,0,.08);

}

.brand{

font-size:24px;

font-weight:bold;

color:#2563eb;

}

.profile{

font-weight:bold;

}

.wrapper{

display:flex;

height:calc(100vh - 70px);

}

.sidebar{

width:240px;

background:#0f172a;

padding:20px;

}

.sidebar button{

width:100%;

margin-bottom:10px;

border:none;

padding:14px;

border-radius:10px;

background:transparent;

color:white;

cursor:pointer;

text-align:left;

font-size:15px;

}

.sidebar button:hover{

background:#2563eb;

}

.content{

flex:1;

padding:30px;

overflow:auto;

}

.card{

background:white;

padding:25px;

border-radius:18px;

box-shadow:0 8px 20px rgba(0,0,0,.08);

margin-bottom:20px;

}

.metric{

font-size:40px;

font-weight:bold;

color:#2563eb;

}

.metric-title{

color:gray;

margin-bottom:10px;

}

</style>
""", unsafe_allow_html=True)

# ==============================
# LOGIN
# ==============================

if not st.session_state.login:

    a,b,c=st.columns([1,1,1])

    with b:

        st.markdown("<br><br><br>",unsafe_allow_html=True)

        st.markdown("<div class='login-card'>",unsafe_allow_html=True)

        st.markdown("<div class='logo'>📦</div>",unsafe_allow_html=True)

        st.markdown("<div class='title'>Operation Tracking</div>",unsafe_allow_html=True)

        st.markdown("<div class='subtitle'>Management System</div>",unsafe_allow_html=True)

        username=st.text_input("Username")

        password=st.text_input("Password",type="password")

        if st.button("LOGIN",use_container_width=True):

            if username=="admin" and password=="admin":

                st.session_state.login=True

                st.rerun()

            else:

                st.error("Username / Password salah")

        st.markdown("</div>",unsafe_allow_html=True)

    st.stop()

# ==============================
# TOPBAR
# ==============================

st.markdown(f"""
<div class="topbar">

<div class="brand">

📦 Operation Tracking System

</div>

<div class="profile">

👤 {st.session_state.user}

</div>

</div>
""",unsafe_allow_html=True)

# ==============================
# MENU
# ==============================

menu=st.sidebar.radio(

"MENU",

[
"🏠 Dashboard",
"🚚 Gate → Container",
"📁 Bundle → MAP",
"📦 Sortir → QC",
"🗄 QC → Arsip",
"📈 Monitoring",
"👥 Master User"
]

)

if st.sidebar.button("Logout"):

    st.session_state.login=False

    st.rerun()

# ==============================
# DASHBOARD
# ==============================

if menu=="🏠 Dashboard":

    st.title("Dashboard")

    c1,c2,c3,c4=st.columns(4)

    with c1:

        st.metric("Gate","120","+5")

    with c2:

        st.metric("MAP","520","+18")

    with c3:

        st.metric("QC","421","+12")

    with c4:

        st.metric("Arsip","398","+9")

    st.divider()

    st.subheader("Recent Activity")

    st.dataframe(

        {

        "Jam":[

        "08:10",

        "08:22",

        "09:10",

        "10:00"

        ],

        "Proses":[

        "Gate",

        "Bundle",

        "QC",

        "Arsip"

        ],

        "Nomor":[

        "RCV001",

        "RCV001",

        "MAP001",

        "MAP001"

        ]

        },

        use_container_width=True,

        hide_index=True

    )

elif menu=="🚚 Gate → Container":

    st.title("🚚 Gate → Container")

    st.caption("Input proses Gate menuju Container")

    with st.form("gate_form", clear_on_submit=False):

        col1,col2=st.columns(2)

        with col1:

            nomor_penerimaan=st.text_input(
                "Nomor Penerimaan",
                placeholder="Contoh : RCV240001"
            )

        with col2:

            kode_container=st.text_input(
                "Kode Container",
                placeholder="Contoh : CONT-001"
            )

        st.divider()

        st.subheader("📷 Dokumentasi")

        foto=st.camera_input(
            "Ambil Foto"
        )

        st.divider()

        st.subheader("✍ Digital Signature")

        tanda_tangan=st.text_area(
            "Nama Penanggung Jawab",
            placeholder="Nama Petugas"
        )

        st.divider()

        timestamp=datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        st.text_input(
            "Timestamp",
            value=timestamp,
            disabled=True
        )

        simpan=st.form_submit_button(
            "💾 SIMPAN",
            use_container_width=True
        )

    if simpan:

        if nomor_penerimaan=="":

            st.error("Nomor penerimaan wajib diisi.")

        elif kode_container=="":

            st.error("Kode Container wajib diisi.")

        elif foto is None:

            st.error("Dokumentasi wajib diambil.")

        elif tanda_tangan=="":

            st.error("Nama petugas wajib diisi.")

        else:

            st.success("Data berhasil disimpan.")

            st.json({

                "Nomor Penerimaan":nomor_penerimaan,

                "Kode Container":kode_container,

                "Petugas":tanda_tangan,

                "Timestamp":timestamp

            })

elif menu=="📁 Bundle → MAP":

    st.title("📁 Bundle → MAP")

    with st.form("bundle"):

        col1,col2=st.columns(2)

        with col1:

            nomor_penerimaan=st.text_input(
                "Nomor Penerimaan"
            )

        with col2:

            nomor_map=st.text_input(
                "Nomor MAP"
            )

        foto=st.camera_input(
            "Dokumentasi"
        )

        petugas=st.text_input(
            "Nama Petugas"
        )

        waktu=datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        st.text_input(
            "Timestamp",
            value=waktu,
            disabled=True
        )

        submit=st.form_submit_button(
            "💾 SIMPAN",
            use_container_width=True
        )

    if submit:

        st.success("Bundle berhasil diproses.")

elif menu=="📦 Sortir → QC":

    st.title("📦 Sortir → QC")

    with st.form("qc"):

        nomor_map=st.text_input(
            "Nomor MAP"
        )

        foto=st.camera_input(
            "Dokumentasi QC"
        )

        petugas=st.text_input(
            "Nama QC"
        )

        waktu=datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        st.text_input(
            "Timestamp",
            value=waktu,
            disabled=True
        )

        submit=st.form_submit_button(
            "💾 SIMPAN",
            use_container_width=True
        )

    if submit:

        st.success("Data QC berhasil disimpan.")

elif menu=="🗄 QC → Arsip":

    st.title("🗄 QC → Arsip")

    with st.form("arsip"):

        nomor_map=st.text_input(
            "Nomor MAP"
        )

        foto=st.camera_input(
            "Dokumentasi Arsip"
        )

        petugas=st.text_input(
            "Nama Petugas Arsip"
        )

        waktu=datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        st.text_input(
            "Timestamp",
            value=waktu,
            disabled=True
        )

        submit=st.form_submit_button(
            "💾 SIMPAN",
            use_container_width=True
        )

    if submit:

        st.success("Dokumen berhasil masuk arsip.")

elif menu=="📈 Monitoring":

    st.title("Monitoring")

elif menu=="👥 Master User":

    st.title("Master User")
