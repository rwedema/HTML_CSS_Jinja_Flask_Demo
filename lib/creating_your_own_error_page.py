from flask import Flask, render_template, abort

app = Flask(__name__)

# global dictionary holding course information
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


@app.route('/')
def courses():
    """
    This function will be called when the root of the server is accessed
    :return: rendered template courses.html
    """
    
    return render_template('simple_routing/courses.html')


@app.route('/course/<course_name>')
def course(course_name):
    """
    Called from /course/<course_name>
    <course_name> will be passed as variable to the course function
    If course_name is not found in the COURSES_INFORMATION dictionary, abort with 404 error
    return rendered course.html passing course information to the page
    :param course_name:
    :return: rendered course.html
    """

    if course_name not in COURSES_INFORMATION:
        abort(404)
    return render_template('simple_routing/course.html', course=COURSES_INFORMATION[course_name])


@app.errorhandler(404)
def page_not_found(error):
    """
    Function to catch and handle the 404 errors
    :param error:
    :return: rendered own defined 404.html
    """
    return render_template('Personal_error_pages/404.html'), 404


# TODO
# add a new view function that will be bound to the address /Secret and will abort with a 403 error
# Add a errorhandler function to handle the 403 error, rendering a new 403 template with the text "forbidden"
