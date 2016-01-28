from flask import Blueprint, abort, redirect, url_for, request

apps = Blueprint('apps', __name__)

@apps.route('/<app>/')
def show_app(app):
    if app == 'csesoc':
        return redirect('http://csesoc.unsw.edu.au/')
    elif app == 'etymograph':
        return redirect('http://etymograph.com/')
    elif app == 'timetable':
        return redirect('https://play.google.com/store/apps/details?id=net.ravrahn.timetablr')
    else:
        return app