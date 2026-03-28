from flask import Flask, render_template, session
from pendu import Pendu

import os


# On crée l'application
app = Flask("pendu")
app.secret_key = os.urandom(32)


#Route de base : Page d'accueil
@app.route("/")
def index():
  return render_template('index.html')

  
# On lance l'application
app.run("0.0.0.0","3904", debug=True)