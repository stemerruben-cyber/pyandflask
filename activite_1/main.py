from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/secret")
def secret():
    return render_template("secret.html")
@app.route("/error")
def error():
    error = "Placeholder"
    return render_template("error.html", error=error)
app.run(host="0.0.0.0", port=81)