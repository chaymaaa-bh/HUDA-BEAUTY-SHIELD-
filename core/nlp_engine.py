import json
import os

def analyze_social_trends():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, '..', 'data', 'trends.json')

    try:
        if not os.path.exists(file_path):
            return "Fichier data/trends.json introuvable."

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        results = []
        for item in data:
            # On cherche le texte par priorité : 'comment', puis 'text', puis 'body'
            content = item.get('comment') or item.get('text') or item.get('body') or "Pas de texte trouvé"
            user = item.get('user') or item.get('username') or item.get('author') or "Anonyme"
            
            text_lower = content.lower()
            if any(w in text_lower for w in ["love", "amazing", "best", "perfect"]):
                sentiment = "POSITIF (Love)"
            elif any(w in text_lower for w in ["matte", "slow", "strong", "issue"]):
                sentiment = "NÉGATIF (Alerte)"
            else:
                sentiment = "NEUTRE"
            
            results.append({
                "user": user,
                "comment": content,
                "analysis": sentiment
            })
        return results
    except Exception as e:
        return f"Erreur : {str(e)}"