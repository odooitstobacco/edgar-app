import streamlit as st
from cursos_data import timeline_data

# -----------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------

# Configuración de la página
st.set_page_config(page_title="Portafolio", page_icon="🧑‍💻", layout="wide")

# Sidebar de navegación
st.sidebar.markdown("## 🧭 Navegación")

opcion = st.sidebar.selectbox("Elegir", [
    "🏠 Inicio", 
    "📁 Habilidades", 
    "🌐 Cursos",
    "📬 Contacto", 
    "💻 Código"])

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

    # -----------------------
    # Formación Académica
    # -----------------------
    st.markdown('''
    ## 💼 Formación Académica ''')

    # Maestría
    st.success("""\
        **Maestría en Dirección de Tecnologías de la Información y Comunicaciones**  
        Universidad Anáhuac Mayab, Campus Campeche (2017–2018)  
        Cédula Profesional: 11492845
    """)

    # Licenciatura
    st.info("""\
        **Licenciatura en Informática**  
        Instituto Tecnológico de Campeche (1990–1994)  
        Cédula Profesional: 7297017
    """)

elif "Habilidades" in opcion:
    st.markdown('''
    ## 🛠️ Habilidades Técnicas

    - **Lenguajes**: Python, JavaScript, SQL
    - **Frameworks**: Django, FastAPI, React
    - **Herramientas**: Git, Docker, Streamlit, AWS
    - **IA/ML**: scikit-learn, TensorFlow, OpenAI API
    ''')
elif "Cursos" in opcion:
    # Mostrar título principal
    st.title(timeline_data["title"]["text"]["headline"])
    st.info(timeline_data["title"]["text"]["text"])
    anno_actual = None
    # Recorrer eventos y mostrar cada uno
    for event in timeline_data["events"]:
         fecha = event["start_date"]
         titulo = event["text"]["headline"]
         institucion = event["text"]["text"]

         anno = fecha["year"]
         if anno != anno_actual:
            st.markdown(f"##### 📅 {anno}")
            anno_actual = anno
    
         fecha_str = f"{fecha['day']:02d}/{fecha['month']:02d}/{fecha['year']}"
         mensaje = f"{fecha_str} — {titulo}\n{institucion}"
         st.code(mensaje)


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
    st.write("El siguiente código es demostrativo del desarrollo de esta aplicación")
    st.write("Visite la ultima actualización en el repositorio de github")
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

            opcion = st.sidebar.selectbox("Elegir", [
                "🏠 Inicio", 
                "📁 Habilidades", 
                "🌐 Cursos",
                "📬 Contacto", 
                "💻 Código"])
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

                # -----------------------
                # Formación Académica
                # -----------------------
                st.markdown('''
                ## 💼 Formación Académica ''')

                # Maestría
                st.success('''\
                    **Maestría en Dirección de Tecnologías de la Información y Comunicaciones**  
                    Universidad Anáhuac Mayab, Campus Campeche (2017–2018)  
                    Cédula Profesional: 11492845
                ''')

                # Licenciatura
                st.info('''\
                    **Licenciatura en Informática**  
                    Instituto Tecnológico de Campeche (1990–1994)  
                    Cédula Profesional: 7297017
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

    with st.expander("📄 Opción de navegación - Cursos "):
        st.write("Crear el archivo de datos cursos_data.py")
        st.code("""
            # Datos para la línea del tiempo en formato TimelineJS (JSON)
            # Los datos deben estar en Orden Cronologico Descendente de preferencia

            timeline_data = {
                "title": {
                    "text": {
                        "headline": "Cursos y Certificaciones",
                        "text": "Línea del tiempo de formación continua de Edgar David Caamal Dzulu"
                    }
                },
                "events": [
                    {
                        "start_date": {"year": 2023, "month": 5, "day": 2},
                        "text": {
                            "headline": "Introducción al Desarrollo Web",
                            "text": "Google Activate"
                        }
                    },
                    {
                        "start_date": {"year": 2023, "month": 5, "day": 1},
                        "text": {
                            "headline": "Desarrollo de Apps Móviles",
                            "text": "Google Activate"
                        }
                    },
                # ... Puede añadir más eventos
                ]
            }        
        """, language="python")
        st.write("Actualizar el archivo principal stramlit_app.py")
        st.code("""
            import streamlit as st
            from cursos_data import timeline_data
        """, language="python")

        st.write("Codigo de la opción")
        st.code("""
            elif "Cursos" in opcion:
                # Mostrar título principal
                st.title(timeline_data["title"]["text"]["headline"])
                st.info(timeline_data["title"]["text"]["text"])
                anno_actual = None
                # Recorrer eventos y mostrar cada uno
                for event in timeline_data["events"]:
                    fecha = event["start_date"]
                    titulo = event["text"]["headline"]
                    institucion = event["text"]["text"]

                    anno = fecha["year"]
                    if anno != anno_actual:
                        st.markdown(f"##### 📅 {anno}")
                        anno_actual = anno
                
                    fecha_str = f"{fecha['day']:02d}/{fecha['month']:02d}/{fecha['year']}"
                    mensaje = f"{fecha_str} — {titulo}\n{institucion}"
                    st.code(mensaje)
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