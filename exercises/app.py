from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/add')
def add():
	return render_template('add.html', add_student_route())

@app.route('/vote', methods=['GET', 'POST'])
def vote():
	if request.method == 'GET':
		return render_template('from.html')
	else:
		firstname = request.form['firstname']
		theyear = request.form['theyear']

		add_studenr_info(firstname, theyear)

		return render_template('response.html',
		n=firstname,
		s=theyear)

@app.route('/students')
def all_students():
	all_info = get_all_survey_info()
	return render_template('all.html', all_students=all_info)


app.run(debug=True)
