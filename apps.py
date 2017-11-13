from flask import Blueprint, abort, redirect, render_template, url_for, request
from render import render_base_template


apps = Blueprint('apps', __name__)

@apps.route('/<app>/')
def show_app(app):
    return app

@apps.route('/csesoc/')
def csesoc():
    return redirect('https://csesoc.unsw.edu.au/')

@apps.route('/etymograph/')
def etymograph():
    return redirect('http://etymograph.com/')

@apps.route('/getflix/')
def getflix():
    return redirect('https://chrome.google.com/webstore/detail/getflix-region-switcher/dnglcfmkeagcfmjnhgboabkbjkdnkija')

@apps.route('/pingchart/')
def pingchart():
    return redirect('https://github.com/ravrahn/pingchart')

@apps.route('/timetable/')
def timetable():
    return redirect('https://play.google.com/store/apps/details?id=net.ravrahn.timetablr')

@apps.route('/dots/')
def dots():
    return render_base_template('dots.html', sheets=['dots.css'], scripts=['dots.js'])

@apps.route('/connect4/')
def connect4():
    return render_base_template('connect4.html', sheets=['connect4.css', 'qunit-1.20.0.css'], scripts=['modernizr.js', 'board.js', 'ai.js', 'qunit-1.20.0.js', 'tests.js'])

@apps.route('/github/')
def github():
    return redirect('https://github.com/ravrahn/')

@apps.route('/cv/')
def cv():
    return render_base_template('cv.html')
