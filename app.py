from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import firebase_admin
from firebase_admin import credentials, auth, firestore
import sqlite3
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

cred = credentials.Certificate('firebase_config.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/category')
def category():
    return render_template('category.html')


@app.route('/lobby')
def lobby():
    return render_template('lobby.html')


@app.route('/leaderboard')
def leaderboard():
    leaderboard_ref = db.collection('leaderboard').order_by(
        'score', direction=firestore.Query.DESCENDING).limit(10)
    scores = leaderboard_ref.stream()
    top_scores = [
        {"name": s.get('displayName'), "score": s.get('score')} for s in scores]
    return render_template('leaderboard.html', scores=top_scores)


@app.route('/start_game', methods=['POST'])
def start_game():
    category_map = {
        '9': 'general_knowledge_quiz.db',
        '18': 'computer_science_quiz.db',
        '21': 'general_sports_quiz.db',
        '23': 'history_quiz.db',
        '22': 'geography_quiz.db'
    }

    category = request.form['category']
    difficulty = request.form['difficulty']
    amount = int(request.form['questions'])
    q_type = request.form['type']

    db_path = category_map.get(category)
    if not db_path:
        return jsonify({"error": "Invalid category"}), 400

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = """
            SELECT question_text, option1, option2, option3, option4, correct_answer
            FROM questions
            WHERE difficulty = ?
            ORDER BY RANDOM()
            LIMIT ?
        """
        cursor.execute(query, (difficulty, amount))
        questions = cursor.fetchall()
        conn.close()

        if not questions:
            return jsonify({"error": "No questions found for the selected criteria"}), 400

        question_list = []
        if q_type == 'boolean':
            for q in questions:
                correct_index = q[5] - 1
                options = [q[1], q[2], q[3], q[4]]
                correct_option = options[correct_index]

                is_true = random.choice([True, False])
                if is_true:
                    statement = f"{q[0]} {correct_option}"
                    correct_answer = 1
                else:
                    incorrect_options = [opt for i, opt in enumerate(
                        options) if i != correct_index and opt]
                    if incorrect_options:
                        incorrect_option = random.choice(incorrect_options)
                        statement = f"{q[0]} {incorrect_option}"
                        correct_answer = 2
                    else:

                        statement = f"{q[0]} {correct_option}"
                        correct_answer = 1

                question_list.append({
                    'text': statement,
                    'options': ['True', 'False'],
                    'correct': correct_answer
                })
        else:
            for q in questions:
                question_list.append({
                    'text': q[0],
                    'options': [q[1], q[2], q[3], q[4]],
                    'correct': q[5]
                })

        random.shuffle(question_list)

        session['questions'] = question_list
        if 'score' not in session:
            session['score'] = 0
        if 'correct_answers' not in session:
            session['correct_answers'] = 0
        if 'wrong_answers' not in session:
            session['wrong_answers'] = 0
        session['current'] = 0
        session['difficulty'] = difficulty
        session['category'] = category
        session['total_questions'] = amount
        session['type'] = q_type

        return redirect(url_for('gamepage'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/gamepage')
def gamepage():
    if 'questions' not in session:
        return redirect(url_for('category'))

    return render_template('gamepage.html',
                           questions=session['questions'],
                           difficulty=session['difficulty'],
                           category=session['category'],
                           total_questions=session['total_questions'],
                           score=session['score'],
                           correct_answers=session['correct_answers'],
                           wrong_answers=session['wrong_answers'],
                           current=session['current'],
                           q_type=session['type'])


@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.json
    uid = data.get("uid")
    name = data.get("name")
    score = data.get("score")

    if not all([uid, name, score]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        user_ref = db.collection('leaderboard').document(uid)
        user_doc = user_ref.get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            current_score = user_data.get('score', 0)
            new_score = current_score + score
        else:
            new_score = score

        user_ref.set({
            'displayName': name,
            'score': new_score,
            'timestamp': firestore.SERVER_TIMESTAMP
        }, merge=True)

        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
