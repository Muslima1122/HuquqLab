import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API kalitini muhit o'zgaruvchisidan olamiz
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "<h1>HuquqLab ishga tushdi!</h1><p>Bu sahifa Render orqali ishlaydi.</p>"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")
    if not question:
        return jsonify({"error": "Savol kiritilmadi"}), 400
    
    # OpenAI javobi
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}]
        )
        answer = response.choices[0].message.content
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render port
    app.run(host="0.0.0.0", port=port)
