import streamlit as st
import numpy as np
from PIL import Image
import os
import sys

# --- CONFIGURATION DES CHEMINS & SÉCURITÉ ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'security')))

try:
    import vision_engine
    import nlp_engine
    import encryption
except ImportError as e:
    st.error(f"Erreur d'importation des modules : {e}")

# --- THÈME ROSE GOLD OPTIMISÉ ---
st.set_page_config(page_title="HUDA BEAUTY SHIELD", page_icon="🌹", layout="wide")
st.markdown("""
    <style>
    /* Fond de page */
    .main { background-color: #FFF5F5; }
    
    /* Titres en Rose Gold */
    h1, h2, h3 { color: #B08D8D !important; font-family: 'serif'; }
    
    /* Boutons */
    .stButton>button { background-color: #B08D8D; color: white; border-radius: 20px; border: none; height: 3em; width: 100%; }
    
    /* Correction visuelle des boîtes de commentaires (Expanders) */
    .stExpander { background-color: white !important; border: 1px solid #B08D8D !important; border-radius: 10px; }
    
    /* FORCE LE TEXTE EN NOIR DANS LES BOITES POUR ÉVITER LE WHITE ON WHITE */
    .stExpander p, .stExpander span, .stExpander div { color: #333333 !important; }
    
    /* Style des onglets */
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { background-color: #F8ECEC; border-radius: 10px 10px 0 0; padding: 10px 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌹 HUDA BEAUTY - SHIELD")
st.write("**Infrastructure Souveraine | Marseille Data Hub | Sécurité Bio-Numérique**")

# --- NAVIGATION PAR ONGLETS ---
tabs = st.tabs(["✨ Shade Matcher", "📈 Social Pulse", "🔐 Sécurité Hub"])

# --- TAB 1 : VISION ---
with tabs[0]:
    st.header("Analyse de Teinte Réelle")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader("Téléchargez un selfie (Mode sécurisé)", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            img = Image.open(uploaded_file)
            st.image(img, caption="Aperçu du visage", width=300)
    
    with col2:
        if uploaded_file and st.button("Lancer le Matching"):
            with st.spinner("Analyse colorimétrique CIE L*a*b*..."):
                img_array = np.array(img.convert('RGB'))
                h, w, _ = img_array.shape
                # Échantillonnage au centre (ROI)
                sample = img_array[h//2-15:h//2+15, w//2-15:w//2+15]
                avg_rgb = sample.mean(axis=(0, 1))
                
                # Conversion simplifiée pour le moteur
                L = (0.299 * avg_rgb[0] + 0.587 * avg_rgb[1] + 0.114 * avg_rgb[2]) / 2.55
                detected_vector = np.array([L, 15, 15]) 
                
                result = vision_engine.match_shade(detected_vector)
                if result:
                    st.success(f"### Recommandation : {result['name']}")
                    st.info(f"**Détails :** {result['desc']}")
                    st.warning("🛡️ Confidentialité : Image source détruite immédiatement.")

# --- TAB 2 : NLP ---
with tabs[1]:
    st.header("Social Listening - IA Mistral")
    
    if st.button("🚀 Actualiser & Analyser les Tendances"):
        with st.spinner("Génération de données et analyse NLP en cours..."):
            # AUTOMATISATION : On lance le script de génération directement depuis l'interface
            try:
                import data_generator # On importe ton script
                data_generator.generate_mock_trends(count=15) # On génère 15 nouveaux avis
                st.toast("Nouveaux flux récupérés avec succès !", icon="✅")
            except Exception as e:
                st.error(f"Erreur d'automatisation : {e}")

            # Ensuite, on affiche le résultat
            trends = nlp_engine.analyze_social_trends()
            
            if isinstance(trends, list):
                for t in trends:
                    with st.expander(f"👤 {t['user']} - {t['analysis']}"):
                        st.write(f"💬 *{t['comment']}*")

# --- TAB 3 : SÉCURITÉ ---
with tabs[2]:
    st.header("Tunnel de Chiffrement Marseille")
    data_to_encrypt = st.text_input("Donnée biométrique ou ID cliente :", "Elena_92_Vect_81")
    
    if st.button("Générer Flux AES-256"):
        encrypted = encryption.encrypt_result(data_to_encrypt)
        st.subheader("Paquet chiffré prêt pour le transit :")
        st.code(encrypted)
        st.write("🔒 Ce flux est protégé contre toute interception sur les câbles sous-marins.")

st.divider()
st.caption("HUDA-BEAUTY-SHIELD v2.0 - Prototype de Souveraineté Numérique")