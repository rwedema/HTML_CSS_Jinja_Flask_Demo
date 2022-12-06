from flask import Flask, render_template

app = Flask(__name__)

# Global dictionary containing dictionaries with course information as values and course name as key
COURSES_INFORMATION = {
    'theme3': {
        'Full_name': 'thema3, DNA harde schijf van de cel',
        'EC': '5',
        'Teacher': 'WERD,BOJP'
    },
    'informatics3': {
        'Full_name': 'Informatica3',
        'EC': '3',
        'Teacher': 'BOJP'
    }
}

# root route initiated at entry
@app.route('/')
def courses():
    return render_template('simple_routing/courses.html')


# route to the "course.html" given variable "course_name"
@app.route('/course/<course_name>')
def course(course_name):
    return render_template('simple_routing/course.html', course=COURSES_INFORMATION[course_name])
