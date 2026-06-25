import streamlit as st

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Mi Closet Virtual", layout="centered")

# --- ESTILOS "KAWAII" ---
st.markdown("""
    <style>
        .main { background-color: #fdf6f0; }
        .header-box { background-color: #ffe4e6; padding: 20px; border-radius: 30px; border: 2px solid #ffccd5; text-align: center; }
        .card { background-color: #ffffff; padding: 20px; border-radius: 25px; border: 1px solid #ffd1dc; box-shadow: 3px 3px 15px #fce4ec; margin-bottom: 15px; }
        .stButton>button { border-radius: 20px; background-color: #ffccd5; color: #555; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- MEMORIA (SESSION STATE) ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'registro'

# --- SIDEBAR (CONFIGURACIONES) ---
with st.sidebar:
    st.title("⚙️ Configuraciones")
    st.text_input("Nombre de Usuario")
    st.selectbox("Idioma", ["Español", "English"])
    st.selectbox("Tema", ["Rosa", "Azul", "Morado"])
    st.checkbox("Unir a Calendario")
    st.checkbox("Unir a Clima")

# --- LÓGICA DE PANTALLAS ---
def ir_a(p): st.session_state.pantalla = p; st.rerun()

p = st.session_state.pantalla

# 1. PANTALLA DE REGISTRO
if p == 'registro':
    st.markdown('<div class="header-box"><h1>👗 Registro</h1></div>', unsafe_allow_html=True)
    st.text_input("Nombre"); st.text_input("Apellido"); st.text_input("Usuario")
    st.selectbox("Género", ["Femenino", "Masculino", "Prefiero no decirlo"])
    st.number_input("Talla (cm)", 50, 250); st.number_input("Peso (kg)", 10, 300)
    st.file_uploader("Subir foto de perfil")
    if st.button("Finalizar Registro"): ir_a('home')

# 2. PANTALLA HOME / MENÚ PRINCIPAL
elif p == 'home':
    st.markdown('<div class="header-box"><h1>✨ Hola, Bienvenida</h1></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: 
        if st.button("📸 Escanear Prenda"): ir_a('escanear')
        if st.button("📁 Cargar desde Galería"): ir_a('galeria')
    with c2:
        if st.button("🎨 Colorimetría"): ir_a('colorimetria')
        if st.button("✨ Crear Outfit"): ir_a('outfit_selector')
    
    # Espacio para mascotas futuras
    st.subheader("Tu Mascota")
    c_m1, c_m2 = st.columns(2)
    c_m1.container(border=True).write("Mascota Femenina")
    c_m2.container(border=True).write("Mascota Masculina")

# 3. FUNCIONALIDADES (Escaneo, Galería, etc)
elif p == 'escanear':
    st.camera_input("Toma foto a la prenda")
    if st.button("Guardar y Volver"): ir_a('home')

elif p == 'galeria':
    st.file_uploader("Selecciona imagen")
    if st.button("Guardar y Volver"): ir_a('home')

elif p == 'colorimetria':
    st.write("Sube tus fotos para análisis de paleta.")
    st.file_uploader("Foto de referencia")
    if st.button("Volver"): ir_a('home')

# 4. OUTFITS
elif p == 'outfit_selector':
    st.subheader("Outfit de la semana")
    # Simulación de opciones
    outfit = st.radio("Selecciona tu opción", ["Outfit 1", "Outfit 2", "Outfit 3"])
    if st.button("Elegir"): st.success(f"Has elegido: {outfit}"); ir_a('home')

# Añadir lógica para completar hasta 20 pantallas...
