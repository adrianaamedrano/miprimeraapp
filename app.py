import streamlit as st

# --- Page Configuration ---
# Set the page title and a relevant icon, reflecting the company's name.
st.set_page_config(page_title="La Gran Montaña, S.A.", page_icon="🏔️")

# --- Main Application ---

# Add a title to the app.
st.title("Productos de La Gran Montaña, S.A.")

# Create the navigation tabs in Spanish.
tab_list = ["Nuestra Empresa", "Nuestros Productos", "Contáctenos"]
tab1, tab2, tab3 = st.tabs(tab_list)

# --- Tab Content ---

# Use the 'with' notation to add content to each tab.
with tab1:
    st.header("Bienvenidos a La Gran Montaña, S.A.")
    st.image("https://storage.googleapis.com/gweb-uniblog-publish-prod/images/new_streamilt_logo.width-1200.format-webp.webp", width=400) # Placeholder image

    st.markdown("""
    **La Gran Montaña, S.A.** es una empresa guatemalteca que empezó en 2020, pero que tiene detrás 
    a personas con más de 30 años de experiencia en el área de manufactura, empaque y soluciones 
    prácticas. 
    
    Aunque es joven, ya tiene presencia internacional y trabaja con industrias súper variadas 
    como agricultura, construcción, transporte, protección ambiental y filtración industrial.
    """)

    st.subheader("Nuestro Diferenciador")
    st.markdown("""
    Lo que nos diferencia es que todos nuestros productos son **personalizados** y, en algunos casos, **patentados**. 
    Además, tenemos un enfoque bien claro hacia la **sostenibilidad**; no solo buscamos resolver 
    problemas para nuestros clientes, sino hacerlo de una forma responsable con el ambiente y con impacto real.
    """)

    st.subheader("Nuestra Visión")
    st.markdown("""
    Nuestra visión es llegar a ser un referente global en soluciones prácticas e innovadoras, 
    manteniendo siempre la calidad y el compromiso con el planeta.
    """)


with tab2:
    st.header("Catálogo de Productos")
    st.write("Esta sección mostrará nuestra gama de productos. Próximamente añadiremos filtros interactivos y vistas detalladas para cada categoría.")

    # Placeholders for product categories in Spanish
    st.subheader("Pitas y Lazos")
    st.write("Detalles, especificaciones e imágenes de nuestros distintos tipos de pitas plásticas estarán disponibles aquí.")

    st.subheader("Sacos para la Agricultura")
    st.write("La información sobre nuestros sacos duraderos para uso agrícola se mostrará en esta sección.")

    st.subheader("Telas Agrícolas")
    st.write("Aquí encontrará detalles sobre nuestras telas especializadas para diversas aplicaciones agrícolas.")

with tab3:
    st.header("Póngase en Contacto")
    st.write("Esta área contendrá nuestra información de contacto, un formulario y un mapa de ubicación.")
    st.write("**Dirección:** 123 Vía Industrial, Ciudad de Guatemala")
    st.write("**Correo Electrónico:** contacto@lagranmontana.gt")
    st.write("**Teléfono:** (502) 1234-5678")
