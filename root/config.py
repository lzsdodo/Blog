#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    POSTS_PER_PAGE = 20

    PERMANENT_SESSION_LIFETIME = timedelta(days=31) # Default: days=31 会话时间
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1) # default: hours=12 设置缓存时间

