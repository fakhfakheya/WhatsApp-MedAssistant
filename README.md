# WhatsApp MedAssistant

**Système d’Analyse Médicale et de Réponse Automatisée via WhatsApp**

Un assistant médical automatisé capable de comprendre les messages des patients, détecter les symptômes ou demandes de précautions, et générer des réponses contextualisées via un graphe médical et le modèle LLaMA.

---

## 🚀 Fonctionnalités principales

* Conception d’un graphe de connaissances médicales sous **Neo4j** (maladies, symptômes, précautions)
* **Analyse NLP** des messages WhatsApp et détection de l’intention médicale
* Génération de réponses **contextualisées et naturelles** avec **LLaMA**
* Gestion du contexte conversationnel pour suivi multi-interactions
* Automatisation complète via **n8n** et **Twilio WhatsApp Sandbox**

---

## 🛠️ Outils et Technologies

* **Python** : Backend principal
* **Flask** : API pour réception des messages et génération des réponses
* **Neo4j** : Graphe médical (maladies, symptômes, précautions)
* **n8n** : Orchestration et workflow automatique
* **Twilio WhatsApp Sandbox** : Communication avec les patients
* **Spacy & NLP** : Extraction et normalisation des symptômes
* **Ollama / LLaMA 7B** : Reformulation et génération de réponses naturelles

---

## 🔹 Structure des dossiers et fichiers

* **chatbot_module.py** : Logique principale du chatbot  
* **conversation_memory.py** : Historique des conversations pour chaque utilisateur  
* **handle_symptoms.py** : Extraction et normalisation des symptômes, recherche des maladies  
* **handle_precautions.py** : Recherche des précautions associées aux maladies  
* **llm_response.py** : Interaction avec LLaMA pour générer les réponses  
* **server.py** : API Flask pour réception et envoi des messages  
* **neo4j_setup.cypher** : pour Neo4j  
* **README.md** : Documentation complète  

---

### 🔹 Diagrammes et images

![Graph Neo4j](./neo4j_graph.png)  
![Flow n8n](./n8n_flow.png)
## ⚡ Installation

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/fakhfakheya/WhatsApp-MedAssistant.git
cd WhatsApp-MedAssistant

---


