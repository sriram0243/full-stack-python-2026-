from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database & table
def init_db():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Add student
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']

    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

    return redirect('/students')

# Display all students
@app.route('/students')
def students():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()

    return render_template('student.html', students=data)

if __name__ == '__main__':
    app.run(debug=True)
