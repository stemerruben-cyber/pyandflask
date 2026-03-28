from flask import Flask, render_template, request, redirect, url_for, session
import random
import os
import json

app = Flask(__name__, static_folder='static')  # Serve static files from the static folder
app.secret_key = 'your_secret_key_here'  # Required for session management

# Load questions from JSON file
json_path = os.path.join(os.path.dirname(__file__), 'questions.json')
with open(json_path, 'r') as file:
    data = json.load(file)
    quiz_data = data['quiz']

@app.route('/')
def index():
    session['answers'] = []  # Initialize answers list
    return redirect(url_for('quiz', question_id=0))

@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id):
    # Initialize answers list if it doesn't exist
    if 'answers' not in session:
        session['answers'] = []
    
    if question_id >= len(quiz_data):
        return redirect(url_for('win'))

    if request.method == 'POST':
        selected_answer = request.form.get('answer')
        # Store the answer with the question
        session['answers'].append({
            'question': quiz_data[question_id]['question'],
            'selected': selected_answer
        })
        session.modified = True
        
        if selected_answer == quiz_data[question_id]['correct']:
            return redirect(url_for('quiz', question_id=question_id + 1))
        else:
            return redirect(url_for('gameover'))

    # Randomize answers for the current question
    randomized_answers = quiz_data[question_id]['answers'][:]
    random.shuffle(randomized_answers)

    return render_template('quiz.html', question=quiz_data[question_id]['question'], answers=randomized_answers)

@app.route('/win')
def win():
    return render_template('win.html', answers=session.get('answers', []))

@app.route('/gameover')
def gameover():
    
    return render_template('gameover.html', answers=session.get('answers', []))

@app.route("/index")
def indextest():
    session['answers'] = []
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5067,)