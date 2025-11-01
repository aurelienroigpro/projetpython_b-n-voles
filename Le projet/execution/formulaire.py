

import streamlit as st
import pandas as pd
from datetime import datetime, date
import os


# ----------------------------
# Configuration de la page
# ----------------------------
st.set_page_config(page_title="Inscription Bénévoles", page_icon="🤝", layout="centered")

# ----------------------------
# Couleur de fond vert clair
# ----------------------------

st.markdown(
    """
    <style>
    /*Fond de la page */.stapp{
        background-color: #8ddc8d;  /* vert clair */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🤝 Bienvenue à l'association!!")
st.write("Merci de prendre quelques minutes pour remplir ce formulaire.")

# ----------------------------
# Création du formulaire
# ----------------------------
with st.form("formulaire_benevoles"):
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    sexe = st.radio("Sexe", ["Homme", "Femme"])
    date_naissance = st.date_input("Date de naissance", min_value=date(1800,1,1), max_value=date.today())
    code_postal = st.text_input("code postal")
    ville = st.text_input("ville")
    num_de_rue = st.text_input("numéro de rue")
    rue = st.text_input("rue")
    email = st.text_input("Email")
    telephone = st.text_input("Téléphone")
    disponibilites = st.text_area("Disponibilités (ex : soirs, week-ends, vacances…)")
    competences = st.text_area("Compétences particulières (ex : communication, logistique, animation…)")
    newsletter = st.selectbox("Souhaitez-vous recevoir nos actualités ?", ["Oui", "Non"])
    submitted = st.form_submit_button("Envoyer")

# ----------------------------
# Sauvegarde des données
# ----------------------------
if submitted:
    if nom and prenom and email:
        data = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Nom": nom,
            "Prénom": prenom,
            "sexe": sexe,
            "Date de naissance":date_naissance,
            "code postal":code_postal,
            "ville":ville,
            "numéro de rue":num_de_rue,
            "rue":rue,
            "Email": email,
            "Téléphone": telephone,
            "Disponibilités": disponibilites,
            "Compétences": competences,
            "Newsletter": newsletter
        }

        # Fichier CSV de stockage
        file_path = r"C:\\Users\\HP USER\\Documents\\Sorbonne Data\\Cours Python\\Projet à rendre\\Le projet\\data\\benevoles_data.csv"
        df = pd.DataFrame([data])

        # Ajout au fichier existant si présent
        if os.path.exists(file_path):
            df.to_csv(file_path, mode='a', header=False, index=False, encoding='utf-8')
        else:
            df.to_csv(file_path, index=False, encoding='utf-8')

        st.success(f"✅ Merci {prenom} {nom}, votre inscription a bien été enregistrée !")
    else:
        st.error("⚠️ Veuillez remplir au minimum les champs Nom, Prénom et Email.")
