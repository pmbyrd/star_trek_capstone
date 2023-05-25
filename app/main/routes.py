from flask import render_template
from app.main import main
#LINK - https://flask.palletsprojects.com/en/1.1.x/blueprints/
#TODO - fix the user model to handle the flask login from within the main blueprint


#NOTE - The main blueprint is used for all the routes that are not specific to a particular blueprint
@main.route('/')
def index():
	return render_template('index.html')

@main.route('/test')
def test_page():
	return 'This is a test page'