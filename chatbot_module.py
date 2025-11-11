# chatbot_module.py
from detect_intent import detect_user_intent, context
from handle_symptoms import process_symptom_query
from handle_precautions import process_precaution_query
from llm_response import llm_response  # ta fonction LLM

def chatbot(user_text):
    intent = detect_user_intent(user_text)
    context["history"].append({"user_text": user_text, "intent": intent})
    response = ""

    # 🔹 Traitement selon l'intention
    if intent == "report_symptoms":
        response = process_symptom_query(user_text, context=context["history"])
        llm_prompt = (
            "Tu es un assistant médical professionnel. "
            "Réponds uniquement par du texte clair, naturel et utile à l'utilisateur, "
            "sans jamais inclure de gestes, d'émoticônes, de notes entre astérisques, "
            "ou des expressions comme 'smile', 'listen', 'adjusts glasses'. "
            "Liste toutes les maladies détectées et leurs symptômes exactement comme fourni ci-dessous :\n"
            f"{response}"
        )
    elif intent == "ask_precaution":
        response = process_precaution_query(user_text)
        llm_prompt = (
            "Tu es un assistant médical professionnel. "
            "Réponds uniquement par du texte clair, naturel et utile à l'utilisateur, "
            "sans jamais inclure de gestes, d'émoticônes, de notes entre astérisques, "
            "ou des expressions comme 'smile', 'listen', 'adjusts glasses'. "
            "Liste toutes les précautions exactement comme fourni ci-dessous :\n"
            f"{response}"
        )
    else:
        # Cas où l'intention est inconnue, mais on garde le contexte médical
        llm_prompt = (
            "Tu es un assistant médical professionnel. "
            f"L'utilisateur a dit : '{user_text}'. "
            f"Voici le contexte des symptômes détectés jusqu'à présent : {context['history']}. "
            "Réponds uniquement par du texte clair, naturel et utile, "
            "sans jamais inclure de gestes, d'émoticônes, de notes entre astérisques, "
            "ou des expressions comme 'smile', 'listen', 'adjusts glasses'. "
            "Pose des questions seulement si nécessaire pour clarifier les symptômes."
        )

    # 🔹 Génération finale avec le LLM
    llm_reply = llm_response(llm_prompt)
    response = llm_reply

    return response
