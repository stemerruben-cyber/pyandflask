from flask import Flask, render_template, request, redirect, url_for
import random
import os

app = Flask(__name__, static_folder='static')  # Serve static files from the static folder

# Questions, answers, and correct answers
questions = [
    "2 + 2 = ?",
    "5 + 3 = ?",
    "10 - 7 = ?"
]

answers = [
    ["3", "4", "5"],
    ["7", "8", "9"],
    ["2", "3", "4"]
]

correct_answers = ["4", "8", "3"]

@app.route('/')
def index():
    return redirect(url_for('quiz', question_id=0))

@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id):
    if question_id >= len(questions):
        return redirect(url_for('win'))

    if request.method == 'POST':
        selected_answer = request.form.get('answer')
        if selected_answer == correct_answers[question_id]:
            return redirect(url_for('quiz', question_id=question_id + 1))
        else:
            return redirect(url_for('gameover'))

    # Randomize answers for the current question
    randomized_answers = answers[question_id][:]
    random.shuffle(randomized_answers)

    return render_template('quiz.html', question=questions[question_id], answers=randomized_answers)

@app.route('/win')
def win():
    return render_template('win.html')

@app.route('/gameover')
def gameover():
    return render_template('gameover.html')

@app.route("/index")
def indextest():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5067,)