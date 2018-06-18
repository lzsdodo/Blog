#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers