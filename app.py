from flask import Flask, render_template, request, redirect
from database.db_connection import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/students')
def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return render_template('view_students.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Students (name, email, course) VALUES (?, ?, ?)", (name, email, course))
        conn.commit()
        conn.close()

        return redirect('/students')
    return render_template('add_student.html')

if __name__ == '__main__':
    app.run(debug=True)
