# conversation_memory.py

# Dictionnaire pour stocker l'historique par utilisateur
conversation_memory = {}

def add_to_memory(user_id, user_text, intent, bot_response):
    if user_id not in conversation_memory:
        conversation_memory[user_id] = []
    conversation_memory[user_id].append({
        "user_text": user_text,
        "intent": intent,
        "bot_response": bot_response
    })

def get_last_interactions(user_id, n=5):
    """Retourne les n derniers échanges d'un utilisateur"""
    return conversation_memory.get(user_id, [])[-n:]
