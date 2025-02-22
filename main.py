from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Ensure request is JSON
        data = request.get_json(force=True)

        # Log the received request data
        print(f"Received data: {data}")

        # Check if 'prompt' exists
        if "prompt" not in data:
            return jsonify({"error": "Missing 'prompt' parameter"}), 400

        prompt = data["prompt"]
        print(f"User Prompt: {prompt}")  # Log user input

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        ai_response = response.choices[0].message.content
        print(f"AI Response: {ai_response}")  # Log AI output

        return jsonify({"response": ai_response})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
