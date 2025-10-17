import streamlit as st
import pandas as pd

# Datos generales de las Elecciones Generales Ecuador 2025
datos = {
    "Aspecto": [
        "Fecha de la primera vuelta",
        "Fecha de la segunda vuelta (si se requiere)",
        "Qué se elige",
        "Padrón electoral",
        "Voto en el exterior",
        "Número de candidaturas principales",
        "Número de binomios presidenciales",
        "Multa por no votar",
        "Horario de votación",
        "Inicio de campaña electoral",
        "Debate presidencial obligatorio",
        "Simulacro electoral",
        "Requisitos y normas relevantes"
    ],
    "Detalles": [
        "9 de febrero de 2025",
        "13 de abril de 2025",
        "Presidente y Vicepresidente, 151 asambleístas nacionales y provinciales, y parlamentarios andinos",
        "Aproximadamente 13,736,314 electores",
        "Sí, está contemplado para ecuatorianos residentes en el exterior",
        "Alrededor de 2,200 candidaturas principales (más suplentes)",
        "16 binomios presidenciales inscritos",
        "10% del Salario Básico Unificado (~US$47)",
        "De 07:00 a 17:00 (hora nacional)",
        "5 de enero de 2025",
        "19 de enero de 2025",
        "19 de enero de 2025",
        "Paridad de género, alternabilidad y secuencialidad en las listas"
    ]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Mostrar título y tabla en Streamlit
st.title("🗳️ Elecciones Generales Ecuador 2025")
st.markdown("Datos oficiales y verificados sobre las elecciones presidenciales y legislativas de Ecuador 2025.")

st.dataframe(df)

# Fuente de información
st.markdown("""
**Fuentes oficiales y verificadas:**  
- [Wikipedia - Elecciones generales de Ecuador 2025](https://en.wikipedia.org/wiki/2025_Ecuadorian_general_election)  
- [Primicias.ec - Calendario electoral y normativa CNE](https://www.primicias.ec/elecciones/ecuador2025/)  
- [El Diario - Elecciones Generales 2025](https://www.eldiario.ec/)  
- [La Prensa - Elecciones 2025 Ecuador](https://www.laprensa.com.ec/)
""")
