from flask import Flask, request, jsonify
from chatbot import chat_with_bot

app = Flask(__name__)
chat_history_ids = None

# Custom, empathetic scripted replies
empathy_lookup = {
    "stress": "I'm sorry to hear you're feeling stressed. Taking deep breaths or a short walk can sometimes help. Want to talk more about it?",
    "anxious": "When you're feeling anxious, it can help to slow down and breathe deeply. Do you want to share more about what's making you anxious?",
    "calm down": "Try a deep breathing exercise: Inhale slowly for 4 counts, hold for 4, exhale for 4. I'm here for you.",
    "feel better": "Taking care of yourself when you're down is important. Can I suggest trying a favorite hobby or calling a friend?",
    "relax": "Listening to calming music, gentle exercise, or mindfulness can help you relax. How are you feeling right now?",
    "sad": "It's okay to feel sad sometimes. If you want to talk about it, I'm here to listen.",
    "positive": "Remember, even small steps count. Celebrate little victories and be kind to yourself."
    # You can add more triggers and responses as needed.
}

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history_ids
    user_msg = request.json.get("message").lower()

    # Check for negative keyword triggers
    for key in empathy_lookup:
        if key in user_msg:
            return jsonify({"reply": empathy_lookup[key]})

    # Default to chatbot model if no keyword matched
    reply, chat_history_ids = chat_with_bot(user_msg, chat_history_ids)
    if not reply.strip():
        reply = "I'm here to listen whenever you want to share."
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
