def main():

    import streamlit as st
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from PIL import Image

    st.markdown("## IV. Conception : Préfiltre, Bac dégraisseur, Poste de relevage")

    # Affichage des schémas dynamiques
    def afficher_schema_bac_degraisseur(volume):
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.set_title(f"Bac dégraisseur ({volume} L)", fontsize=10)
        ax.add_patch(patches.Rectangle((0.3, 0.4), 0.4, 0.3, edgecolor='black', facecolor='lightgrey'))
        ax.text(0.2, 0.55, "Entrée", ha='center', fontsize=9, color='blue')
        ax.text(0.8, 0.55, "Sortie", ha='center', fontsize=9, color='green')
        ax.arrow(0.2, 0.55, 0.1, 0, head_width=0.02, head_length=0.02, fc='blue', ec='blue')
        ax.arrow(0.8, 0.55, -0.1, 0, head_width=0.02, head_length=0.02, fc='green', ec='green')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        st.pyplot(fig)

    def afficher_schema_prefiltre(volume):
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.set_title(f"Préfiltre ({volume} L)", fontsize=10)
        ax.add_patch(patches.Rectangle((0.3, 0.4), 0.4, 0.3, edgecolor='black', facecolor='lightgrey'))
        ax.text(0.2, 0.55, "Entrée", ha='center', fontsize=9, color='blue')
        ax.text(0.8, 0.55, "Sortie", ha='center', fontsize=9, color='green')
        ax.text(0.5, 0.45, "Filtre (pointillé)", ha='center', fontsize=8, color='grey')
        ax.arrow(0.2, 0.55, 0.1, 0, head_width=0.02, head_length=0.02, fc='blue', ec='blue')
        ax.arrow(0.8, 0.55, -0.1, 0, head_width=0.02, head_length=0.02, fc='green', ec='green')
        ax.plot([0.35, 0.65], [0.55, 0.55], linestyle="--", color="grey")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        st.pyplot(fig)

    def afficher_schema_poste_relevage():
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.set_title("Poste de relevage", fontsize=10)
        ax.add_patch(patches.Rectangle((0.3, 0.4), 0.4, 0.3, edgecolor='black', facecolor='lightblue'))
        ax.text(0.2, 0.55, "Entrée", ha='center', fontsize=9, color='blue')
        ax.text(0.8, 0.55, "Sortie", ha='center', fontsize=9, color='green')
        ax.text(0.5, 0.45, "Pompe", ha='center', fontsize=8, color='grey')
        ax.arrow(0.2, 0.55, 0.1, 0, head_width=0.02, head_length=0.02, fc='blue', ec='blue')
        ax.arrow(0.8, 0.55, -0.1, 0, head_width=0.02, head_length=0.02, fc='green', ec='green')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        st.pyplot(fig)

    # Interface utilisateur
    choix = st.multiselect(
        "Choisissez les ouvrages à dimensionner :",
        ["Bac dégraisseur", "Préfiltre", "Poste de relevage"]
    )

    if "Bac dégraisseur" in choix:
        st.markdown("### Bac dégraisseur")
        effluent_type = st.radio("Type d'effluents :", ["Cuisine seule", "Eaux ménagères"], key="effluent")
        volume = 200 if effluent_type == "Cuisine seule" else 500
        st.write(f"✅ Volume recommandé : **{volume} litres**")
        afficher_schema_bac_degraisseur(volume)

    if "Préfiltre" in choix:
        st.markdown("### Préfiltre")
        installation_type = st.radio("Type d'installation :", ["Extérieur fosse", "Incorporé fosse"], key="prefiltre")
        volume = 200 if installation_type == "Extérieur fosse" else 50
        st.write(f"✅ Volume recommandé : **{volume} litres**")
        afficher_schema_prefiltre(volume)
        st.image("images/image1_prefiltre.jpeg", caption="Exemple réel de préfiltre", use_column_width=True)

    if "Poste de relevage" in choix:
        st.markdown("### Poste de relevage")
        nb_habitants = st.number_input("Nombre d'habitants", min_value=1, value=6, step=1)
        volume_poste = 100 + (nb_habitants - 6) * 25 if nb_habitants > 6 else 100
        volume_bachee = 80 + (nb_habitants - 6) * 20 if nb_habitants > 6 else 80
        st.write(f"✅ Volume du poste : **{volume_poste} litres**")
        st.write(f"✅ Volume de bâchée : **{volume_bachee} litres**")
        afficher_schema_poste_relevage()