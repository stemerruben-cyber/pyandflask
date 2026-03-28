from flask import Flask, render_template, session, request, redirect, url_for
from pendu import Pendu
import os


# On crée l'application
app = Flask("pendu")
app.secret_key = os.urandom(32)
print(f"Secret Key: {app.secret_key}") # This is for debugging purposes, you can remove this line in production

def load_strings(strname):
    f = open("strings.json", "r")
    data = f.read()
    f.close()
    return {"strings":[strname]}


#Route de base : Page d'accueil 
@app.route("/")
def index():
    data = request.args.get("data")
    if data is None:
        data = "Bienvenue au jeu du pendu !"
        return redirect(url_for("reset", data=data))
    return render_template('index.html', data=data)

@app.route("/submit", methods=["POST"])
def submit():
    user_input = request.form["user_input"]
    if not user_input or len(user_input) != 1:
        return redirect(url_for("index", data="Please enter a single character."))  # Redirect back to the index page with an error message
    # Process the user input here
    return redirect(url_for("index", data=user_input))  # Redirect to the index page with the user input as a query parameter

@app.route("/reset")
def reset():
    data = request.args.get("data")
    session.clear()  # Clear the session to reset the game state
    #session["pendu"] = Pendu("magic", 6)  # Reinitialize the Pendu game
    return redirect(url_for("index", data=data))

print(load_strings("welcome"))

# On lance l'application
app.run("0.0.0.0","3904", debug=True)