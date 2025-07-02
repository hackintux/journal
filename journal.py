import streamlit as st
import os
from datetime import datetime
import random

# ---- TITRE ----
st.title("🌟 Mon Journal Intime avec Coach Statique 🌟")
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
    "🌈 Chaque échec est une leçon, chaque succès une fête."
]

# ---- SECTION MESSAGE MOTIVATION ----
if st.button("✨ Génère mon boost du jour !"):
    with st.spinner("L'IA réfléchit à ton message motivant..."):
        boost = random.choice(boosts)
        st.success(boost)

# ---- SECTION JOURNAL ----
st.header("📝 Écris ton journal intime")

journal_text = st.text_area("Exprime-toi librement :", height=300)

if st.button("💾 Sauvegarder mon entrée du jour"):
    today = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"journal_{today}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(journal_text)
    st.success(f"Entrée sauvegardée sous {filename}")

# ---- SECTION LECTURE ----
st.header("📚 Relire mes entrées")

if st.button("📂 Charger mes anciennes entrées"):
    files = [f for f in os.listdir() if f.startswith("journal_") and f.endswith(".txt")]
    if files:
        for file in sorted(files, reverse=True):
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
                st.subheader(f"{file}")
                st.write(content)
    else:
        st.info("Aucune entrée trouvée pour le moment.")
