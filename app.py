import streamlit as st
import random

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Mi Closet Virtual", layout="centered")

# Lógica de Temas
temas = {
    "Rosa": {"fondo": "#fdf6f0", "btn": "#ffccd5", "header": "#ffe4e6"},
    "Azul": {"fondo": "#f0f8ff", "btn": "#87ceeb", "header": "#e6f3ff"},
    "Morado": {"fondo": "#f8f0ff", "btn": "#d8b4fe", "header": "#ede9fe"}
}

if 'tema' not in st.session_state: st.session_state.tema = "Rosa"
t = temas[st.session_state.tema]

st.markdown(f"""
    <style>
        .stApp {{ background-color: {t['fondo']}; }}
        .header-box {{ background-color: {t['header']}; padding: 20px; border-radius: 30px; text-align: center; }}
        .stButton>button {{ border-radius: 20px; background-color: {t['btn']}; border: none; font-weight: bold; width: 100%; }}
    </style>
""", unsafe_allow_html=True)

# --- ESTADO GLOBAL ---
if 'p' not in st.session_state: st.session_state.p = 'registro'
if 'user' not in st.session_state: st.session_state.user = {'u': 'Usuario', 'foto': None}
if 'closet' not in st.session_state: st.session_state.closet = []

def ir(p): st.session_state.p = p; st.rerun()

# --- NAVEGACIÓN DE PANTALLAS ---
p = st.session_state.p

# 1. REGISTRO
if p == 'registro':
    st.markdown('<div class="header-box"><h1>👗 Registro</h1></div>', unsafe_allow_html=True)
    st.text_input("Nombre"); st.text_input("Apellido"); st.session_state.user['u'] = st.text_input("Usuario")
    if st.button("Siguiente"): ir('exito_reg')

elif p == 'exito_reg':
    st.success("¡Registro exitoso!")
    if st.button("Continuar"): ir('datos')

elif p == 'datos':
    st.selectbox("Género", ["Femenino", "Masculino", "Prefiero no decirlo"])
    st.number_input("Talla (cm)", 50, 250); st.number_input("Peso (kg)", 10, 300)
    st.session_state.user['foto'] = st.file_uploader("Foto de perfil")
    if st.button("Finalizar"): ir('vinculacion')

elif p == 'vinculacion':
    st.checkbox("Vincular Calendario"); st.checkbox("Vincular Clima")
    if st.button("Confirmar"): ir('home')

# 2. HOME
elif p == 'home':
    c1, c2 = st.columns([1, 4])
    with c1: 
        if st.session_state.user['foto']: st.image(st.session_state.user['foto'], width=50)
    with c2: st.write(f"**{st.session_state.user['u']}**")
    
    if st.button("⚙️ Configuración"): ir('config')
    st.markdown('<div class="header-box"><h1>Mi Closet Virtual</h1></div>', unsafe_allow_html=True)
    st.info(random.choice(["¡Hoy tendrás un día excelente!", "Hoy es un día para brillar.", "¡Eres grandiosa!"]))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📸 Escanear"): ir('escanear')
        if st.button("📁 Cargar"): ir('galeria')
    with col2:
        if st.button("🎨 Colorimetría"): ir('colorimetria')
        if st.button("✨ Crear Outfit"): ir('outfit')
    st.button("🤖 Elegir Asistente", on_click=lambda: ir('asistente'))

# 3. FUNCIONALIDADES RESTAURADAS
elif p == 'escanear':
    st.subheader("Escanear prenda")
    img_cam = st.camera_input("Usa tu cámara") # <--- AQUÍ ESTÁ LA CÁMARA
    if img_cam:
        if st.button("Guardar en Closet"): st.session_state.closet.append(img_cam); ir('home')
    if st.button("Volver"): ir('home')

elif p == 'galeria':
    archivo = st.file_uploader("Subir desde galería")
    if archivo and st.button("Guardar"): st.session_state.closet.append(archivo); ir('home')
    if st.button("Volver"): ir('home')

elif p == 'colorimetria':
    st.file_uploader("Subir foto")
    if st.button("Analizar"): st.success("Análisis realizado"); ir('home')
    if st.button("Volver"): ir('home')

elif p == 'outfit':
    st.radio("Opciones:", ["Outfit 1", "Outfit 2", "Outfit 3"])
    if st.button("Elegir"): ir('home')
    if st.button("Volver"): ir('home')

elif p == 'asistente':
    if st.button("Asistente Femenino"): ir('home')
    if st.button("Asistente Masculino"): ir('home')
    if st.button("Volver"): ir('home')

elif p == 'config':
    st.title("Configuración")
    st.session_state.tema = st.selectbox("Cambiar Tema", ["Rosa", "Azul", "Morado"])
    st.selectbox("Idioma", ["Español", "English"])
    if st.button("Cerrar Sesión"): ir('registro')
    if st.button("Volver"): ir('home')

# (Nota: Puedes repetir el bloque elif para las 20 pantallas)

# (Resto de pantallas como escanear/galería/outfit permanecen igual)

# (Las otras pantallas como escanear/galería/colorimetría siguen el mismo patrón)
# Añadir lógica para completar hasta 20 pantallas...
