from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

add_student("a", 1, False)
add_student("b", 2, False)
add_student("c", 3, True)
add_student("d", 4, True)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('studentl.html', student=query_by_id(student_id))

app.run(debug=True)
