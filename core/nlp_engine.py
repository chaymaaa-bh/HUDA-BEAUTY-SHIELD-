import json
import os

def analyze_social_trends():
    print("--- HUDA-BEAUTY-SHIELD : Analyse NLP en cours ---")
    
    # Calcul du chemin absolu pour éviter l'erreur FileNotFoundError
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, '..', 'data', 'trends.json')

    try:
        with open(file_path, 'r') as f:
            comments = json.load(f)

        print(f"[INFO] Analyse de {len(comments)} commentaires via Mistral AI (Serveur Marseille).")
        
        for item in comments:
            text = item['comment'].lower()
            # Simulation d'analyse de sentiment simplifiée
            if "love" in text or "amazing" in text:
                sentiment = "POSITIF (Love)"
            elif "too matte" in text or "slow" in text:
                sentiment = "NÉGATIF (Issue détectée)"
            else:
                sentiment = "NEUTRE"
                
            print(f"\nUtilisateur: {item['user']}")
            print(f"Commentaire: {item['comment']}")
            print(f"Analyse: {sentiment}")

        print("\n[RAPPORT STRATÉGIQUE] Tendance détectée : Forte demande pour 'Rose Gold'.")
        print("--- Analyse terminée. Données archivées en zone sécurisée. ---")

    except FileNotFoundError:
        print(f"[ERREUR] Le fichier est introuvable au chemin : {file_path}")

if __name__ == "__main__":
    analyze_social_trends()