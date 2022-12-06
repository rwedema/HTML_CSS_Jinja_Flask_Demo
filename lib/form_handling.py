from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def simple_form_handling():
    if request.method == 'GET':
        # default response when a form is called. Renders 'form/form_GET.html'
        return render_template('form/form_GET.html')

    elif request.method == 'POST':
        # response when the submit button is clicked in the 'form/form_GET.html'
        # pack the variables in a dictionary
        kwargs = {
            'course': request.form['course'],
            'ec': request.form['ec'],
            'teacher': request.form['teacher'],
        }
        # render the 'form_POST.html' with the variables collected from the form in 'form_GET.html'
        return render_template('form/form_POST.html', **kwargs)
