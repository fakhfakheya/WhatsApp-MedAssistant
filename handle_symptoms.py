# handle_symptoms.py
import re
import spacy
from neo4j import GraphDatabase

# --- Connexion Neo4j ---
uri = "neo4j://127.0.0.1:7687"
user = "neo4j"
password = "Sami.Eyya123456"
driver = GraphDatabase.driver(uri, auth=(user, password))

nlp = spacy.load("en_core_web_sm")

def normalize_symptom(symptom: str):
    return symptom.lower().replace(" ", "_")

def extract_symptoms(text):
    text_clean = re.sub(r"[^\w\s]", "", text.lower())
    doc = nlp(text_clean)
    words = set([token.text for token in doc] + [token.lemma_ for token in doc])

    query = "MATCH (s:Symptom) RETURN s.name AS name"
    with driver.session() as session:
        result = session.run(query)
        symptoms_list = [record["name"] for record in result]

    found = []
    for symptom in symptoms_list:
        if all(w in words for w in symptom.split("_")):
            found.append(symptom)
    return found

def get_diseases_by_symptoms(symptoms: list):
    if not symptoms:
        return []
    query = """
    MATCH (d:Disease)-[:HAS_SYMPTOM]->(s:Symptom)
    WITH d, collect(s.name) AS disease_symptoms
    WHERE all(symptom IN $symptoms WHERE symptom IN disease_symptoms)
    RETURN d.name AS disease, disease_symptoms
    """
    with driver.session() as session:
        result = session.run(query, symptoms=symptoms)
        diseases = []
        for record in result:
            diseases.append({
                "name": record["disease"],
                "matched_symptoms": record["disease_symptoms"]
            })
        return diseases

def process_symptom_query(text, context=None):
    detected = extract_symptoms(text)
    response = f"🔍 Symptômes détectés : {detected}\n"

    normalized = [normalize_symptom(s) for s in detected]
    diseases = get_diseases_by_symptoms(normalized)

    if diseases:
        for d in diseases:
            response += f"✅ Maladie possible : {d['name']} | Symptômes correspondants : {d['matched_symptoms']}\n"
    else:
        response += "❌ Aucune maladie trouvée avec tous ces symptômes.\n"


    return response
