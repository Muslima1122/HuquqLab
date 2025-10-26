from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# OpenAI API kalitini Render'dagi Environment Variables orqali ulaysan
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "Savol yuborilmadi."}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        answer = response.choices[0].message["content"]
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
