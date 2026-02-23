import json
import random

users = ["BeautyLover", "MUA_Pro", "HudaFan", "SkinCareQueen", "DubaiPrincess", "ParisianChic"]
comments = [
    "I love the coverage but the shade is a bit too yellow.",
    "Best foundation ever, 100% match!",
    "Mistral AI suggested this shade and it is perfect.",
    "The delivery to Marseille was so fast!",
    "We need more rose gold packaging!",
    "Is this formula vegan? I love the texture.",
    "The privacy features of this app are top notch."
]

def generate_mock_trends(count=50):
    data = []
    for i in range(count):
        data.append({
            "user": f"{random.choice(users)}_{i}",
            "comment": random.choice(comments),
            "platform": random.choice(["Instagram", "TikTok", "X"]),
            "sentiment_score": round(random.uniform(0.5, 1.0), 2)
        })
    
    with open('data/trends.json', 'w') as f:
        json.dump(data, f, indent=2)
    print(f"[SUCCESS] {count} commentaires générés dans data/trends.json")

if __name__ == "__main__":
    generate_mock_trends()