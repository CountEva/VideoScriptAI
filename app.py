from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime
import os

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# -----------------------------
# Flask Setup
# -----------------------------
app = Flask(__name__)
CORS(app)

MODEL = "llama-3.3-70b-versatile"


# -----------------------------
# AI Call Function
# -----------------------------
def call_ai(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert marketing and promotional video content creator."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.8,
            max_tokens=1024,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# -----------------------------
# Prompt Builders
# -----------------------------
def generate_hook(product, description, audience, goal):

    prompt = f"""
Generate ONE attention-grabbing marketing hook.

Rules:
- Maximum 20 words.
- Begin with a question, surprising fact, or bold statement.
- Product: {product}
- Description: {description}
- Target Audience: {audience}
- Campaign Goal: {goal}
"""

    return call_ai(prompt)


def generate_script(product, description, audience, goal, duration):

    prompt = f"""
Write a promotional video script.

Product:
{product}

Description:
{description}

Audience:
{audience}

Campaign Goal:
{goal}

Duration:
{duration} seconds

Instructions:
- Approximately one sentence every 3 seconds.
- Maximum 3 scenes.
- Format:

[SCENE 1]
Scene Description:
Voiceover:

[SCENE 2]
Scene Description:
Voiceover:
"""

    return call_ai(prompt)


def generate_scenes(product, description, audience, goal):

    prompt = f"""
Suggest exactly THREE engaging visual scenes.

Each scene should contain:
- 2-3 sentences
- Practical camera shots
- Match the campaign goal

Product:
{product}

Description:
{description}

Audience:
{audience}

Campaign Goal:
{goal}
"""

    return call_ai(prompt)


def generate_cta(product, audience, goal):

    prompt = f"""
Generate ONE Call-To-Action.

Rules:
- Maximum 25 words.
- Encourage action.
- Mention where to purchase if appropriate.

Product:
{product}

Audience:
{audience}

Campaign Goal:
{goal}
"""

    return call_ai(prompt)


# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Validation
# -----------------------------
def validate(data):

    required = [
        "product",
        "description",
        "audience",
        "goal"
    ]

    for field in required:
        if not data.get(field):
            return False, field

    return True, None


# -----------------------------
# Generate Hook
# -----------------------------
@app.route("/api/generate-hook", methods=["POST"])
def api_hook():

    data = request.json

    valid, missing = validate(data)

    if not valid:
        return jsonify({
            "error": f"Missing field: {missing}"
        }), 400

    result = generate_hook(
        data["product"],
        data["description"],
        data["audience"],
        data["goal"]
    )

    return jsonify({
        "result": result,
        "timestamp": datetime.utcnow().isoformat()
    })


# -----------------------------
# Generate Script
# -----------------------------
@app.route("/api/generate-script", methods=["POST"])
def api_script():

    data = request.json

    valid, missing = validate(data)

    if not valid:
        return jsonify({
            "error": f"Missing field: {missing}"
        }), 400

    duration = data.get("duration", 30)

    result = generate_script(
        data["product"],
        data["description"],
        data["audience"],
        data["goal"],
        duration
    )

    return jsonify({
        "result": result,
        "timestamp": datetime.utcnow().isoformat()
    })


# -----------------------------
# Generate Scenes
# -----------------------------
@app.route("/api/generate-scenes", methods=["POST"])
def api_scenes():

    data = request.json

    valid, missing = validate(data)

    if not valid:
        return jsonify({
            "error": f"Missing field: {missing}"
        }), 400

    result = generate_scenes(
        data["product"],
        data["description"],
        data["audience"],
        data["goal"]
    )

    return jsonify({
        "result": result,
        "timestamp": datetime.utcnow().isoformat()
    })


# -----------------------------
# Generate CTA
# -----------------------------
@app.route("/api/generate-cta", methods=["POST"])
def api_cta():

    data = request.json

    valid, missing = validate(data)

    if not valid:
        return jsonify({
            "error": f"Missing field: {missing}"
        }), 400

    result = generate_cta(
        data["product"],
        data["audience"],
        data["goal"]
    )

    return jsonify({
        "result": result,
        "timestamp": datetime.utcnow().isoformat()
    })


# -----------------------------
# Generate Complete Package
# -----------------------------
@app.route("/api/generate-all", methods=["POST"])
def api_all():

    data = request.json

    valid, missing = validate(data)

    if not valid:
        return jsonify({
            "error": f"Missing field: {missing}"
        }), 400

    duration = data.get("duration", 30)

    return jsonify({

        "hook": generate_hook(
            data["product"],
            data["description"],
            data["audience"],
            data["goal"]
        ),

        "script": generate_script(
            data["product"],
            data["description"],
            data["audience"],
            data["goal"],
            duration
        ),

        "scenes": generate_scenes(
            data["product"],
            data["description"],
            data["audience"],
            data["goal"]
        ),

        "cta": generate_cta(
            data["product"],
            data["audience"],
            data["goal"]
        ),

        "timestamp": datetime.utcnow().isoformat()

    })


# -----------------------------
# Run Flask
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)