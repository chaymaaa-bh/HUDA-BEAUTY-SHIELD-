from cryptography.fernet import Fernet

# Simulation de génération de clé (Souveraine)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_result(shade_id):
    """Chiffre l'ID du produit avant l'envoi au serveur."""
    encrypted_id = cipher.encrypt(shade_id.encode())
    return encrypted_id

# Démo de sécurité pour l'oral
if __name__ == "__main__":
    secret = encrypt_result("200B-Shortbread")
    print(f"ID envoyé vers Marseille (Chiffré) : {secret}")