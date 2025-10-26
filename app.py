from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route('/')
def home():
    return "HuquqLab AI xizmati ishga tushdi!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question", "")
    # Bu joyda hozircha AI javobi emulyatsiya qilinadi (keyin haqiqiy OpenAI API ulanadi)
    return jsonify({"answer": f"Siz so‘radingiz: {question}. AI javobi bu yerda chiqadi."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
