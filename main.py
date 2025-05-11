import streamlit as st
import requests

st.set_page_config(page_title="Langues pour Tous", layout="centered")

# Titre et sous-titre
st.title("🌍 Langues pour Tous")
st.subheader("Association de cours de langues étrangères")

# Présentation
st.markdown("""
Bienvenue !  
Notre association propose des **cours de langues arabe accessibles à tous**, animés par :


- 🇸🇦 Arabe

📍 *Lieu : Maison des Associations, Courbevoie *  
📅 *Horaires flexibles en semaine*  
""")

# Formulaire de contact
st.markdown("## 📬 Contactez-nous")

with st.form("contact_form"):
    nom = st.text_input("Votre nom")
    email = st.text_input("Votre email")
    message = st.text_area("Votre message")

    submitted = st.form_submit_button("Envoyer")

    if submitted:
        # 🔁 Remplace cette URL par celle fournie par Formspree
        formspree_url = "https://formspree.io/f/abcxyzde"

        # Préparation des données
        data = {
            "name": nom,
            "email": email,
            "message": message
        }

        # Envoi du message
        try:
            response = requests.post(formspree_url, data=data)
            if response.status_code == 200:
                st.success("✅ Votre message a été envoyé avec succès !")
            else:
                st.error("❌ Une erreur est survenue. Veuillez réessayer plus tard.")
        except Exception as e:
            st.error("❌ Impossible d'envoyer le message. Vérifiez votre connexion.")
