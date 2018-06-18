#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import abort, redirect, url_for
from flask import render_template
from app import app

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# Error handler
@app.errorhandler(404)
def error_404(error):
    return '404 Not Found',404

