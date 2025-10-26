from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

# OpenAI API kalitini olish
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "<h1>HuquqLab AI Server ishlayapti!</h1>"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "Savol yuborilmadi"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Siz huquqiy masalalarda yordam beruvchi AI yordamchisiz."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
