from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Initialize OpenAI client correctly
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Change to "gpt-4" if needed
            messages=[{"role": "user", "content": prompt}]
        )
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
