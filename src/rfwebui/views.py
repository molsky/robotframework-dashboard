#!/usr/bin/env python

from flask import render_template, request, redirect, Response, session, url_for, jsonify
from rfwebui import app
from rfwebui.code.helper import ConfigSectionMap
from glob import glob
from subprocess import Popen
import json


working_dir = ConfigSectionMap("Files")['path']


def split_filter(s):
    return s.split('.')[0]
app.jinja_env.filters['split'] = split_filter


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    types = (working_dir + '*.robot', working_dir + '*.txt')
    files_grabbed = []
    for files in types:
        fwp = glob(files)
        for item in fwp:
            files_grabbed.append(item.replace(working_dir, ''))
    if not files_grabbed:
        files_grabbed.append('Nothing to show')  # TODO: redirect to error page with proper message
    return render_template('index.html',
                           title='RF - Web UI',
                           tests=files_grabbed)


@app.route('/cmd', methods=['POST'])
def cmd():
    command = request.form.get('data')
    proc = Popen(["robot", working_dir + command])
    proc.wait()
    sjson = json.dumps({'test_name': command, 'status_code': proc.returncode})
    return Response(sjson, content_type='text/event-stream')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Page not found')


@app.errorhandler(405)
def page_error(e):
    return render_template('405.html', title='Something unexpected happened')
