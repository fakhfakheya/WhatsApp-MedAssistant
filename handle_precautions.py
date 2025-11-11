# handle_precautions.py
from neo4j import GraphDatabase

# --- Connexion Neo4j ---
uri = "neo4j://127.0.0.1:7687"
user = "neo4j"
password = "Sami.Eyya123456"
driver = GraphDatabase.driver(uri, auth=(user, password))

def get_precautions_for_disease(disease_name: str):
    """Récupère les précautions/soins liés à une maladie depuis Neo4j"""
    query = """
    MATCH (d:Disease {name:$disease_name})-[:HAS_PRECAUTION]->(p:Precaution)
    RETURN p.name AS precaution
    """
    with driver.session() as session:
        result = session.run(query, disease_name=disease_name)
        return [record["precaution"] for record in result]

def process_precaution_query(text, last_disease=None):
    """
    Pipeline pour les précautions :
    - détecte le nom de la maladie dans le texte
    - récupère les précautions depuis Neo4j
    - si aucune maladie dans le texte, utilise last_disease
    """
    # Rechercher les maladies dans le texte
    query = "MATCH (d:Disease) RETURN d.name AS name"
    with driver.session() as session:
        result = session.run(query)
        diseases = [record["name"] for record in result]

    found_disease = None
    text_lower = text.lower()
    for disease in diseases:
        if disease.lower() in text_lower:
            found_disease = disease
            break

    # Si aucune maladie détectée, utiliser celle du contexte
    if not found_disease and last_disease:
        found_disease = last_disease

    if found_disease:
        precautions = get_precautions_for_disease(found_disease)
        if precautions:
            response = f"💊 Précautions pour {found_disease} :\n"
            response += "\n".join(f" - {p}" for p in precautions)
        else:
            response = f"❌ Aucune précaution trouvée pour {found_disease}."
    else:
        response = "❌ Aucun nom de maladie détecté dans le texte."

    return response
