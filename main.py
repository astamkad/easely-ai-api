from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Initialize OpenAI client correctly
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Ensure request is JSON
        data = request.get_json(force=True)  # This prevents 400 errors

        # Check if 'prompt' exists
        if "prompt" not in data:
            return jsonify({"error": "Missing 'prompt' parameter"}), 400

        prompt = data["prompt"]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        # Send only the response text, no extra nesting
        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
