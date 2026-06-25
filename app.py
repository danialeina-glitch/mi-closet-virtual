import streamlit as st
import random
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Mi Closet Virtual", layout="centered")

# --- ESTILOS KAWAI ---
st.markdown("""
    <style>
        .main { background-color: #fdf6f0; }
        .header-box { background-color: #ffe4e6; padding: 20px; border-radius: 30px; border: 2px solid #ffccd5; text-align: center; }
        .card { background-color: #ffffff; padding: 20px; border-radius: 25px; border: 1px solid #ffd1dc; box-shadow: 3px 3px 15px #fce4ec; margin-bottom: 15px; }
        .stButton>button { border-radius: 20px; background-color: #ffccd5; color: #555; font-weight: bold; width: 100%; }
        .profile-bar { display: flex; align-items: center; gap: 15px; padding: 10px; background: #fffafc; border-radius: 20px; border: 1px solid #ffccd5; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- ESTADO GLOBAL ---
if 'p' not in st.session_state: st.session_state.p = 'registro'
if 'user' not in st.session_state: 
    st.session_state.user = {'n': '', 'a': '', 'u': '', 'gen': '', 't': 0, 'p': 0, 'foto': None, 'idioma': 'Español', 'tema': 'Rosa'}
if 'closet' not in st.session_state: st.session_state.closet = []
if 'asistente' not in st.session_state: st.session_state.asistente = None

# --- FUNCIONES DE NAVEGACIÓN ---
def ir(p): st.session_state.p = p; st.rerun()

# 1. REGISTRO
if st.session_state.p == 'registro':
    st.markdown('<div class="header-box"><h1>👗 Registro</h1></div>', unsafe_allow_html=True)
    st.session_state.user['n'] = st.text_input("Nombre")
    st.session_state.user['a'] = st.text_input("Apellido")
    st.session_state.user['u'] = st.text_input("Nombre de Usuario")
    if st.button("Siguiente"): ir('datos')

elif st.session_state.p == 'datos':
    st.session_state.user['gen'] = st.selectbox("Género", ["Femenino", "Masculino", "Prefiero no decirlo"])
    st.session_state.user['t'] = st.number_input("Talla (cm)", 50, 250)
    st.session_state.user['p'] = st.number_input("Peso (kg)", 10, 300)
    st.session_state.user['foto'] = st.file_uploader("Sube tu foto de perfil", type=['jpg', 'png'])
    st.success("¡Felicidades, registro exitoso!")
    if st.button("Ir al Closet"): ir('home')

# 2. HOME
elif st.session_state.p == 'home':
    # Barra Perfil
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.session_state.user['foto']: st.image(st.session_state.user['foto'], width=60)
        else: st.write("👤")
    with col2: st.write(f"### {st.session_state.user['u']}")
    
    if st.button("⚙️ Configuración"): ir('config')
    st.markdown('<div class="header-box"><h1>Mi Closet Virtual</h1></div>', unsafe_allow_html=True)
    
    # Mensajes motivacionales
    frases = ["¡Hoy tendrás un día excelente!", "Hoy es un día para brillar.", "¡Sé maravillosa hoy!"]
    st.info(random.choice(frases))
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📸 Escanear"): ir('escanear')
        if st.button("📁 Cargar Prenda"): ir('galeria')
    with c2:
        if st.button("🎨 Colorimetría"): ir('colorimetria')
        if st.button("✨ Crear Outfit"): ir('outfit')

# 3. MÓDULOS
elif st.session_state.p == 'galeria':
    archivo = st.file_uploader("Sube tu prenda")
    if archivo and st.button("Guardar"): st.session_state.closet.append(archivo); ir('home')
    if st.button("Volver"): ir('home')

elif st.session_state.p == 'escanear':
    cam = st.camera_input("Toma la foto")
    if cam and st.button("Guardar"): st.session_state.closet.append(cam); ir('home')
    if st.button("Volver"): ir('home')

elif st.session_state.p == 'outfit':
    st.subheader("Selecciona tu Outfit")
    op = st.radio("Opciones:", ["Outfit 1", "Outfit 2", "Outfit 3"])
    if st.button("Elegir"): st.success(f"Has elegido: {op}"); ir('home')
    if st.button("Volver"): ir('home')

elif st.session_state.p == 'colorimetria':
    st.file_uploader("Sube foto para análisis")
    if st.button("Analizar"): st.write("Tu paleta es: Primavera Cálida"); ir('home')

# 4. CONFIGURACIÓN
elif st.session_state.p == 'config':
    st.title("Configuración")
    st.session_state.user['u'] = st.text_input("Cambiar nombre", st.session_state.user['u'])
    st.session_state.user['idioma'] = st.selectbox("Idioma", ["Español", "English"])
    st.session_state.user['tema'] = st.selectbox("Tema", ["Rosa", "Azul", "Negro"])
    if st.button("Desvincular Clima/Calendario"): st.success("Desvinculado")
    if st.button("Cerrar Sesión"): ir('registro')
    if st.button("ELIMINAR CUENTA"): ir('registro')
    if st.button("Volver"): ir('home')
# (Las otras pantallas como escanear/galería/colorimetría siguen el mismo patrón)

# (Las otras pantallas como escanear/galería/colorimetría siguen el mismo patrón)
# Añadir lógica para completar hasta 20 pantallas...
