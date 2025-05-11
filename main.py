{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab782703-81e0-4a40-ac06-bffbb1722773",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Choisir le nom du fichier Streamlit\n",
    "filename = \"main.py\"\n",
    "\n",
    "# Code Python Streamlit\n",
    "streamlit_code = '''\n",
    "import streamlit as st\n",
    "\n",
    "st.set_page_config(page_title=\"Langues pour Tous\", layout=\"centered\")\n",
    "\n",
    "st.title(\"🌍 Langues pour Tous\")\n",
    "st.subheader(\"Association de cours de langues étrangères\")\n",
    "\n",
    "st.markdown(\"\"\"\n",
    "Bienvenue sur notre plateforme !  \n",
    "Nous proposons des **cours de langues** :\n",
    "- 🇫🇷 Français langue étrangère\n",
    "- 🇬🇧 Anglais\n",
    "- 🇪🇸 Espagnol\n",
    "- 🇸🇦 Arabe\n",
    "- 🇨🇳 Chinois\n",
    "\n",
    "📍 *Lieu : Maison des Associations, Lyon*  \n",
    "📅 *Horaires flexibles*  \n",
    "📧 *Contact : langues.pour.tous@example.org*\n",
    "\"\"\")\n",
    "\n",
    "st.markdown(\"## 📬 Nous contacter\")\n",
    "with st.form(\"contact_form\"):\n",
    "    nom = st.text_input(\"Votre nom\")\n",
    "    email = st.text_input(\"Votre email\")\n",
    "    message = st.text_area(\"Votre message\")\n",
    "\n",
    "    submitted = st.form_submit_button(\"Envoyer\")\n",
    "    if submitted:\n",
    "        st.success(\"✅ Merci pour votre message ! (simulation)\")\n",
    "'''\n",
    "\n",
    "# Écriture du fichier .py\n",
    "with open(filename, \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(streamlit_code.strip())\n",
    "\n",
    "# requirements.txt\n",
    "with open(\"requirements.txt\", \"w\") as f:\n",
    "    f.write(\"streamlit\")\n",
    "\n",
    "print(f\"✅ Fichiers {filename} et requirements.txt créés.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
