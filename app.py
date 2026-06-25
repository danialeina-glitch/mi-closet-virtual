import streamlit as st
import random

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Mi Closet Virtual", layout="centered")

# --- LÓGICA DE TEMAS Y IDIOMA ---
temas = {
    "Rosa": {"fondo": "#fdf6f0", "btn": "#ffccd5", "header": "#ffe4e6"},
    "Azul": {"fondo": "#f0f8ff", "btn": "#87ceeb", "header": "#e6f3ff"},
    "Morado": {"fondo": "#f8f0ff", "btn": "#d8b4fe", "header": "#ede9fe"}
}

if 'tema' not in st.session_state: st.session_state.tema = "Rosa"
if 'idioma' not in st.session_state: st.session_state.idioma = "Español"

# Aplicar estilo dinámico
t = temas[st.session_state.tema]
st.markdown(f"""
    <style>
        .stApp {{ background-color: {t['fondo']}; }}
        .header-box {{ background-color: {t['header']}; padding: 20px; border-radius: 30px; text-align: center; }}
        .stButton>button {{ border-radius: 20px; background-color: {t['btn']}; border: none; font-weight: bold; }}
    </style>
""", unsafe_allow_html=True)

# --- ESTADO GLOBAL ---
if 'p' not in st.session_state: st.session_state.p = 'registro'
if 'user' not in st.session_state: st.session_state.user = {'u': 'Usuario', 'foto': None}

# --- NAVEGACIÓN ---
def ir(p): st.session_state.p = p; st.rerun()

p = st.session_state.p

# 1. FLUJO DE REGISTRO
if p == 'registro':
    st.markdown('<div class="header-box"><h1>👗 Registro</h1></div>', unsafe_allow_html=True)
    st.text_input("Nombre"); st.text_input("Apellido"); st.session_state.user['u'] = st.text_input("Usuario")
    if st.button("Siguiente"): ir('exito_reg')

elif p == 'exito_reg':
    st.success("¡Tu registro ha sido exitoso!")
    if st.button("Continuar"): ir('datos')

elif p == 'datos':
    st.selectbox("Género", ["Femenino", "Masculino", "Prefiero no decirlo"])
    st.number_input("Talla (cm)", 50, 250); st.number_input("Peso (kg)", 10, 300)
    st.session_state.user['foto'] = st.file_uploader("Subir foto perfil")
    if st.button("Finalizar"): ir('vinculacion')

elif p == 'vinculacion':
    st.write("### Vincular herramientas")
    st.checkbox("Vincular Calendario"); st.checkbox("Vincular Clima")
    if st.button("Confirmar vinculación"): st.success("¡Éxito!"); ir('home')

# 2. HOME
elif p == 'home':
    col1, col2 = st.columns([1, 4])
    with col1: 
        if st.session_state.user['foto']: st.image(st.session_state.user['foto'], width=50)
    with col2: st.write(f"**{st.session_state.user['u']}**")
    
    # Botón configuración a la derecha
    if st.button("⚙️ Configuración"): ir('config')
    st.markdown('<div class="header-box"><h1>Mi Closet Virtual</h1></div>', unsafe_allow_html=True)
    
    # Mensajes
    st.info(random.choice(["¡Hoy tendrás un día excelente!", "Hoy es un día para brillar.", "¡Eres grandiosa!"]))
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📸 Escanear"): ir('escanear')
        if st.button("📁 Cargar"): ir('galeria')
    with col2:
        if st.button("🎨 Colorimetría"): ir('colorimetria')
        if st.button("✨ Crear Outfit"): ir('outfit')
    
    if st.button("🤖 Elegir Asistente"): ir('asistente')

# 3. MÓDULOS Y CONFIG
elif p == 'config':
    st.title("Configuración")
    st.session_state.tema = st.selectbox("Cambiar Tema", ["Rosa", "Azul", "Morado"])
    st.session_state.idioma = st.selectbox("Idioma", ["Español", "English"])
    if st.button("Cerrar Sesión"): ir('registro')
    if st.button("Volver al Inicio"): ir('home')

elif p == 'asistente':
    if st.button("Asistente Femenino"): st.success("Seleccionado"); ir('home')
    if st.button("Asistente Masculino"): st.success("Seleccionado"); ir('home')
    if st.button("Volver"): ir('home')

# (Nota: Puedes repetir el bloque elif para las 20 pantallas)

# (Resto de pantallas como escanear/galería/outfit permanecen igual)

# (Las otras pantallas como escanear/galería/colorimetría siguen el mismo patrón)
# Añadir lógica para completar hasta 20 pantallas...
