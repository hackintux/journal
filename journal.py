# fichier : app_journal_ia.py
import streamlit as st
import os
from datetime import datetime
import openai

# ---- CONFIG ----
# Place ici ta clé API OpenAI ou utilise une variable d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

# ---- TITRE ----
st.title("🌟 Mon Journal Intime avec Coach IA 🌟")
st.write("Un espace pour te confier et recevoir un boost quotidien !")

# ---- SECTION MESSAGE MOTIVATION ----
if st.button("✨ Génère mon boost du jour !"):
    with st.spinner("L'IA réfléchit à ton message motivant..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # utilise un modèle adapté à ta clé API
            messages=[
                {"role": "system", "content": "Tu es un coach de motivation optimiste et bienveillant."},
                {"role": "user", "content": "Donne-moi un boost pour aujourd'hui !"}
            ]
        )
        boost = response.choices[0].message.content
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
