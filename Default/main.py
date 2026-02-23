from flask import Flask, render_template, request, make_response
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key at runtime

print("Secret key generated at runtime:", app.secret_key)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/1")
def page1():
    resp = make_response(render_template("index.html"))
    pressed = request.cookies.get("pressed", "")
    pressed += "1,"
    resp.set_cookie("pressed", pressed) 
    return resp

@app.route("/2")
def page2():
    resp = make_response(render_template("index.html"))
    pressed = request.cookies.get("pressed", "")
    pressed += "2,"
    resp.set_cookie("pressed", pressed)
    return resp

@app.route("/3")
def page3():
    resp = make_response(render_template("index.html"))
    pressed = request.cookies.get("pressed", "")
    pressed += "3,"
    resp.set_cookie("pressed", pressed)
    return resp

@app.route("/end")
def end():
    pressed = request.cookies.get("pressed", "")
    pressed_list = pressed.strip(",").split(",") if pressed else []
    return render_template("end.html", pressed_list=pressed_list)

app.run(host="0.0.0.0", port=81)