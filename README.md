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

## 📁 Structure du projet

