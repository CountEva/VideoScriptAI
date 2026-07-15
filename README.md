# VideoScriptAI

VideoScriptAI is an AI-powered promotional video content generator built using Flask and Groq's LLaMA 3.3-70B Versatile model.

The application helps marketers, businesses, and content creators quickly generate engaging promotional video content, including hooks, promotional scripts, scene suggestions, and call-to-action (CTA) messages.

---

## Features

- AI-powered Hook Generator
- Scene-by-scene Promotional Script Generator
- Visual Scene Suggestion Generator
- Call-to-Action (CTA) Generator
- Generate All Feature
- Flask REST API
- Secure API Key Management using `.env`
- Input Validation and JSON Responses

---

## Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python 3
- Flask
- Flask-CORS

### AI
- Groq API
- LLaMA 3.3-70B Versatile

### Libraries
- python-dotenv
- groq
- flask
- flask-cors

---

## Project Structure

```
VideoScriptAI/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/CountEva/VideoScriptAI.git
```

Move into the project directory:

```bash
cd VideoScriptAI
```

Create a virtual environment:

```bash
python -m venv videoscriptai-env
```

Activate the virtual environment (Windows):

```powershell
.\videoscriptai-env\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your Groq API key:

```text
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
python app.py
```

Open the application in your browser:

```
http://127.0.0.1:5000
```

---

## Application Modules

- Hook Generator
- Script Generator
- Scene Generator
- CTA Generator
- Generate All

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home page |
| `/api/hook` | Generate Hook |
| `/api/script` | Generate Script |
| `/api/scenes` | Generate Scene Suggestions |
| `/api/cta` | Generate CTA |
| `/api/generate-all` | Generate all promotional content |

---

## Demo

Demo video:

*Add the Google Drive or YouTube link here.*

---

## Developed By

**Mohit Atkaan**

B.Tech Gaming & Technology

Manav Rachna International Institute of Research & Studies

---

## License

This project was developed for educational purposes.
