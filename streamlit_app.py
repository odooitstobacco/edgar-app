import streamlit as st

# -----------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------

# Configuración de la página
st.set_page_config(page_title="Portafolio", page_icon="🧑‍💻", layout="wide")

# Sidebar de navegación
st.sidebar.markdown("## 🧭 Navegación")

opcion = st.sidebar.selectbox("Elegir", ["🏠 Inicio", "📁 Habilidades", "📬 Contacto", "💻 Código"])

# FOTO DE PERFIL
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("static/avatarEDCD.png", width=200)

# Opciones de Navegación interna
if "Inicio" in opcion:
    st.markdown('''
    # 👋 ¡Hola! Soy **Edgar David Caamal ;D**
    ### *Desarrollador | Entusiasta de la IA | Freelancer | Docente del CONALEP*
    ''')


    # -----------------------
    # SOBRE MÍ
    # -----------------------
    st.markdown('''
    ## 🧠 Sobre mí

    Soy un apasionado por la tecnología con experiencia en desarrollo web, inteligencia artificial y ciencia de datos. Me encanta aprender nuevas herramientas y aplicarlas en proyectos reales que generen impacto.

    - 💼 Más de 25 años de experiencia en desarrollo.
    - 📍 Ubicado en Ciudad de Campeche , México.
    - 🛠️ Trabajo con Python, JavaScript, Java, y más.

    ''')

elif "Habilidades" in opcion:
    st.markdown('''
    ## 🛠️ Habilidades Técnicas

    - **Lenguajes**: Python, JavaScript, SQL
    - **Frameworks**: Django, FastAPI, React
    - **Herramientas**: Git, Docker, Streamlit, AWS
    - **IA/ML**: scikit-learn, TensorFlow, OpenAI API
    ''')

elif "Contacto" in opcion:
    st.markdown("## 📬 Contacto")
    st.markdown('''
    - 📧 [caamal.edgar@gmail.com](mailto:caamal.edgar@gmail.com)
    - 🌐 [GitHub](https://github.com/caamaledgar)
    - 💼 [LinkedIn](https://www.linkedin.com/in/edcaamal)
    ''')

elif "Código" in opcion:
    st.markdown("## 💻 Código del Portafolio")
    st.markdown("Este portafolio fue desarrollado con [Streamlit](https://streamlit.io). A continuación puedes ver el código fuente de esta aplicación:")

    with st.expander("📄 Sección inicial"):
        st.code("""
            import streamlit as st

            # -----------------------
            # CONFIGURACIÓN DE LA PÁGINA
            # -----------------------

            # Configuración de la página
            st.set_page_config(page_title="Portafolio", page_icon="🧑‍💻", layout="wide")

            # Sidebar de navegación
            st.sidebar.markdown("## 🧭 Navegación")

            opcion = st.sidebar.selectbox("Elegir", ["🏠 Inicio", "📁 Habilidades", "📬 Contacto", "💻 Código"])

            # FOTO DE PERFIL
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image("static/avatarEDCD.png", width=200)

        """, language="python")

    with st.expander("📄 Opción de navegación - Inicio"):
        st.code("""
            # Opciones de Navegación interna
            if "Inicio" in opcion:
                st.markdown('''
                # 👋 ¡Hola! Soy **Edgar David Caamal ;D**
                ### *Desarrollador | Entusiasta de la IA | Freelancer | Docente del CONALEP*
                ''')


                # -----------------------
                # SOBRE MÍ
                # -----------------------
                st.markdown('''
                ## 🧠 Sobre mí

                Soy un apasionado por la tecnología con experiencia en desarrollo web, inteligencia artificial y ciencia de datos. Me encanta aprender nuevas herramientas y aplicarlas en proyectos reales que generen impacto.

                - 💼 Más de 25 años de experiencia en desarrollo.
                - 📍 Ubicado en Ciudad de Campeche , México.
                - 🛠️ Trabajo con Python, JavaScript, Java, y más.

                ''')
        """, language="python")
        
    with st.expander("📄 Opción de navegación - Habilidades"):
        st.code("""
            elif "Habilidades" in opcion:
                                st.markdown('''
                ## 🛠️ Habilidades Técnicas

                - **Lenguajes**: Python, JavaScript, SQL
                - **Frameworks**: Django, FastAPI, React
                - **Herramientas**: Git, Docker, Streamlit, AWS
                - **IA/ML**: scikit-learn, TensorFlow, OpenAI API
                ''')
        """, language="python")
        
    with st.expander("📄 Opción de navegación - Contacto"):
        st.code("""
            elif "Contacto" in opcion:
                st.markdown("## 📬 Contacto")
                st.markdown('''
                - 📧 [caamal.edgar@gmail.com](mailto:caamal.edgar@gmail.com)
                - 🌐 [GitHub](https://github.com/caamaledgar)
                - 💼 [LinkedIn](www.linkedin.com/in/edcaamal)
                ''')
        """, language="python")
        
    with st.expander("📄 Opción de navegación - Pie de Página"):
        st.code("""
            # -----------------------
            # PIE DE PÁGINA
            # -----------------------
            st.markdown("---")
            st.markdown("También puedes ver el código completo en [mi repositorio en GitHub](https://github.com/odooitstobacco/edgar-app).")
            st.markdown("© 2025 Edgar David Caamal ;D — Construido con ❤️ en Streamlit")
        """, language="python")        

# -----------------------
# PIE DE PÁGINA
# -----------------------
st.markdown("---")
st.markdown("También puedes ver el código completo en [mi repositorio en GitHub](https://github.com/odooitstobacco/edgar-app).")
st.markdown("© 2025 Edgar David Caamal ;D — Construido con ❤️ en Streamlit")