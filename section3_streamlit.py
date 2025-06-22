def main():

    import streamlit as st
    from PIL import Image

    st.markdown("## III. Traitement : Conception des filières")

    def afficher_images(image_paths):
        for path in image_paths:
            st.image(f"images/{path}", use_column_width=True)

    def choisir_filiere_et_dimensionner(K, surface_disponible, pente, nappe_hydromorphie, profondeur_nappe, denivele):
        if 15 <= K <= 500 and surface_disponible > 200 and pente < 2 and nappe_hydromorphie == 'non' and profondeur_nappe > 1.5:
            filiere = "Tranchées d'épandage à faible profondeur"
            images = [
                "trancee_epandagefaible_prof_coupe_longitidinale.jpeg",
                "trancee_epandagefaible_prof_coupe_transversale.jpeg",
                "tranchee_epandagefaible_prof_vuedessus.jpeg"
            ]
            dimensions = [
                "- Longueur de chaque branche : max 30 m",
                "- Largeur minimale : 0,5 m"
            ]
        elif 15 <= K <= 500 and surface_disponible > 200 and 2 <= pente <= 10 and nappe_hydromorphie == 'non' and profondeur_nappe > 1.5:
            filiere = "Tranchées d'épandage pour terrain en pente"
            images = ["trancee_epandage_terrain_pente.jpeg"]
            dimensions = ["- Tuyaux disposés perpendiculairement à la pente."]
        elif 50 <= K <= 500 and surface_disponible > 200 and pente < 2 and nappe_hydromorphie == 'non' and profondeur_nappe > 1.5:
            filiere = "Lit d'épandage à faible profondeur"
            images = ["lit_epandagefaible_prof1.jpeg", "lit_epandagefaible_prof2.jpeg"]
            dimensions = ["- Surface minimale : 60 m² pour 5 pièces principales."]
        elif (K < 15 or K > 500) and surface_disponible >= 25:
            filiere = "Lit filtrant non drainé à flux vertical"
            images = [
                "lit_filtrant_sable_non_draine_a_flux_vertical_filtre_sable_vertical_non_draine1_.jpeg",
                "lit_filtrant_sable_non_draine_a_flux_vertical_filtre_sable_vertical_non_draine2.jpeg",
                "lit_filtrant_sable_non_draine_a_flux_vertical_filtre_sable_vertical_non_draine3.jpeg"
            ]
            dimensions = ["- Surface minimale : 25 m² pour 5 pièces principales."]
        elif 15 <= K <= 500 and surface_disponible >= 80 and profondeur_nappe < 0.8:
            filiere = "Tertre d'infiltration"
            images = ["tertre_dinfiltration1.jpeg", "tertre_dinfiltration2.jpeg"]
            dimensions = ["- Surface minimale : 80 m² pour 5 pièces principales."]
        elif K <= 6 and denivele > 1.5 and surface_disponible >= 25 and pente < 10 and nappe_hydromorphie == 'oui':
            filiere = "Filtre à sable vertical drainé"
            images = [
                "lit_filtrant_draine_a_flux_vertical_filtre_sable_vertical_draine1_.jpeg",
                "lit_filtrant_draine_a_flux_vertical_filtre_sable_vertical_draine2.jpeg",
                "lit_filtrant_draine_a_flux_vertical_filtre_sable_vertical_draine3.jpeg"
            ]
            dimensions = [
                "- Surface minimale : 25 m² pour 5 pièces principales.",
                "- Dénivelé requis : > 1.5 m"
            ]
        elif K <= 6 and surface_disponible >= 33 and profondeur_nappe >= 0.8 and pente < 5 and nappe_hydromorphie == 'oui':
            filiere = "Filtre à sable horizontal drainé"
            images = [
                "lit_filtrant_draine_a_flux_horizontal_filtre_sable_horizontal_draine1_.jpeg",
                "lit_filtrant_draine_a_flux_horizontal_filtre_sable_horizontal_draine2.jpeg",
                "lit_filtrant_draine_a_flux_horizontal_filtre_sable_horizontal_draine3.jpeg"
            ]
            dimensions = [
                "- Surface minimale : 33 m² pour 4 pièces principales.",
                "- Profondeur de la nappe : >= 0.8 m"
            ]
        else:
            filiere = None
            images = []
            dimensions = []
        return filiere, images, dimensions

    # Interface utilisateur
    with st.form("form_filiere"):
        K = st.number_input("Perméabilité du sol (K en mm/h)", min_value=0.0)
        surface_disponible = st.number_input("Surface disponible (m²)", min_value=0.0)
        pente = st.number_input("Pente du terrain (%)", min_value=0.0)
        nappe_hydromorphie = st.radio("Présence de nappe ou traces d'hydromorphie ?", ["oui", "non"])
        profondeur_nappe = st.number_input("Profondeur de la nappe (m)", min_value=0.0)
        denivele = st.number_input("Dénivelé disponible (m)", min_value=0.0)
        submitted = st.form_submit_button("Déterminer la filière")

    if submitted:
        filiere, images, dimensions = choisir_filiere_et_dimensionner(K, surface_disponible, pente, nappe_hydromorphie, profondeur_nappe, denivele)
        if filiere:
            st.success(f"### Filière adaptée : {filiere}")
            st.markdown("#### Instructions de dimensionnement :")
            for d in dimensions:
                st.write(f"- {d}")
            st.markdown("#### Illustrations :")
            afficher_images(images)
        else:
            st.error("Aucune filière adaptée aux paramètres fournis. Veuillez revoir les conditions.")