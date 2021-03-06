from flask import render_template

def render_base_template(template, title=None, sheets=[], scripts=[], **kwargs):
    page_title = 'Owen Cassidy'
    if title is not None:
        page_title = title + ' | ' + page_title

    sheets = ['foundation.css', 'style.css'] + sheets

    scripts = ['jquery-2.2.0.min.js', 'foundation.min.js'] + scripts

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
            'name': 'My Github',
            'url': 'github'
        },
        {
            'name': 'My CV',
            'url': 'cv'
        },
    ]

    kwargs['title'] = page_title
    kwargs['scripts'] = scripts
    kwargs['sheets'] = sheets
    kwargs['sites'] = sites

    return render_template(template,
        **kwargs)