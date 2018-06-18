#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from app import app

#def connect_db():
#    """Connects to the specific database."""
#    return None

#def init_db():
#    pass


from flask import render_template


if __name__ == '__main__':
    app.debug = True
    app.run()
    #app.run(host='0.0.0.0', port='80')
