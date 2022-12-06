from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def root():
    """
    Main entry bound function
    :return: redirection to the address that belongs to the all_your_base() function
    """

    return redirect(url_for('all_your_base'))


# 301 means ULR moved permanently, 302 is default for redirect and is for temporary relocating
@app.route('/index')
def index():
    """
    Entry for the /index url
    :return: redirection to the address that belongs to the all_your_base() function
    """

    return redirect(url_for('all_your_base'), code=301)


@app.route('/courses')
def courses():
    """
    Entry for the /courses url
    :return: redirection to the address that belongs to the all_your_base() function
    """

    return redirect(url_for('all_your_base'), code=302)


@app.route('/all_your_base')
def all_your_base():
    """
    Entry for the /all_your_base url
    All other url's are redirected to this url
    :return: rendered redirection.html template
    """

    return render_template('simple_routing/redirection.html')