def main():

    import streamlit as st
    from PIL import Image

    st.markdown("## VI. Évacuation : puits d'infiltration, rejet naturel, réutilisation")

    st.markdown("""
    Dans cette section, l'utilisateur doit choisir le **mode d’évacuation** de l’eau traitée parmi les options suivantes :

    - 🌿 **Rejet naturel** (rivières, fossés, etc.)
    - ♻️ **Réutilisation** (arrosage, irrigation, etc.)
    - 🌍 **Infiltration par puits**

    👉 **Attention** : Chaque option est soumise à des **conditions spécifiques** environnementales, sanitaires ou réglementaires.
    """)

    choix = st.radio(
        "Quel mode d'évacuation souhaitez-vous envisager ?",
        ["Rejet naturel", "Réutilisation", "Infiltration par puits"]
    )

    if choix == "Infiltration par puits":
        st.markdown("### 🌍 Infiltration par puits :")
        st.info("Cette méthode permet de laisser infiltrer l’eau traitée dans le sol à travers un puits conçu à cet effet.")
        st.image("images/puits_infiltration.jpeg", caption="Puits d’infiltration", use_column_width=True)
    elif choix == "Rejet naturel":
        st.markdown("### 🌿 Rejet naturel :")
        st.info("Autorisé uniquement si les caractéristiques de l’eau traitée respectent les normes de rejet dans le milieu naturel.")
    elif choix == "Réutilisation":
        st.markdown("### ♻️ Réutilisation :")
        st.info("Peut être envisagée pour l’arrosage ou l’irrigation, sous réserve de qualité bactériologique et réglementaire.")

    st.markdown("---")
    st.warning("✅ Cette section pourra être enrichie avec des vérifications de conformité ou des simulateurs selon les scénarios choisis.")