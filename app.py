from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("API_Key")
genai.configure(api_key=api_key)

# To Show how many models are available through 'Key' with 'input tokens'
models = genai.list_models()
for m in models:
    print(m.name, m.supported_generation_methods, m.input_token_limit)
# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Gemini model setup
model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp")
chat_session = model.start_chat()

@app.route('/')
def home():
    return render_template("index.html")  # Make sure templates/index.html exists

@app.route('/chat', methods=['GET','POST'])
def chat():
    user_input = request.json.get('message')
    try:
        response = chat_session.send_message(user_input)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)