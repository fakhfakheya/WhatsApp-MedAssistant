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

**Graph Neo4j** – Ce graphe montre la structure des nœuds et relations entre maladies, symptômes et précautions.  
![Graph Neo4j](./neo4j_graph.png)  

**Flow n8n** – Diagramme illustrant le workflow n8n : Webhook, HTTP Request, Set/Edit Fields, et envoi via Twilio WhatsApp.  
![Flow n8n](./n8n_flow.png)

---
### 2️⃣ Configurer Twilio et le workflow n8n

Le projet utilise **n8n** pour orchestrer l’automatisation complète de la réception, du traitement et de l’envoi de messages WhatsApp via **Twilio**.

#### Composants n8n utilisés

| Composant                     | Rôle |
|--------------------------------|------|
| Webhook                        | Point d’entrée pour recevoir les messages WhatsApp de Twilio |
| HTTP Request                   | Appel à l’API Flask (/chat) pour envoyer le texte utilisateur et recevoir la réponse générée par le chatbot |
| Set / Edit Fields              | Préparer et formater les données reçues ou à envoyer |
| Twilio – Send SMS / MMS / WhatsApp | Envoyer la réponse automatiquement au patient via WhatsApp |

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/fakhfakheya/WhatsApp-MedAssistant.git
cd WhatsApp-MedAssistant
