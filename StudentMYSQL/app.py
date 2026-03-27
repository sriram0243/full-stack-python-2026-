from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # your MySQL username
    password="root",  # your MySQL password
    database="student_db"
)

cursor = db.cursor()


# Home Page - Form
@app.route('/')
def index():
    return render_template('index.html')


# Add Student
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']

    query = "INSERT INTO students (name) VALUES (%s)"
    cursor.execute(query, (name,))
    db.commit()

    return redirect('/students')


# Display Students
@app.route('/students')
def students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    return render_template('student.html', students=data)


if __name__ == '__main__':
    app.run(debug=True)