import os
from flask import Flask, redirect, render_template, redirect, url_for

app = Flask(__name__)
app.config.from_object('config')
ctx = app.app_context()
ctx.push()

def navbar():
    return render_template('navbar.html',
        sites=sites)
app.jinja_env.globals.update(navbar=navbar)

def head(title=None, sheets=[], scripts=[]):
    page_title = 'Owen Cassidy'
    if title is not None:
        page_title = title + ' | ' + page_title

    sheets = ['foundation.css', 'style.css'] + sheets

    scripts = ['jquery-2.2.0.min.js', 'foundation.js'] + scripts

    return render_template('head.html',
        title=page_title,
        scripts=scripts,
        sheets=sheets)

app.jinja_env.globals.update(head=head)

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
        'date': '2015-Ongoing',
        'image': 'etymograph.png',
        'desc': 'Etymograph is a web service designed to store word etymologies in a structured way. It was originally developed by me and four others as part of a large university project. Since then, I have been the sole developer. It is written in Python 3 using Flask, and makes use of several Javascript libraries for data visualisation. I have made major contributions to the entire web stack for this project, including the database, the backend, and the frontend.'
    },
    {
        'name': 'CSESoc',
        'url': 'csesoc',
        'date': '2014',
        'image': 'csesoc.png',
        'desc': 'In early 2014, I volunteered to help the UNSW Computer Science society to create a new website. I designed the entirely of the site’s front-end, created almost all of the Django HTML templates, and wrote all of the CSS and Javascript. Over the course of creating this website, I taught myself Javascript.'
    },
    {
        'name': 'Mekong',
        'url': 'mekong',
        'date': '2013',
        'image': 'mekong.png',
        'desc': 'My first web project was a simple CGI-based bookstore website written in Python, carried out in a software development course. While most students used a simple template such as Bootstrap when designing the front-end, I took it as an opportunity to learn web design and CSS, and wrote all the CSS myself. The back-end was a rudimentary templating engine based on Python string formatting, and was heavily functional. I achieved a nearly-perfect mark for this project.'
    },
    {
        'name': 'Dots',
        'url': 'dots',
        'date': '2014',
        'image': 'dots.png',
        'desc': 'Dots is a static web app I created. It calculates the dots-per-inch of a display given a width and height in pixels, and a diagonal in inches. This web app gave me substantially more experience in Javascript, as well as HTML and CSS.'
    },
    {
        'name': 'Connect 4',
        'url': 'connect-4',
        'date': '2014, updated 2016',
        'image': 'connect4.png',
        'desc': 'A simple connect four game with a simple min-max AI that I initially built in mid 2014. I updated the algorithm in 2016 to fix some issues that it had.'
    },
    {
        'name': 'Timetable',
        'url': 'timetable',
        'date': '2011-2013',
        'image': 'timetable.png',
        'desc': 'The first major software project I had was an Android app I wrote called Timetable. It stored a high school student’s timetable in a database and displayed it to them. It used an SQLite database, an XML front-end and a Java back-end. Its primary focus was on user interface design, and in creating it I learnt both basic Java and XML.'
    },
]

sites = [
    {
        'name': 'Etymograph',
        'url': 'etymograph',
    },
    {
        'name': 'Dots',
        'url': 'dots',
    },
    {
        'name': 'Connect 4',
        'url': 'connect-4',
    },
]


if __name__ == '__main__':
    app.run(port=8000, debug=True)
