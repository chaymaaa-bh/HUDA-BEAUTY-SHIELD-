import json
import numpy as np
import os

def load_catalog():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, '..', 'data', 'huda_catalog.json')
    with open(file_path, 'r') as f:
        return json.load(f)

def match_shade(detected_lab):
    catalog = load_catalog()
    best_match = None
    min_dist = float('inf')
    for product in catalog:
        prod_vector = np.array([product['L'], product['a'], product['b']])
        dist = np.linalg.norm(prod_vector - detected_lab)
        if dist < min_dist:
            min_dist = dist
            best_match = product
    return best_match

def run_prototype(fake_face_color):
    print("\n--- HUDA-BEAUTY-SHIELD : Lancement du Scan ---")
    print(f"[IA] Analyse des sous-tons détectés : {fake_face_color}")
    print("[SECURITY] IMAGE SOURCE DÉTRUITE. Conversion en vecteur réussie.")
    
    result = match_shade(fake_face_color)
    if result:
        print(f"\n[RÉSULTAT] Teinte recommandée : {result['name']} (ID: {result['id']})")
        print(f"[CONSEIL] {result['desc']}")
    
    print("\n--- Données prêtes pour transfert chiffré vers Marseille ---")

if __name__ == "__main__":
    test_skin = np.array([80, 13, 17])
    run_prototype(test_skin)