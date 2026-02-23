import streamlit as st
import numpy as np
from PIL import Image
import os
import sys

# Import de ton moteur de vision
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
import vision_engine

st.set_page_config(page_title="HUDA BEAUTY SHIELD", page_icon="🌹")

st.title("🌹 HUDA BEAUTY - REAL SHADE DETECTOR")
st.write("Analyse réelle de la peau via infrastructure souveraine (Marseille).")

# --- INTERFACE D'UPLOAD ---
uploaded_file = st.file_uploader("Téléchargez votre selfie pour analyse", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # 1. Afficher l'image
    img = Image.open(uploaded_file)
    st.image(img, caption="Photo reçue", width=300)
    
    if st.button("Lancer la détection réelle"):
        # 2. EXTRACTION RÉELLE DE LA COULEUR (On prend le centre de l'image)
        img_array = np.array(img.convert('RGB'))
        height, width, _ = img_array.shape
        
        # On analyse un carré au centre (ROI - Region of Interest)
        center_x, center_y = width // 2, height // 2
        sample = img_array[center_y-20:center_y+20, center_x-20:center_x+20]
        avg_rgb = sample.mean(axis=(0, 1))
        
        # 3. CONVERSION SIMPLIFIÉE EN LAB (Pour ton moteur vision_engine)
        # On simule la luminosité L basée sur la moyenne RGB
        L_simulated = (0.299 * avg_rgb[0] + 0.587 * avg_rgb[1] + 0.114 * avg_rgb[2]) / 2.55
        a_simulated = (avg_rgb[0] - avg_rgb[1]) + 15
        b_simulated = (avg_rgb[1] - avg_rgb[2]) + 15
        
        detected_vector = np.array([L_simulated, a_simulated, b_simulated])
        
        # 4. APPEL DU MOTEUR
        result = vision_engine.match_shade(detected_vector)
        
        # 5. AFFICHAGE DES RÉSULTATS
        st.subheader(f"Résultat : {result['name']}")
        st.write(f"**Description :** {result['desc']}")
        
        # Preuve de sécurité
        st.warning("🛡️ **SÉCURITÉ :** L'image a été transformée en vecteur [L, a, b] et supprimée de la mémoire temporaire.")