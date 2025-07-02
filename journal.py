import streamlit as st
import os
from datetime import datetime, date
import random

# ---- TITRE ----
st.title("❤️ Journal Intime pour la femme que j'aime ❤️")
st.write("Un espace pour te confier et recevoir un boost quotidien !")

# ---- LISTE DE PHRASES MOTIVANTES ----
boosts = [
    "💪 Crois en toi, chaque jour est une victoire.",
    "🚀 Même les plus grands ont commencé petits.",
    "🌱 Cultive ta persévérance, elle est ton super-pouvoir.",
    "🔥 Ce que tu fais aujourd'hui construit ton demain.",
    "🌟 Rappelle-toi pourquoi tu as commencé.",
    "🏆 Un pas après l'autre mène toujours plus loin.",
    "⚡ Tu es plus fort que tes peurs.",
    "🎯 Focalise-toi sur ce qui compte vraiment.",
    "⛰️ Les sommets paraissent hauts jusqu'à ce qu'on les atteigne.",
    "🌈 Chaque échec est une leçon, chaque succès une fête.",
    "🦃 Tu es peut-etre une Dinde, mais tu es MA grosse dinde."
]

# ---- SECTION MESSAGE MOTIVATION ----
if st.button("✨ Génère mon boost du jour !"):
    boost = random.choice(boosts)
    st.success(boost)

# ---- SECTION JOURNAL ----
st.header("📝 Écris ton journal intime")

# Sélecteur de date pour choisir le jour de l'entrée
selected_date = st.date_input(
    "Sélectionne une date pour ton entrée :",
    date.today()
)

journal_text = st.text_area("Exprime-toi librement :", height=300)

if st.button("💾 Sauvegarder mon entrée du jour"):
    filename = f"journal_{selected_date}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(journal_text)
    st.success(f"Entrée sauvegardée pour le {selected_date} sous {filename}")

# ---- SECTION LECTURE ----
st.header("📚 Relire mes entrées")

# Sélecteur de date pour relire une entrée spécifique
read_date = st.date_input(
    "Sélectionne une date pour relire ton entrée :",
    date.today(),
    key="read_date"
)

if st.button("📂 Charger mon entrée pour cette date"):
    filename = f"journal_{read_date}.txt"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            st.subheader(f"Entrée du {read_date}")
            st.write(content)
    else:
        st.info(f"Aucune entrée trouvée pour le {read_date}.")

# ---- SECTION TÉLÉCHARGEMENT ----
st.header("💾 Télécharger l'entrée du jour")

if st.button("📥 Télécharger mon entrée"):
    if journal_text.strip() != "":
        st.download_button(
            label="📥 Télécharger maintenant",
            data=journal_text,
            file_name=f"journal_{selected_date}.txt",
            mime="text/plain"
        )
    else:
        st.warning("Rien à télécharger : écris quelque chose d'abord !")
