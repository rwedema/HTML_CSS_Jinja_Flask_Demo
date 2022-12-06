from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def simple_form_handling():
    """
    Flask form handling, check if request is GET (default) or POST
    If method is GET show form_GET_bootstrap.html
    if method is POST, get values submitted and insert into form_POST.html
    :return: rendered HTML template
    """

    if request.method == 'GET':
        return render_template('form/form_GET_bootstrap.html')
    elif request.method == 'POST':
        kwargs = {
            'course': request.form['course'],
            'ec': request.form['ec'],
            'teacher': request.form['teacher'],
        }
        return render_template('form/form_POST.html', **kwargs)
