# 🤖 Chatbot Gemini AI – Flask + Gemini API + Markdown Styling

A fully functional, beautifully styled AI chatbot built with Flask and Google's **Gemini 2.0 Pro API**. 
This chatbot supports styled responses (headings, subheadings, bullet points), and offers a smooth, responsive experience using HTML/CSS/JS frontend.

---

## 🚀 Features

- ✅ Google Gemini 2.0 (Pro) API Integration
- ✅ Styled chat responses (Markdown → HTML formatting)
- ✅ Clean, dark-themed UI with animation
- ✅ Instant scroll-to-bottom behavior
- ✅ Ctrl+Enter for new lines in the input
- ✅ Easy `.env` setup for secrets

---

## 🧱 Tech Stack

- **Backend**: Flask, Python, `google-generativeai`, `flask-cors`, `dotenv`
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Minimalist dark mode with chat bubbles

---

## 📁 Project Structure

chatbot-gemini/
├── app.py # Flask backend
├── .env.example # Sample env file (no key committed)
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend (chat UI)

yaml

## ⚙️ Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/chatbot-gemini.git
cd chatbot-gemini

2. Create Environment File
-- cp .env.example .env
Open .env and add your Gemini API key:
-- GEMINI_API_KEY=your-api-key-here

3. Install Dependencies
-- pip install -r requirements.txt

4. Run the Flask App
-- python app.py
Visit http://localhost:5000 to start chatting!

📦 Dependencies
.txt

Flask
flask-cors
python-dotenv
google-generativeai

Install them with:
-- pip install -r requirements.txt

📝 License
This project is licensed under the MIT License.
