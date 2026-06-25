import streamlit as st
import random
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Mi Closet Virtual", layout="centered")

# --- ESTADO GLOBAL (Memoria) ---
if 'pantalla' not in st.session_state: st.session_state.pantalla = 'home'
if 'closet' not in st.session_state: st.session_state.closet = []

# --- ESTILOS ---
st.markdown("""
    <style>
        .header-box { background-color: #ffe4e6; padding: 20px; border-radius: 30px; border: 2px solid #ffccd5; text-align: center; }
        .stButton>button { border-radius: 20px; background-color: #ffccd5; color: #555; font-weight: bold; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# Función para volver siempre al menú
def btn_volver():
    if st.button("⬅️ Volver al Menú Principal"):
        st.session_state.pantalla = 'home'
        st.rerun()

# --- NAVEGACIÓN ---
p = st.session_state.pantalla

if p == 'home':
    st.markdown('<div class="header-box"><h1>👗 Mi Closet Virtual</h1></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📸 Escanear Prenda"): st.session_state.pantalla = 'escanear'; st.rerun()
    with col2:
        if st.button("📁 Cargar desde Galería"): st.session_state.pantalla = 'galeria'; st.rerun()
    
    if st.button("✨ Crear Outfit"): st.session_state.pantalla = 'outfit'; st.rerun()

# --- PANTALLA CARGAR GALERÍA ---
elif p == 'galeria':
    st.subheader("Cargar desde Galería")
    # Este es el componente que faltaba:
    archivo = st.file_uploader("Selecciona tu prenda", type=['png', 'jpg', 'jpeg'])
    
    if archivo is not None:
        st.image(archivo, caption="Prenda seleccionada", use_container_width=True)
        if st.button("💾 Guardar Prenda en mi Closet"):
            st.session_state.closet.append(archivo)
            st.success("¡Tus prendas han sido guardadas con éxito!")
            
    btn_volver()

# --- PANTALLA ESCANEAR ---
elif p == 'escanear':
    st.subheader("Escanear Prenda")
    camara = st.camera_input("Toma la foto")
    if camara:
        if st.button("💾 Guardar Prenda"):
            st.session_state.closet.append(camara)
            st.success("¡Prenda guardada exitosamente!")
    btn_volver()

# --- PANTALLA OUTFIT ---
elif p == 'outfit':
    st.subheader("Crear Outfit")
    if len(st.session_state.closet) < 2:
        st.warning("Necesitas al menos 2 prendas guardadas para crear un outfit.")
    else:
        st.write("¡Aquí están tus prendas mezcladas!")
        # Lógica de outfits...
    btn_volver()
# (Las otras pantallas como escanear/galería/colorimetría siguen el mismo patrón)

# (Las otras pantallas como escanear/galería/colorimetría siguen el mismo patrón)
# Añadir lógica para completar hasta 20 pantallas...
