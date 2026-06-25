import streamlit as st
import random
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Mi Closet Virtual", layout="centered")

# --- ESTILOS "KAWAII" PERSONALIZADOS ---
st.markdown("""
    <style>
        .main { background-color: #fdf6f0; }
        .header-box { background-color: #ffe4e6; padding: 20px; border-radius: 30px; border: 2px solid #ffccd5; text-align: center; margin-bottom: 20px; }
        .profile-bar { display: flex; align-items: center; justify-content: space-between; padding: 10px; background: #fff; border-radius: 20px; border: 1px solid #ffccd5; margin-bottom: 10px; }
        .stButton>button { border-radius: 20px; background-color: #ffccd5; color: #555; border: none; font-weight: bold; }
        .frase-box { text-align: center; font-style: italic; color: #888; margin-top: 20px; min-height: 50px; }
    </style>
""", unsafe_allow_html=True)

# --- ESTADO GLOBAL ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'registro'
if 'user_data' not in st.session_state: 
    st.session_state.user_data = {'nombre': '', 'apellido': '', 'usuario': '', 'foto': None}

# --- LÓGICA DE PANTALLAS ---
p = st.session_state.pantalla

# 1. PANTALLAS DE REGISTRO
if p == 'registro':
    st.markdown('<div class="header-box"><h1>👗 Registro</h1></div>', unsafe_allow_html=True)
    st.session_state.user_data['nombre'] = st.text_input("Nombre")
    st.session_state.user_data['apellido'] = st.text_input("Apellido")
    st.session_state.user_data['usuario'] = st.text_input("Nombre de Usuario")
    if st.button("Siguiente"): st.session_state.pantalla = 'exito_reg'; st.rerun()

elif p == 'exito_reg':
    st.success("¡Felicidades, te has registrado con éxito!")
    if st.button("Continuar a Datos Personales"): st.session_state.pantalla = 'datos'; st.rerun()

elif p == 'datos':
    st.markdown("### Introduce tus datos")
    st.selectbox("Género", ["Femenino", "Masculino", "Prefiero no decirlo"])
    st.number_input("Talla (cm)", 50, 250)
    st.number_input("Peso (kg)", 10, 300)
    st.session_state.user_data['foto'] = st.file_uploader("Subir foto de perfil", type=['png', 'jpg'])
    if st.button("Finalizar"): st.session_state.pantalla = 'config_inicial'; st.rerun()

elif p == 'config_inicial':
    st.markdown("### Conecta tus herramientas")
    st.checkbox("Unir a Calendario")
    st.checkbox("Unir a Clima")
    if st.button("Entrar a mi Closet"): st.session_state.pantalla = 'home'; st.rerun()

# 2. HOME Y PANTALLA PRINCIPAL
elif p == 'home':
    # Perfil Superior
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.session_state.user_data['foto']: st.image(st.session_state.user_data['foto'], width=60)
        else: st.write("👤")
    with col2:
        st.write(f"**{st.session_state.user_data['usuario']}**")
    
    # Botón de Configuración pequeña a la derecha
    if st.button("⚙️ Configuración"): st.session_state.pantalla = 'config_menu'; st.rerun()
    
    st.markdown('<div class="header-box"><h1>Mi Closet Virtual</h1></div>', unsafe_allow_html=True)
    
    # Acciones principales
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📸 Escanear Prenda"): st.session_state.pantalla = 'escanear'
        if st.button("📁 Cargar Prenda"): st.session_state.pantalla = 'galeria'
    with c2:
        if st.button("🎨 Colorimetría"): st.session_state.pantalla = 'colorimetria'
        if st.button("✨ Crear Outfit"): st.session_state.pantalla = 'outfit'
        
    # Frases motivacionales
    frases = ["¡Hoy tendrás un día excelente!", "Hoy es un día para brillar.", "¡Eres capaz de todo!"]
    st.markdown(f'<div class="frase-box">{random.choice(frases)}</div>', unsafe_allow_html=True)
    time.sleep(1) # Pequeña espera para el efecto

# 3. PANTALLAS DE CONFIGURACIÓN
elif p == 'config_menu':
    st.title("Configuración")
    st.selectbox("Idioma", ["Español", "English"])
    st.selectbox("Tema", ["Rosa", "Azul", "Negro"])
    if st.button("Desvincular Calendario"): st.success("Desvinculado")
    if st.button("Desvincular Clima"): st.success("Desvinculado")
    if st.button("Cerrar Sesión"): st.warning("Sesión finalizada"); st.session_state.pantalla = 'registro'; st.rerun()
    if st.button("ELIMINAR CUENTA"): st.error("Cuenta eliminada"); st.session_state.pantalla = 'registro'; st.rerun()
    if st.button("Volver"): st.session_state.pantalla = 'home'; st.rerun()

# (Las otras pantallas como escanear/galería/colorimetría siguen el mismo patrón)

# (Las otras pantallas como escanear/galería/colorimetría siguen el mismo patrón)
# Añadir lógica para completar hasta 20 pantallas...
