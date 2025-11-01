import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# ----------------------------
# Données fictives (liste de listes)
# ----------------------------

 
import pandas as pd

file_path = r"C:\\Users\\HP USER\\Documents\\Sorbonne Data\\Cours Python\\Projet à rendre\\Le projet\\data\\benevoles_data.csv"

data = pd.read_csv(file_path)

# ----------------------------
# Conversion en DataFrame
# ----------------------------
columns = ["Date","Nom","Prénom","Sexe","Date de naissance","Code postal","Ville","numéro de rue","Rue","Email","Téléphone","Disponibilités","Compétences","Newsletter"]
df = pd.DataFrame(data, columns=columns)

# ----------------------------
# Configuration de la page Streamlit
# ----------------------------
st.set_page_config(page_title="Analyse Bénévoles", page_icon="📊", layout="wide")

st.title("📊 Analyse des bénévoles de l'association")
st.write("Visualisation des données issues du tableau interne des bénévoles.")

# ----------------------------
# Nettoyage et préparation
# ----------------------------
df["Ville"] = df["Ville"].str.strip().str.title()
df["Sexe"] = df["Sexe"].str.strip().str.capitalize()

# ----------------------------
# 1️⃣ Répartition hommes / femmes
# ----------------------------
st.subheader("👫 Répartition par sexe")
sexe_counts = df["Sexe"].value_counts(normalize=True) * 100
sexe_table = pd.DataFrame({
    "Sexe": sexe_counts.index,
    "Pourcentage": sexe_counts.values.round(0).astype(int)

    
})
st.table(sexe_table)

fig_sexe = px.pie(
    sexe_table,
    names="Sexe",
    values="Pourcentage",
    title="Répartition Hommes / Femmes",
    color_discrete_sequence=["#66c2a5","#fc8d62"]
)
st.plotly_chart(fig_sexe, use_container_width=True)




#correction: 
# Nettoyage + conversion directe
df["Date de naissance"] = pd.to_datetime(df["Date de naissance"], errors="coerce")

# Vérifier combien de dates n'ont pas pu être converties
st.write("Dates invalides :", df["Date de naissance"].isna().sum())

# Supprimer les lignes avec des dates invalides
df = df.dropna(subset=["Date de naissance"])

# Calculer l'âge
today = pd.Timestamp(datetime.today())
df["Âge"] = ((today - df["Date de naissance"]).dt.days / 365.25).astype(int)

# ----------------------------
# Configuration de la page Streamlit
# ----------------------------

st.title("📊 L'âge des bénévoles")
st.write("Visualisation de la répartition.")

# ----------------------------
# Graphique 1 : répartition par âge (tous)
# ----------------------------
st.subheader("👥 Répartition par âge (tous)")
fig_age_all = px.histogram(
    df,
    x="Âge",
    nbins=20,
    title="Répartition par âge de l'ensemble des bénévoles",
    color_discrete_sequence=["#66c2a5"]
)
st.plotly_chart(fig_age_all, use_container_width=True)

# ----------------------------
# Graphique 2 : hommes uniquement
# ----------------------------
st.subheader("👨 Répartition par âge (hommes)")
df_hommes = df[df["Sexe"] == "Homme"]
fig_age_hommes = px.histogram(
    df_hommes,
    x="Âge",
    nbins=20,
    title="Répartition par âge des hommes bénévoles",
    color_discrete_sequence=["#1f77b4"]
)
st.plotly_chart(fig_age_hommes, use_container_width=True)

# ----------------------------
# Graphique 3 : femmes uniquement
# ----------------------------
st.subheader("👩 Répartition par âge (femmes)")
df_femmes = df[df["Sexe"] == "Femme"]
fig_age_femmes = px.histogram(
    df_femmes,
    x="Âge",
    nbins=20,
    title="Répartition par âge des femmes bénévoles",
    color_discrete_sequence=["#ff7f0e"]
)
st.plotly_chart(fig_age_femmes, use_container_width=True)

# ----------------------------
# 2️⃣ Graphique : Nombre de bénévoles par ville
# ----------------------------
st.subheader("🏙️ Nombre de bénévoles par ville")
ville_counts = df.groupby("Ville").size().reset_index(name="Nombre de bénévoles")
ville_counts = ville_counts.sort_values(by="Nombre de bénévoles", ascending=False)

fig_villes = px.bar(
    ville_counts,
    x="Ville",
    y="Nombre de bénévoles",
    text="Nombre de bénévoles",
    color="Nombre de bénévoles",
    color_continuous_scale="Blues",
    title="Nombre de bénévoles par ville"
)
fig_villes.update_layout(
    xaxis_title="Ville",
    yaxis_title="Nombre de bénévoles",
    xaxis_tickangle=-45
)
st.plotly_chart(fig_villes, use_container_width=True)

# ----------------------------
# 3️⃣ Tableau résumé
# ----------------------------
st.subheader("📋 Détail des villes")
st.dataframe(ville_counts)


