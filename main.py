import streamlit as st

st.set_page_config(page_title="Langues pour Tous", layout="centered")

# En-tête
st.title("🌍 Langues pour Tous")
st.subheader("Association de cours de langues étrangères")

# Présentation
st.markdown("""
Bienvenue sur notre plateforme !  
Nous proposons des **cours de langues** accessibles à tous :
- 🇸🇦 Arabe


📍 *Lieu : Maison des Associations, Lyon*  
📅 *Horaires flexibles en semaine*  
📧 *Contact : langues.pour.tous@example.org*
""")

# Formulaire de contact simulé
st.markdown("## 📬 Nous contacter")
with st.form("contact_form"):
    nom = st.text_input("Votre nom")
    email = st.text_input("Votre email")
    message = st.text_area("Votre message")

    submitted = st.form_submit_button("Envoyer")
    if submitted:
        st.success("✅ Merci pour votre message ! (simulation)")
