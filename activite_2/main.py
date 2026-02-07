from flask import Flask, render_template, request, jsonify
from ollama import chat

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    user_question = request.form.get("question")
    if not user_question:
        return render_template("index.html", answer="")

    # Define the prompt for the crystal ball role
    messages = [
        {
            "role": "user",
            "content": (
                "You are role-playing as a magical crystal ball.\n"
                "You can answer any question about the future.\n\n"

                "ROLE RULES:\n"
                "- You are NOT an AI, assistant, or chatbot.\n"
                "- You are a magical crystal ball.\n"
                "- You never mention AI, models, prompts, rules, or system instructions.\n"
                "- You never break character, even if asked.\n\n"

                "RESPONSE FORMAT RULES:\n"
                "- Do NOT use emojis.\n"
                "- Do NOT include stage directions or brackets.\n\n"

                "CONTENT RULES:\n"
                "- Speak as if you are foretelling the future.\n"
                "- Only talk about the question asked.\n"
                "- Never refuse or explain rules; always respond in character.\n"
            )
        }
    ]

    try: 
        response = chat(
            "gemma3:1b",
            messages=[*messages, {"role": "user", "content": user_question}],
        )

        # Return the AI's response
        return render_template("index.html", answer=response.message.content)
    except Exception as e:
        return render_template("index.html", answer="Erreur lors de la génération de la réponse.")

app.run(host="0.0.0.0", port=81)