import re
from neo4j import GraphDatabase
from handle_symptoms import process_symptom_query, extract_symptoms, normalize_symptom, get_diseases_by_symptoms
from handle_precautions import process_precaution_query

# --- Connexion Neo4j ---
uri = "neo4j://127.0.0.1:7687"
user = "neo4j"
password = "****"
driver = GraphDatabase.driver(uri, auth=(user, password))

# --- Historique des conversations ---
context = {
    "history": [],       # liste de dicts {"user_text": ..., "intent": ...}
    "last_diseases": []  # 🔹 Liste de toutes les maladies détectées
}

def detect_user_intent(text):
    """
    Détecte l'intention de l'utilisateur :
    - "report_symptoms" : s'il décrit ses symptômes
    - "ask_precaution" : s'il demande un soin ou précaution
    - "mention_disease" : s'il mentionne une maladie
    - "unknown" : autre cas
    """
    text_lower = text.lower()
    text_clean = re.sub(r"[^\w\s]", "", text_lower)

    # 1️⃣ Vérifier symptômes connus depuis Neo4j
    query = "MATCH (s:Symptom) RETURN s.name AS name"
    with driver.session() as session:
        result = session.run(query)
        known_symptoms = [record["name"] for record in result]

    for symptom in known_symptoms:
        symptom_words = symptom.split("_")
        if all(w in text_clean for w in symptom_words):
            return "report_symptoms"

    # 2️⃣ Vérifier si le texte demande des soins/précautions
    precaution_keywords = ["precaution", "care", "soin", "treatment", "what to do", "how to treat"]
    if any(k in text_lower for k in precaution_keywords):
        return "ask_precaution"

    # 3️⃣ Vérifier maladies mentionnées
    query = "MATCH (d:Disease) RETURN d.name AS name"
    with driver.session() as session:
        result = session.run(query)
        known_diseases = [record["name"].lower() for record in result]

    for disease in known_diseases:
        if disease in text_lower:
            return "mention_disease"

    # 4️⃣ Cas inconnu
    return "unknown"

