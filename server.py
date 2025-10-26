from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# OpenAI API kalitini Render muhitida sozlaysiz (pastda ko‘rsataman)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"reply": "Savol yuborilmadi."})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    ai_reply = response.choices[0].message.content
    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
