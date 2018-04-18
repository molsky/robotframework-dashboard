#!/usr/bin/env python

from flask import render_template, request, redirect, Response, session, url_for
from rfwebui import app
from funcs.helper import ConfigSectionMap, save_settings, read_settings
from glob import glob
from subprocess import Popen
from os import getcwd, path, makedirs
import json


results_dir = getcwd() + "/results/"
if not path.exists(results_dir):
    makedirs(results_dir)


def split_filter(s):
    return s.split('.')[0]


app.jinja_env.filters['split'] = split_filter


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if not path.isfile("app_configs/settings.ini"):
        return redirect(url_for('settings'))
    working_dir = ConfigSectionMap("FILES")['path']
    types = (working_dir + '*.robot', working_dir + '*.txt')
    files_grabbed = []
    for files in types:
        fwp = glob(files)
        for item in fwp:
            files_grabbed.append(item.replace(working_dir, ''))
    if not files_grabbed:
        files_grabbed.append('Nothing to show')  # TODO: redirect to error page with proper message
    return render_template('index.html',
                           title='RF Dashboard',
                           tests=files_grabbed)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    app_settings = read_settings()
    print(app_settings)
    if request.method == 'POST':
        save_settings(request.form['dir_path'])
    return render_template('settings.html',
                           title='RF Dashboard - Settings',
                           settings=app_settings)


@app.route('/cmd', methods=['POST'])
def cmd():
    working_dir = ConfigSectionMap("FILES")['path']
    command = request.form.get('data')
    output_dir = results_dir + command.split('.')[0] + '/'
    proc = Popen(["robot", "-d", output_dir, working_dir + command])
    proc.wait()
    sjson = json.dumps({'test_name': command, 'status_code': proc.returncode})
    return Response(sjson, content_type='text/event-stream')


@app.route('/results')
def results():
    return redirect(url_for('results'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Page not found')


@app.errorhandler(405)
def page_error(e):
    return render_template('405.html', title='Something unexpected happened')
