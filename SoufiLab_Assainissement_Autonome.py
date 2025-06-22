
import streamlit as st

# Import des modules pour chaque section
import section1_streamlit as s1
import section2_streamlit as s2
import section3_streamlit as s3
import section4_streamlit as s4
import section5_streamlit as s5
import section6_streamlit as s6

st.set_page_config(page_title="SoufiLab_Assainissement_Autonome", layout="wide")

st.title("🏠 SoufiLab - Application d'assainissement autonome")

st.markdown("""
Bienvenue dans **SoufiLab_Assainissement_Autonome**, une application interactive conçue pour :

- Concevoir des systèmes d’assainissement non collectif  
- Réaliser des calculs de dimensionnement  
- Visualiser des ouvrages et vérifier les conditions de mise en œuvre

Sélectionnez une section dans le menu à gauche pour commencer.
""")

# Menu de navigation
section = st.sidebar.selectbox(
    "📂 Aller à la section :",
    [
        "Section I - Collecte et Transport",
        "Section II - Prétraitement",
        "Section III - Traitement",
        "Section IV - Ouvrages complémentaires",
        "Section V - Qualité de l'eau",
        "Section VI - Évacuation"
    ]
)

# Appel direct aux fonctions des sections
if section == "Section I - Collecte et Transport":
    s1.main()
elif section == "Section II - Prétraitement":
    s2.main()
elif section == "Section III - Traitement":
    s3.main()
elif section == "Section IV - Ouvrages complémentaires":
    s4.main()
elif section == "Section V - Qualité de l'eau":
    s5.main()
elif section == "Section VI - Évacuation":
    s6.main()
