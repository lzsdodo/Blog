#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)           # 实例化
app.config.from_object(Config)  # 引入配置

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
