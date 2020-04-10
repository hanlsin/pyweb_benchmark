#!/bin/sh

export FLASK_APP=./flask/app.py
export FLASK_ENV=development
export FLASK_RUN_PORT=8080
flask run

