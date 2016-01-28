import os
from flask import Flask, redirect, render_template, redirect, url_for

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

from apps import apps

app.register_blueprint(apps, url_prefix='/apps')

portfolio_list = [
    {
        'name': 'Etymograph',
        'url': 'etymograph',
    },
    {
        'name': 'CSESoc',
        'url': 'csesoc',
    },
    {
        'name': 'Mekong',
        'url': 'mekong',
    },
    {
        'name': 'Dots',
        'url': 'dots',
    },
    {
        'name': 'Connect 4',
        'url': 'connect-4',
    },
    {
        'name': 'Timetable',
        'url': 'timetable',
    },
]


if __name__ == '__main__':
    app.run(port=8000, debug=True)
