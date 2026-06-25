import streamlit as st
import random

# --- CONFIGURACIÓN Y ESTILO ---
st.set_page_config(page_title="Mi Closet Virtual", layout="centered")

# Lógica de Tema (CSS Dinámico)
temas = {
    "Rosa": {"fondo": "#fdf6f0", "card": "#ffffff", "btn": "#ffccd5"},
    "Azul": {"fondo": "#f0f8ff", "card": "#e6f3ff", "btn": "#87ceeb"},
    "Negro": {"fondo": "#2c2c2c", "card": "#3e3e3e", "btn": "#555555"}
}

if 'tema' not in st.session_state: st.session_state.tema = "Rosa"
t = temas[st.session_state.tema]

st.markdown(f"""
    <style>
        .main {{ background-color: {t['fondo']}; }}
        .header-box {{ background-color: {t['btn']}; padding: 20px; border-radius: 30px; text-align: center; }}
        .stButton>button {{ border-radius: 20px; background-color: {t['btn']}; border: none; }}
    </style>
""", unsafe_allow_html=True)

# --- ESTADO GLOBAL ---
if 'p' not in st.session_state: st.session_state.p = 'registro'
if 'user' not in st.session_state: 
    st.session_state.user = {'u': 'Usuario', 'foto': None, 'cal': False, 'clima': False}

# --- NAVEGACIÓN ---
def ir(p): st.session_state.p = p; st.rerun()

p = st.session_state.p

# 1. FLUJO DE REGISTRO
if p == 'registro':
    st.markdown('<div class="header-box"><h1>👗 Registro</h1></div>', unsafe_allow_html=True)
    st.session_state.user['n'] = st.text_input("Nombre"); st.session_state.user['a'] = st.text_input("Apellido")
    st.session_state.user['u'] = st.text_input("Nombre de Usuario")
    if st.button("Siguiente"): ir('datos')

elif p == 'datos':
    st.selectbox("Género", ["Femenino", "Masculino", "Prefiero no decirlo"])
    st.number_input("Talla (cm)", 50, 250); st.number_input("Peso (kg)", 10, 300)
    st.session_state.user['foto'] = st.file_uploader("Foto de perfil")
    if st.button("Finalizar"): ir('home')

# 2. HOME
elif p == 'home':
    if st.session_state.user['foto']: st.image(st.session_state.user['foto'], width=60)
    st.write(f"### {st.session_state.user['u']}")
    if st.button("⚙️ Configuración"): ir('config')
    st.markdown('<div class="header-box"><h1>Mi Closet Virtual</h1></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📸 Escanear"): ir('escanear')
        if st.button("📁 Cargar"): ir('galeria')
    with col2:
        if st.button("🎨 Colorimetría"): ir('colorimetria')
        if st.button("✨ Crear Outfit"): ir('outfit')
    
    st.button("🤖 Elegir Asistente", on_click=lambda: ir('asistente_selector'))

# 3. MÓDULOS DE ASISTENTE Y CONFIG
elif p == 'asistente_selector':
    st.subheader("Selecciona tu asistente")
    if st.button("Asistente Femenino"): st.success("Elegido Femenino"); ir('home')
    if st.button("Asistente Masculino"): st.success("Elegido Masculino"); ir('home')
    if st.button("Volver"): ir('home')

elif p == 'config':
    st.title("Configuración")
    # Cambiar tema (esto recarga la página y cambia el color)
    st.session_state.tema = st.selectbox("Cambiar Tema", ["Rosa", "Azul", "Negro"])
    st.session_state.user['idioma'] = st.selectbox("Idioma", ["Español", "English"])
    
    # Vinculación lógica
    if st.button("Vincular/Desvincular Calendario"): st.session_state.user['cal'] = not st.session_state.user['cal']
    st.write(f"Estado Calendario: {'Vinculado' if st.session_state.user['cal'] else 'No vinculado'}")
    
    if st.button("Vincular/Desvincular Clima"): st.session_state.user['clima'] = not st.session_state.user['clima']
    
    if st.button("Cerrar Sesión"): ir('registro')
    if st.button("ELIMINAR CUENTA"): ir('registro')
    if st.button("Volver"): ir('home')

# (Resto de pantallas como escanear/galería/outfit permanecen igual)

# (Las otras pantallas como escanear/galería/colorimetría siguen el mismo patrón)
# Añadir lógica para completar hasta 20 pantallas...
