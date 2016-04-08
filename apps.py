from flask import Blueprint, abort, redirect, render_template, url_for, request
from render import render_base_template


apps = Blueprint('apps', __name__)

@apps.route('/<app>/')
def show_app(app):
    return app

@apps.route('/csesoc/')
def csesoc():
    return redirect('http://csesoc.unsw.edu.au/')

@apps.route('/etymograph/')
def etymograph():
    return redirect('http://etymograph.com/')

@apps.route('/timetable/')
def timetable():
    return redirect('https://play.google.com/store/apps/details?id=net.ravrahn.timetablr')

@apps.route('/dots/')
def dots():
    return render_base_template('dots.html', sheets=['dots.css'], scripts=['dots.js'])

@apps.route('/connect4/')
def connect4():
    return render_base_template('connect4.html', sheets=['connect4.css', 'qunit-1.20.0.css'], scripts=['modernizr.js', 'board.js', 'ai.js', 'qunit-1.20.0.js', 'tests.js'])