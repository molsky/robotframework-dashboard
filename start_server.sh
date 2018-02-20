#!/bin/bash

VENV_DIRECTORY=rfd-venv

source "$VENV_DIRECTORY/bin/activate"

cd src/rfwebui

gunicorn --bind 0.0.0.0:8000 wsgi:app
