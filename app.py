import streamlit as st
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Mi Closet Virtual", layout="centered")

if 'tema' not in st.session_state: st.session_state.tema = "Morado"
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'inicio'
if 'num_outfit' not in st.session_state: st.session_state.num_outfit = 1

# --- ESTILOS ---
colores = {"Morado": "#6f42c1", "Rosa": "#d63384", "Azul": "#0d6efd"}
st.markdown(f"""
    <style>
        h1 {{ color: {colores[st.session_state.tema]}; text-align: center; }}
        .stButton>button {{ background-color: {colores[st.session_state.tema]}; color: white; }}
    </style>
""", unsafe_allow_html=True)

st.title("👗 Mi Closet Virtual")

# --- LÓGICA DE NAVEGACIÓN ---
p = st.session_state.pantalla

# Pantallas 1-5
if p == 'inicio':
    st.subheader("Iniciar Sesión")
    st.text_input("Nombre")
    st.text_input("First Name")
    st.text_input("Second Last Name")
    if st.button("Registrar"): st.session_state.pantalla = 'exito'; st.rerun()

elif p == 'exito':
    st.success("¡Felicidades, te has registrado con éxito!")
    if st.button("Continuar"): st.session_state.pantalla = 'datos'; st.rerun()

elif p == 'datos':
    st.subheader("Introduce tus datos")
    st.number_input("Talla", 0, 100)
    st.number_input("Peso (kg)", 0, 200)
    st.text_input("Define tu estilo (Ej: Casual)")
    if st.button("Listo"): st.session_state.pantalla = 'procesando'; st.rerun()

elif p == 'procesando':
    with st.spinner('Procesando información...'): time.sleep(2)
    st.session_state.pantalla = 'menu'; st.rerun()

# Pantallas 6-10
elif p == 'menu':
    st.subheader("Menú Principal")
    if st.button("Escanear prenda"): st.session_state.pantalla = 'escanear'; st.rerun()
    if st.button("Colorimetría"): st.session_state.pantalla = 'colorimetria'; st.rerun()
    if st.button("Crear Outfit"): st.session_state.pantalla = 'outfit1'; st.rerun()
    if st.button("Configuración"): st.session_state.pantalla = 'config'; st.rerun()

elif p == 'escanear':
    st.subheader("Escanear")
    st.file_uploader("Cargar imagen de prenda")
    if st.button("Volver"): st.session_state.pantalla = 'menu'; st.rerun()

elif p == 'colorimetria':
    st.subheader("Medir Colorimetría")
    st.write("Análisis de paleta realizado.")
    if st.button("Volver"): st.session_state.pantalla = 'menu'; st.rerun()

# Pantallas 11-15 (Outfits)
elif p.startswith('outfit'):
    st.subheader(f"Outfit sugerido {p[-1]}")
    st.info("Recomendación: Ideal para el clima de hoy.")
    c1, c2, c3 = st.columns(3)
    if c1.button("⬅️"): st.session_state.pantalla = f'outfit{max(1, int(p[-1])-1)}'; st.rerun()
    if c3.button("➡️"): st.session_state.pantalla = f'outfit{min(3, int(p[-1])+1)}'; st.rerun()
    if st.button("Elegir este outfit"): st.session_state.pantalla = 'confirmar'; st.rerun()

elif p == 'confirmar':
    st.success("¡Has elegido tu outfit del día!")
    if st.button("Menú"): st.session_state.pantalla = 'menu'; st.rerun()

# Pantallas 16-20 (Configuración y extras)
elif p == 'config':
    st.subheader("Configuración")
    st.session_state.tema = st.selectbox("Cambiar color", ["Morado", "Rosa", "Azul"])
    st.text_input("Cambiar Nombre de usuario")
    if st.button("Guardar y Volver"): st.session_state.pantalla = 'menu'; st.rerun()
else:
    st.write("Página en desarrollo...")
    if st.button("Regresar"): st.session_state.pantalla = 'menu'; st.rerun()
