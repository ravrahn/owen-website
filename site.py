import os
from flask import Flask

app = Flask(__name__)

def header():
	return ''

@app.route('/')
def home():
	return 'Hello world!'

@app.route('/portfolio/')
def portfolio():
	return 'work'

@app.route('/apps/')
def apps():
	apps_list = os.listdir('apps')
	return ''

@app.route('/apps/<app>/')
def show_app(app):
	return ''


if __name__ == '__main__':
	app.run(port=8000)