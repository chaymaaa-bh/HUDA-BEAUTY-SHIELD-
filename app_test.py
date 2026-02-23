import sys
import os
import numpy as np

# On force Python à regarder dans les dossiers core et security
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'security')))

# Imports des fonctions spécifiques
try:
    from vision_engine import run_prototype
    from nlp_engine import analyze_social_trends
    from encryption import encrypt_result
    print("[SUCCESS] Système HUDA-SHIELD chargé.\n")
except ImportError as e:
    print(f"[ERROR] Problème d'import : {e}")
    sys.exit(1)

def run_full_demo():
    print("==============================================")
    print("   DEMO : HUDA-BEAUTY-SHIELD (MARSEILLE HUB)  ")
    print("==============================================\n")

    # STEP 1: Vision
    fake_skin_tone = np.array([81, 13, 17])
    run_prototype(fake_skin_tone)
    
    # STEP 2: Sécurité
    print("\n[STEP 2] Sécurisation des données...")
    secret_data = encrypt_result("Shortbread-200B")
    print(f"Flux chiffré prêt pour Marseille : {secret_data[:30]}...")

    # STEP 3: NLP
    print("\n[STEP 3] Lancement du Social Listening...")
    analyze_social_trends()

    print("\n==============================================")
    print("      TEST TERMINÉ : SYSTÈME OPÉRATIONNEL     ")
    print("==============================================")

if __name__ == "__main__":
    run_full_demo()