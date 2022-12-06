from flask import Flask, render_template_string, render_template

app = Flask(__name__)


@app.route('/')
def our_first_html_page():
    """
    This function is still bound to the root, but now we use Jinja2 syntax to allow some dynamic content
    The title of the page and the list items are created dynamically
    We use the render_template_string from Flask to fill the placeholders in the string
    :return: rendered HTML page from string
    """

    courses = ['Theme1','Theme2','Theme3','Theme4','Theme5']

    page = """
    <html>
        <head>
            <title>{{ title }}</title>
        </head>
        <body>
            <h1>Finally, my own website</h1>

            <ul>
                {% for course in courses %}
                    <li>{{ course }}</li>
                {% endfor %}
            </ul>
        </body>
    </html>
    """

    rendered_page = render_template_string(page, title='My, first page', courses=courses)
    return rendered_page


@app.route('/second')
def our_second_html_page():
    """
    In this view function the html code is moved to it's own location index.html under the templates folder
    :return: rendered HTML page from template
    """

    courses = ['Theme1','Theme2','Theme3','Theme4','Theme5']

    return render_template('index.html', title='My, second page', courses=courses)


# TODO
# Create a third_html_page() function bound to the address /third that will render a page showing the
# Courses list with alternating text color (red, green) for the items using an appropriate CSS file
# look for the Jinja2 loop.cycle helper to add classes to the items in your HTML template
