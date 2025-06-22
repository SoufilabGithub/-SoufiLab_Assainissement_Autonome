def main():

    import streamlit as st
    from PIL import Image


    st.markdown("# SoufiLab Conception d'un système d'Assainissement autonome ou individuel ou non collectif")
    st.markdown("## Section I. Collecte et transport: Définition, Règles et Caractéristiques")

    st.markdown("""
    ### 1️⃣. Définition :
    Lorsqu’une habitation n’est pas desservie par un réseau d’égout, celle-ci doit être dotée d’un système de traitement des eaux usées domestiques disposé sur la parcelle :

    C’est l’assainissement non collectif (appelé également assainissement autonome ou individuel).

    L’objectif de l’assainissement est d’assurer l’évacuation des effluents (salubrité), tout en protégeant l’environnement (nappe aquifère, cours d’eau, voisins…).

    Les eaux usées domestiques concernent :
    - **Les eaux ménagères** (20 à 30 l/hbt/j) : eaux de cuisine (lave-vaisselle, évier), eaux grises (salle de bains, lavabo, lave-linge)
    - **Les eaux vannes** (50 à 100 l/hbt/j) : eaux des WC
    """)

    st.markdown("""
    ### 2️⃣. Règles d’implantation du système autonome :
    La filière doit se trouver :
    - Hors zone : de circulation, de stockage, de cultures et plantations
    - à 35 m minimum d’une source d’eau pour l’alimentation humaine
    - à au moins 5 m d’une habitation
    - à au moins 3 m d'un arbre
    - à au moins 3 m de limite de propriété ou d’une clôture
    - ⚠️ En aucun cas, les eaux pluviales provenant des toitures et du ruissellement ne doivent rentrer dans le système
    """)

    st.markdown("### 3️⃣. Les caractéristiques de l'habitation et les données d'utilisation :")

    # Formulaire pour saisie utilisateur
    with st.form("form_donnees"):
        st.subheader("Entrer les caractéristiques et données :")
        epaisseur_sol = st.number_input("Épaisseur de la couche de sol naturel non saturée (m)", min_value=0.0)
        permeabilite = st.number_input("Perméabilité du terrain récepteur (mm/h)", min_value=0.0)

        tendance_sol = st.selectbox(
            "Tendance du sol",
            options=[
                "Sableuse", "Végétale", "Argileuse", "Limoneuse",
                "Limono-argileuse", "Dominante sableuse", "Craie"
            ]
        )

        surface_disponible = st.number_input("Superficie disponible (m²)", min_value=0.0)
        pente = st.number_input("Pente du terrain récepteur (%)", min_value=0.0)
        denivele = st.number_input("Dénivelé (m)", min_value=0.0)

        nappe_hydromorphie = st.radio("Y a-t-il une nappe ou des traces d'hydromorphie ?", ["oui", "non"])
        profondeur_nappe = st.number_input("Profondeur de la nappe ou traces (m)", min_value=0.0)
        distance_habitation_fosse = st.number_input("Distance fosse-habitation (m)", min_value=0.0)

        rehabilitation_traitement_separe = st.radio("Réhabilitation pour traitement séparé ?", ["oui", "non"])
        poste_relevage = st.radio("Pente insuffisante ou besoin de relevage ?", ["oui", "non"])

        submitted = st.form_submit_button("Afficher les résultats")

    # Traitement des données et affichage
    if submitted:
        st.subheader("=== Caractéristiques saisies ===")
        st.write(f"Épaisseur sol : {epaisseur_sol} m")
        st.write(f"Perméabilité : {permeabilite} mm/h")
        st.write(f"Tendance sol : {tendance_sol}")
        st.write(f"Surface dispo : {surface_disponible} m²")
        st.write(f"Pente : {pente} %")
        st.write(f"Dénivelé : {denivele} m")
        st.write(f"Nappe ou hydromorphie : {nappe_hydromorphie}")
        st.write(f"Profondeur nappe : {profondeur_nappe} m")
        st.write(f"Distance fosse-habitation : {distance_habitation_fosse} m")
        st.write(f"Traitement séparé : {rehabilitation_traitement_separe}")
        st.write(f"Poste de relevage : {poste_relevage}")

        ouvrages = {
            "obligatoires": ["Habitation", "Collecte et Transport", "Prétraitement", "Traitement", "Évacuation"],
            "optionnels": []
        }

        if rehabilitation_traitement_separe == "oui":
            ouvrages["optionnels"].append("Préfiltre")
        if distance_habitation_fosse > 10:
            ouvrages["optionnels"].append("Bac Dégraisseur")
        if poste_relevage == "oui" or pente < 2:
            ouvrages["optionnels"].append("Poste de Relevage")

        st.subheader("=== Résumé des ouvrages ===")
        st.markdown("**Ouvrages obligatoires :**")
        for o in ouvrages["obligatoires"]:
            st.write(f"- {o}")

        st.markdown("**Ouvrages optionnels :**")
        if ouvrages["optionnels"]:
            for o in ouvrages["optionnels"]:
                st.write(f"- {o}")
        else:
            st.write("Aucun.")

    st.markdown("---")
    st.image("images/image_generale1.jpg", caption="Schéma général 1", use_column_width=True)
    st.image("images/image_generale2.png", caption="Schéma général 2", use_column_width=True)
    st.markdown("---")