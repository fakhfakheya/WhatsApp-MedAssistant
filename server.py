from flask import Flask, request, jsonify
from chatbot_module import chatbot  # ton fichier avec la fonction chatbot(user_text)

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_text = data.get("user_text", "")
    user_from = data.get("from", "")  # récupère le numéro de l'expéditeur
    response = chatbot(user_text)
    return jsonify({
        "reply": response,
        "from": user_from
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
