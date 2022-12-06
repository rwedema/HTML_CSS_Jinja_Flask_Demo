from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def root():
    """
    Browsing to the root of the server will execute the root() function
    rendering the base.html
    :return: rendered HTML file base.html
    """
    return render_template('Jinja2_inheritance/base.html')


@app.route('/add_course')
def add_course():
    """
    Browsing to server/add_course, will show the form_base_inheritance.html file
    :return: rendered form_base_inheritance.html file
    """
    if request.method == 'GET':
        return render_template('Jinja2_inheritance/form_base_inheritance.html')
