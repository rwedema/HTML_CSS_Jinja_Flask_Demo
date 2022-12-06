'''
Here are all the examples Flask app's that have been discussed during the lectures
Simply uncomment one and run to see how it functions
look for the # TODO parts for you to implement
'''

from lib.basic_Flask_app import app
#from lib.Flask_app_without_templating import app
#from lib.Flask_app_with_templating import app
#from lib.simple_routing import app
#from lib.creating_your_own_error_page import app
#from lib.redirections import app
#from lib.form_handling import app
#from lib.Flask_static_folder import app
#from lib.Jinja2_inheritance import app
#from lib.Flask_create_image import app


if __name__ == '__main__':
    # setting debug on True will restart the server on each change
    app.debug = True
    app.run()
