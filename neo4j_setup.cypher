// ================================
// Neo4j Setup pour WhatsApp MedAssistant
// ================================

// 1️⃣ Créer les contraintes d’unicité
CREATE CONSTRAINT IF NOT EXISTS ON (d:Disease) ASSERT d.name IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS ON (s:Symptom) ASSERT s.name IS UNIQUE;
CREATE CONSTRAINT IF NOT EXISTS ON (p:Precaution) ASSERT p.name IS UNIQUE;

// 2️⃣ Créer les nœuds Disease
LOAD CSV WITH HEADERS FROM 'file:///diseases.csv' AS row
MERGE (d:Disease {name: row.Disease});

// 2️⃣ Créer les nœuds Symptom
LOAD CSV WITH HEADERS FROM 'file:///diseases.csv' AS row
UNWIND [row.Symptom_1, row.Symptom_2, row.Symptom_3, row.Symptom_4, row.Symptom_5,
        row.Symptom_6, row.Symptom_7, row.Symptom_8, row.Symptom_9, row.Symptom_10,
        row.Symptom_11, row.Symptom_12, row.Symptom_13, row.Symptom_14, row.Symptom_15,
        row.Symptom_16, row.Symptom_17] AS symptom_name
MERGE (s:Symptom {name: symptom_name});

// 2️⃣ Créer les nœuds Precaution
LOAD CSV WITH HEADERS FROM 'file:///precautions.csv' AS row
UNWIND [row.Precaution_1, row.Precaution_2, row.Precaution_3, row.Precaution_4] AS precaution_name
MERGE (p:Precaution {name: precaution_name});

// 3️⃣ Créer les relations Disease -> Symptom
LOAD CSV WITH HEADERS FROM 'file:///disease_symptom.csv' AS row
MATCH (d:Disease {name: row.disease})
MATCH (s:Symptom {name: row.symptom})
MERGE (d)-[:HAS_SYMPTOM]->(s);

// 3️⃣ Créer les relations Disease -> Precaution
LOAD CSV WITH HEADERS FROM 'file:///disease_precaution.csv' AS row
MATCH (d:Disease {name: row.disease})
MATCH (p:Precaution {name: row.precaution})
MERGE (d)-[:HAS_PRECAUTION]->(p);
