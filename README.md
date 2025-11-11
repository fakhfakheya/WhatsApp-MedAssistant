WhatsApp MedAssistant

Système d’Analyse Médicale et de Réponse Automatisée via WhatsApp

Un assistant médical automatisé capable de comprendre les messages des patients, détecter les symptômes ou demandes de précautions, et générer des réponses contextualisées via un graphe médical et le modèle LLaMA.

🚀 Fonctionnalités principales

Conception d’un graphe de connaissances médicales sous Neo4j (maladies, symptômes, précautions)

Analyse NLP des messages WhatsApp et détection de l’intention médicale

Génération de réponses contextualisées et naturelles avec LLaMA

Gestion du contexte conversationnel pour suivi multi-interactions

Automatisation complète via n8n et Twilio WhatsApp Sandbox : réception, traitement et réponse automatique

🛠️ Outils et Technologies

Python : Backend principal

Flask : API pour réception des messages et génération des réponses

Neo4j : Graphe médical (maladies, symptômes, précautions)

n8n : Orchestration et workflow automatique

Twilio WhatsApp Sandbox : Communication avec les patients

Spacy & NLP : Extraction et normalisation des symptômes

Ollama / LLaMA 7B : Reformulation et génération de réponses naturelles

📁 Structure du projet
app4doc/
├─ chatbot_module.py        # Logique principale du chatbot
├─ conversation_memory.py   # Gestion du contexte et historique
├─ handle_symptoms.py       # Extraction et recherche des symptômes
├─ handle_precautions.py    # Recherche des précautions pour chaque maladie
├─ llm_response.py          # Interaction avec LLaMA
├─ server.py                # API Flask
├─ neo4j_import/            # CSV pour import dans Neo4j
└─ README.md

⚡ Installation

Cloner le dépôt :

git clone https://github.com/fakhfakheya/WhatsApp-MedAssistant.git
cd WhatsApp-MedAssistant


Créer un environnement Python :

python -m venv venv
source venv/bin/activate  # mac/linux
venv\Scripts\activate     # Windows


Installer les dépendances :

pip install -r requirements.txt

🔹 Setup Neo4j

Avant de lancer le chatbot, il faut importer les données dans Neo4j :

Créer les contraintes d’unicité pour éviter les doublons

Créer les nœuds Disease, Symptom et Precaution

Créer les relations Disease -> Symptom et Disease -> Precaution

Toutes les commandes sont dans le fichier neo4j_setup.cypher

🔹 Workflow n8n & Intégration Twilio

Le projet utilise n8n pour orchestrer l’automatisation complète de la réception, du traitement et de l’envoi de messages WhatsApp via Twilio.

1️⃣ Composants n8n utilisés
Composant	Rôle
Webhook	Point d’entrée pour recevoir les messages WhatsApp de Twilio
HTTP Request	Appel à l’API Flask (/chat) pour envoyer le texte utilisateur et recevoir la réponse générée par le chatbot
Set / Edit Fields	Préparer et formater les données reçues ou à envoyer
Twilio – Send SMS / MMS / WhatsApp	Envoyer la réponse automatiquement au patient via WhatsApp
2️⃣ Exemple de flow n8n

Webhook

Type : POST

URL exposée : https://<votre_n8n_instance>/webhook/whatsapp

Payload attendu :

{ "From": "<numéro>", "Body": "<message_utilisateur>" }


HTTP Request

Méthode : POST

URL : http://localhost:5000/chat (API Flask)

Body :

{ "user_text": {{$json["Body"]}}, "from": {{$json["From"]}} }


Set / Edit Fields

Préparer les champs nécessaires pour Twilio

Exemple :

{
  "To": "{{$json['From']}}",
  "Body": "{{$json['reply']}}"
}


Twilio – Send WhatsApp

From : numéro Twilio Sandbox (whatsapp:+14155238886)

To : numéro du patient

Body : réponse du chatbot

3️⃣ Configuration Twilio

Créer un compte sur Twilio

Accéder au WhatsApp Sandbox et suivre les instructions pour connecter votre numéro

Copier le Account SID, Auth Token, et numéro sandbox

Dans n8n, configurer le nœud Twilio avec ces informations

Tester l’envoi de messages depuis n8n pour vérifier que le flow fonctionne

### 🔹 Graph médical Neo4j
Le graphe montre les nœuds `Disease`, `Symptom` et `Precaution` et leurs relations.
![Graph médical Neo4j](assets/neo4j_graph.png)

### 🔹 Flow n8n et composants
Le diagramme illustre le workflow n8n : Webhook, HTTP Request, Set/Fields, Twilio Send WhatsApp.
![Flow n8n](assets/n8n_flow.png)
