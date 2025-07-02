import streamlit as st
import os
from datetime import datetime
from openai import OpenAI

# ---- CONFIG ----
# Initialise le client OpenAI avec ta clé API (définie dans tes secrets Streamlit Cloud)
client = OpenAI()

# ---- TITRE ----
st.title("🌟 Mon Journal Intime avec Coach IA 🌟")
st.write("Un espace pour te confier et recevoir un boost quotidien !")

# ---- SECTION MESSAGE MOTIVATION ----
if st.button("✨ Génère mon boost du jour !"):
    with st.spinner("L'IA réfléchit à ton message motivant..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un coach de motivation optimiste, bienveillant et pragmatique."
                },
                {
                    "role": "user",
                    "content": "Donne-moi un boost pour aujourd'hui !"
                }
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
