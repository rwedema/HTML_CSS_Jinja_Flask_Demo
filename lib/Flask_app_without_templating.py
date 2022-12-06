from flask import Flask

app = Flask(__name__)


@app.route('/')
def our_first_html_page():
    """
    This function will be called when someone is trying to access the root of the server ('/')
    A hardcoded HTML file will be created and returned
    :return: html page as string
    """

    # string containing a simple HTML page with a header and a bullet list
    page = """
    <html>
        <head>
            <title>Our first page!</title>
        </head>
        <body>
            <h1>Finally, my own website</h1>
            
            <ul>
                <li>Theme01</li>
                <li>Thema02</li>
                <li>Thema03</li>
            </ul>
        </body>
    </html>
    """

    return page



# TODO
# add a new view function bound to the address /second
# return a page with CSS styling, CSS files should be placed under the static folder
