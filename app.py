import os
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config.from_object('config')
ctx = app.app_context()
ctx.push()

def header():
	return ''

@app.route('/')
def home():
	return redirect(url_for('portfolio'))

@app.route('/portfolio/')
def portfolio():
	return render_template('portfolio.html', portfolio=portfolio_list)

@app.route('/apps/')
def apps():
	apps_list = os.listdir('apps')
	return ''

@app.route('/apps/<app>/')
def show_app(app):
	return ''

portfolio_list = [
    {
        'name': 'Etymograph',
        'url': 'http://etymograph.com/',
    },
    {
        'name': 'CSESoc',
        'url': 'http://csesoc.unsw.edu.au/',
    },
    {
        'name': 'Mekong',
        # 'url': url_for('show_app', app='mekong'),
    },
    {
        'name': 'Dots',
        # 'url': url_for('show_app', app='dots'),
    },
    {
        'name': 'Connect 4',
        # 'url': url_for('show_app', app='connect-4'),
    },
    {
        'name': 'Timetable'
    },
]


if __name__ == '__main__':
	app.run(port=8000, debug=True)
