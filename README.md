# 🌹 HUDA-BEAUTY-SHIELD (HBS)
**Infrastructure IA Souveraine & Sécurisée pour Huda Beauty**

[![Python 3.12](https://img.shields.io/badge/Python-3.12-gold.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-rose.svg)](https://opensource.org/licenses/MIT)
[![Location: Marseille Hub](https://img.shields.io/badge/Server-Marseille%20(MRS)-blue.svg)]()

## 📌 Vision du Projet
Huda Beauty, leader mondial de la cosmétique basé à Dubaï, doit garantir la confidentialité absolue des données biométriques de ses clientes. **HUDA-BEAUTY-SHIELD** est un prototype d'écosystème propriétaire remplaçant les solutions tierces américaines et asiatiques par une infrastructure souveraine hébergée à **Marseille (France)**.

Le projet assure le pont entre la créativité de Dubaï et la rigueur de la sécurité européenne (RGPD).

---

## 🚀 Architecture Technologique

### 1. Vision Engine (Real Shade Matcher)
Extraction colorimétrique en temps réel via l'espace **CIE L*a*b***. 
- **Modèle :** EfficientNet-B4 (Inférence optimisée).
- **Fonctionnement :** Analyse des pixels centraux de l'image, conversion en vecteur mathématique et comparaison avec le catalogue Huda Beauty par distance euclidienne.

### 2. NLP Engine (Social Pulse)
Analyse des tendances mondiales via le modèle européen **Mistral-7B**.
- **Usage :** Sentiment Analysis sur les réseaux sociaux (Instagram, TikTok).
- **Objectif :** Détection de signaux faibles et aide à la décision pour le développement de nouveaux produits.

### 3. Cyber-Sécurité (The Shield)
- **Privacy by Design :** Destruction immédiate de l'image source après extraction du vecteur.
- **Chiffrement :** Flux sécurisés via **TLS 1.3** et stockage des données sensibles en **AES-256**.
- **Zéro-Trust :** Aucun SDK tiers n'est utilisé dans le cœur du moteur de matching.

---

## 📂 Structure du Projet
```text
HUDA-BEAUTY-SHIELD/
├── core/                # Moteurs IA (Vision & NLP)
│   ├── vision_engine.py # Algorithme de matching colorimétrique
│   └── nlp_engine.py    # Analyse de sentiment via Mistral
├── security/            # Couche de protection
│   └── encryption.py    # Logique de chiffrement AES-256
├── data/                # Bases de données simulées (JSON)
│   ├── huda_catalog.json # 50+ teintes réelles référencées
│   └── trends.json       # Big Data social simulé
├── app.py               # Interface UI Streamlit (Rose Gold)
├── app_test.py          # Script de test de l'infrastructure
└── requirements.txt     # Dépendances du projet

## 📂 Installation & Déploiement
Cloner le dépôt :

```bash
git clone [https://github.com/ton-username/HUDA-BEAUTY-SHIELD.git](https://github.com/ton-username/HUDA-BEAUTY-SHIELD.git)
cd HUDA-BEAUTY-SHIELD
```

Installer les dépendances :
```bash
pip install -r requirements.txt
```
Lancer l'interface utilisateur :
```bash
streamlit run app.py
```
