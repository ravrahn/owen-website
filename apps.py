from flask import Blueprint, abort, redirect, render_template, url_for, request

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
    return render_template('dots.html')
